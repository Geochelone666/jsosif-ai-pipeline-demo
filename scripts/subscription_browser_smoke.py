"""Exercise the portal using synthetic Auth/RPC responses; no live requests or email."""
import argparse
from copy import deepcopy
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright, expect

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--site',type=Path,required=True)
parser.add_argument('--artifacts',type=Path,default=Path('review/subscription-browser'))
args=parser.parse_args();args.artifacts.mkdir(parents=True,exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(args.site.resolve())))
Thread(target=server.serve_forever,daemon=True).start()
base='http://127.0.0.1:'+str(server.server_address[1])
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=os.environ.get('BROWSER_EXECUTABLE') or None,headless=True,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':390,'height':844});errors=[]
  page.on('pageerror',lambda error:errors.append(str(error)))
  page.goto(base+'/subscriptions.html')
  expect(page.locator('#status')).to_contain_text('not yet enabled')
  assert not page.locator('#login').is_visible()
  page.route('**/portal-config.json',lambda route:route.fulfill(json={'enabled':True,'url':'https://portal-test.supabase.co','publishable_key':'sb_publishable_synthetic'}))
  state={'version':1,'approved':True,'failed':False,'conflict':False,'saves':[],'emails':0,
         'preferences':{'name':'Example Analyst','groups':['tech'],'tickers':['CSCO'],'enabled':True,
                        'timezone':'America/Toronto','send_weekday':1,'send_time':'09:00'}}
  def api(route):
   req=route.request;path=req.url.split('.supabase.co')[1];data=req.post_data_json
   assert req.headers['apikey']=='sb_publishable_synthetic'
   if path=='/auth/v1/otp':
    assert req.headers.get('authorization') is None
    assert data['email']=='analyst@example.com';state['emails']+=1;route.fulfill(json={})
   elif path=='/auth/v1/verify':
    assert data['token']=='12345678'
    route.fulfill(json={'access_token':'synthetic-session','expires_in':3600,'user':{'email':'analyst@example.com'}})
   else:
    assert req.headers.get('authorization')=='Bearer synthetic-session'
    if path.endswith('subscription_options'):
     if not state['approved']:route.fulfill(status=403,json={});return
     route.fulfill(json={'groups':{'tech':{'name':'Technology','tickers':['CSCO']}},'tickers':['CSCO','JPM']})
    elif path.endswith('get_my_subscription'):
     route.fulfill(json={'version':state['version'],'updated_at':'2026-11-05T10:00:00Z','preferences':state['preferences']})
    elif path.endswith('save_my_subscription'):
     assert 'email' not in data['p_preferences'] and 'id' not in data['p_preferences']
     state['saves'].append(deepcopy(data))
     if not state['failed']:
      state['failed']=True;route.abort();return
     if state['conflict']:
      state['conflict']=False;state['version']=3;route.fulfill(status=409,json={});return
     assert data['p_expected_version']==state['version']
     state['version']+=1;state['preferences']=deepcopy(data['p_preferences'])
     route.fulfill(json={'version':state['version'],'updated_at':'2026-11-05T11:00:00Z'})
    elif path=='/auth/v1/user':
     assert data=={'email':'new@example.com'};route.fulfill(json={})
    elif path=='/auth/v1/logout':route.fulfill(status=204)
    else:raise AssertionError('Unexpected mocked endpoint')
  page.route('https://portal-test.supabase.co/**',api)
  def login():
   page.locator('#email').fill('analyst@example.com');page.get_by_role('button',name='Send sign-in code',exact=True).click()
   page.locator('#code').wait_for(state='visible');page.locator('#code').fill('12345678');page.get_by_role('button',name='Verify code',exact=True).click()
  page.reload();page.locator('#email').wait_for(state='visible');login()
  page.locator('#account').wait_for(state='visible')
  page.locator('#tickers').fill('CSCO, JPM');page.get_by_role('button',name='Save preferences',exact=True).click()
  expect(page.locator('#status')).to_contain_text('could not be completed')
  page.get_by_role('button',name='Save preferences',exact=True).click()
  expect(page.locator('#status')).to_contain_text('Preferences saved')
  assert state['saves'][0]==state['saves'][1], 'Ambiguous retry must retain request ID and payload'
  state['conflict']=True;page.locator('#enabled').uncheck();page.get_by_role('button',name='Save preferences',exact=True).click()
  expect(page.locator('#status')).to_contain_text('changed elsewhere')
  assert page.locator('#save').is_disabled()
  page.get_by_role('button',name='Reload saved settings',exact=True).click()
  expect(page.locator('#version')).to_contain_text('version: 3')
  page.locator('#enabled').uncheck();page.get_by_role('button',name='Save preferences',exact=True).click()
  expect(page.locator('#version')).to_contain_text('version: 4')
  assert not state['preferences']['enabled']
  page.locator('#new-email').fill('new@example.com');page.get_by_role('button',name='Request email change',exact=True).click()
  expect(page.locator('#status')).to_contain_text('Email change requested')
  assert page.evaluate('localStorage.length===0 && sessionStorage.length===0')
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.screenshot(path=str(args.artifacts/'subscription-settings-mobile.png'),full_page=True)
  page.get_by_role('button',name='Sign out',exact=True).click();page.locator('#account').wait_for(state='hidden')
  assert page.locator('#name').input_value()==''
  state['approved']=False;login()
  expect(page.locator('#status')).to_contain_text('approve')
  assert not page.locator('#account').is_visible()
  assert errors==[],errors
  print('Portal browser checks passed: disabled gate, login, read/write, idempotent retry, conflict, opt-out, email-change request, logout, approval denial and mobile layout; all Auth/RPC requests mocked')
  browser.close()
finally:
 server.shutdown();server.server_close()
