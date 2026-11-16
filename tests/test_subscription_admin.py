from copy import deepcopy
import io
import json
import stat
import subprocess
import sys
from urllib.error import HTTPError

import pytest

from subscription_admin import apply, inspect_account, prepare, rpc, validate_plan

USER='00000000-0000-0000-0000-000000000001'
ADMIN='00000000-0000-0000-0000-000000000004'
ENV={'SUBSCRIPTIONS_SUPABASE_URL':'https://admin-test.supabase.co',
     'SUBSCRIPTIONS_PUBLISHABLE_KEY':'sb_publishable_synthetic',
     'SUBSCRIPTIONS_ADMIN_TOKEN':'synthetic-admin-token'}


@pytest.fixture
def inspection():
    return {'schema_version':1,'project_url':ENV['SUBSCRIPTIONS_SUPABASE_URL'],
            'subscription':{'operator_id':ADMIN,'user_id':USER,'member_id':'legacy-stable',
                            'version':3,'approved':True,'preferences':{'enabled':False}}}


def test_prepare_is_offline_preserves_expected_state_and_creates_retry_identity(inspection):
    original=deepcopy(inspection)
    plan=prepare(inspection,approval='revoke',reason=' Requested access revocation ')
    assert plan['arguments']['p_preferences'] is None
    assert plan['arguments']['p_expected_approved'] is True
    assert plan['arguments']['p_approved'] is False
    assert plan['arguments']['p_expected_actor']==ADMIN
    assert plan['arguments']['p_expected_version']==3
    assert inspection==original


def test_inspect_checks_target_and_keeps_history_private():
    calls=[]
    def call(name,args):
        calls.append(name)
        if name.endswith('history'):return [{'reason':'Private administrative context'}]
        return {'operator_id':ADMIN,'user_id':USER,'version':3,'approved':True}
    result=inspect_account(USER,call=call,env=ENV)
    assert len(calls)==2 and result['recent_history'][0]['reason'].startswith('Private')


def test_credential_request_is_bounded_and_errors_are_sanitized():
    def opener(request,timeout):
        assert timeout==20
        assert request.full_url=='https://admin-test.supabase.co/rest/v1/rpc/get_admin_subscription'
        assert request.headers['Authorization']=='Bearer synthetic-admin-token'
        assert request.headers['Apikey']=='sb_publishable_synthetic'
        raise HTTPError(request.full_url,403,'PRIVATE_BACKEND_TEXT',{},io.BytesIO(b'PRIVATE_IDENTITY'))
    with pytest.raises(ValueError) as error:
        rpc('get_admin_subscription',{'p_user_id':USER},env=ENV,opener=opener)
    assert 'PRIVATE' not in str(error.value) and 'synthetic-admin-token' not in str(error.value)


@pytest.mark.parametrize('change',[
    {'SUBSCRIPTIONS_SUPABASE_URL':'https://user:password@admin-test.supabase.co'},
    {'SUBSCRIPTIONS_PUBLISHABLE_KEY':'sb_secret_forbidden'},
    {'SUBSCRIPTIONS_ADMIN_TOKEN':''},
    {'SUBSCRIPTIONS_ADMIN_TOKEN':'token\nInjected: yes'},
])
def test_bad_credentials_never_dispatch(change):
    with pytest.raises(ValueError):
        rpc('get_admin_subscription',{},env={**ENV,**change},opener=lambda *a,**kw:pytest.fail('network dispatched'))


@pytest.mark.parametrize('change',[
    {'p_expected_version':True}, {'p_expected_version':-1}, {'p_expected_approved':'true'},
    {'p_approved':None}, {'p_expected_actor':'not-a-uuid'}, {'p_request_id':'not-a-uuid'},
    {'p_reason':' '}, {'p_reason':'line\nbreak'}, {'p_reason':'x'*1001},
    {'p_preferences':{'email':'forbidden@example.com'}},
])
def test_invalid_review_rejected_before_any_call(inspection,change):
    plan=prepare(inspection,approval='revoke',reason='Correction')
    plan['arguments'].update(change)
    with pytest.raises(ValueError):validate_plan(plan)


def test_apply_keeps_request_id_and_unconfirmed_receipt_after_lost_response(inspection,tmp_path):
    plan=prepare(inspection,approval='revoke',reason='Correction')
    original=deepcopy(plan);calls=[]
    first=tmp_path/'first.json';second=tmp_path/'retry.json'
    def call(name,args):
        calls.append(deepcopy(args))
        if len(calls)==1:
            assert json.loads(first.read_text())['status']=='unconfirmed'
            raise ValueError('lost response')
        return {'request_id':args['p_request_id'],'user_id':USER,'operator_id':ADMIN,
                'version':4,'approved':False,'member_id':'legacy-stable'}
    with pytest.raises(ValueError):apply(plan,first,call=call,env=ENV)
    assert json.loads(first.read_text())['status']=='unconfirmed'
    result=apply(plan,second,call=call,env=ENV)
    assert calls[0]==calls[1] and plan==original
    assert result['member_id']=='legacy-stable'
    assert json.loads(second.read_text())['status']=='confirmed'
    assert all(stat.S_IMODE(p.stat().st_mode)==0o600 for p in (first,second))
    with pytest.raises(FileExistsError):apply(plan,second,call=lambda *a:pytest.fail('overwrite dispatched'),env=ENV)


def test_plan_cannot_be_replayed_on_another_project(inspection,tmp_path):
    plan=prepare(inspection,approval='revoke',reason='Correction')
    with pytest.raises(ValueError):
        apply(plan,tmp_path/'receipt',call=lambda *a:pytest.fail('wrong project dispatched'),
              env={**ENV,'SUBSCRIPTIONS_SUPABASE_URL':'https://other-project.supabase.co'})
    assert not (tmp_path/'receipt').exists()


def test_mismatched_response_never_claims_success(inspection,tmp_path):
    plan=prepare(inspection,approval='revoke',reason='Correction')
    receipt=tmp_path/'receipt'
    with pytest.raises(ValueError):apply(plan,receipt,call=lambda *a:{'request_id':'wrong'},env=ENV)
    assert json.loads(receipt.read_text())['status']=='unconfirmed'


def test_offline_cli_prepare_needs_no_credentials_and_refuses_overwrite(inspection,tmp_path):
    source=tmp_path/'inspection.json';source.write_text(json.dumps(inspection))
    reason=tmp_path/'reason.txt';reason.write_text('Private access review')
    output=tmp_path/'plan.json'
    command=[sys.executable,'scripts/subscription_admin.py','prepare','--inspection',str(source),
             '--approval','revoke','--reason-file',str(reason),'--output',str(output)]
    result=subprocess.run(command,capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    plan=json.loads(output.read_text())
    assert plan['arguments']['p_expected_actor']==ADMIN and plan['arguments']['p_approved'] is False
    assert 'Private access review' not in result.stdout and ADMIN not in result.stdout
    assert stat.S_IMODE(output.stat().st_mode)==0o600
    retry=subprocess.run(command,capture_output=True,text=True)
    assert retry.returncode!=0 and json.loads(output.read_text())==plan


def test_oversized_rpc_response_is_rejected_without_private_diagnostics():
    with pytest.raises(ValueError) as error:
        rpc('get_admin_subscription',{},env=ENV,opener=lambda *a,**kw:io.BytesIO(b'X'*(2*1024*1024+1)))
    assert str(error.value)=='Administrator request failed; no success confirmed'
