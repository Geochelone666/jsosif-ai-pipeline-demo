"""Reviewed deployment records shared by the public changelog and weekly digests."""
from datetime import datetime, timezone
import hashlib
from html import escape
import json
from pathlib import Path
import re

CATALOG = Path(__file__).resolve().parents[1] / 'config/release_announcements.json'
SITE = 'https://geochelone666.github.io/jsosif-ai-pipeline-demo/'
KINDS = {'feature', 'report_structure', 'data_correction', 'delivery_policy', 'maintenance'}


def instant(value):
    if not isinstance(value, str):
        raise ValueError('Release timestamp must be text')
    stamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if stamp.utcoffset() is None:
        raise ValueError('Release times require a timezone')
    return stamp


def text(value, limit):
    return isinstance(value, str) and 0 < len(value.strip()) <= limit and not any(ord(c) < 32 for c in value)


def load(path=None):
    payload = json.loads(Path(path or CATALOG).read_text(encoding='utf-8'))
    if (not isinstance(payload, dict) or set(payload) != {'schema_version', 'releases'} or
            type(payload['schema_version']) is not int or payload['schema_version'] != 1 or
            not isinstance(payload['releases'], list)):
        raise ValueError('Invalid release catalogue')
    ids = set()
    for item in payload['releases']:
        required = {'id','version','title','summary','kind','status','audience','url'}
        if (not isinstance(item, dict) or not required <= item.keys() or
                set(item) - required - {'deployed_at','verified_at','evidence_url'}):
            raise ValueError('Invalid release record')
        if (not isinstance(item['id'], str) or not re.fullmatch(r'[a-z0-9][a-z0-9._-]{0,79}',item['id']) or
                item['id'] in ids or not text(item['version'],40) or not text(item['title'],120) or
                not isinstance(item['kind'], str) or item['kind'] not in KINDS or
                item['status'] not in ('draft','published','withdrawn') or
                not isinstance(item['summary'],list) or not 1 <= len(item['summary']) <= 2 or
                not all(text(line,280) for line in item['summary'])):
            raise ValueError('Invalid release identity or content')
        ids.add(item['id'])
        # Public links stay inside the reviewed project, without queries or credentials.
        if (not isinstance(item['url'], str) or not item['url'].startswith(SITE) or
                not re.fullmatch(r'[A-Za-z0-9_./#-]*',item['url'][len(SITE):]) or
                '..' in item['url'][len(SITE):].split('/')):
            raise ValueError('Release link must stay on the project site')
        audience = item['audience']
        if not isinstance(audience,dict) or set(audience) != {'groups','tickers'}:
            raise ValueError('Invalid release audience')
        for field in ('groups','tickers'):
            if (not isinstance(audience[field],list) or len(audience[field]) > 100 or
                    not all(isinstance(v,str) and re.fullmatch(r'[A-Za-z0-9._-]{1,80}',v) for v in audience[field])):
                raise ValueError('Invalid release audience')
        if item['status'] == 'published':
            if (not text(item.get('evidence_url'),250) or not re.fullmatch(
                    r'https://github.com/Geochelone666/jsosif-ai-pipeline-demo/actions/runs/[0-9]+', item['evidence_url'])):
                raise ValueError('Published releases require reviewed deployment evidence')
            if instant(item.get('verified_at')) < instant(item.get('deployed_at')):
                raise ValueError('Release verification precedes deployment')
    return payload['releases']


def published(releases, now):
    return sorted((r for r in releases if r['status'] == 'published' and
                   instant(r['verified_at']) <= now), key=lambda r: (instant(r['verified_at']),r['id']), reverse=True)


def recipient_key(member_id):
    return hashlib.sha256(('release-announcements:' + member_id).encode()).hexdigest()


def select(releases, member, tickers, ledger, now):
    recipient = recipient_key(member['id'])
    seen = {release for record in ledger.values()
            if record.get('announcement_recipient') == recipient and
            record.get('status') in ('accepted','sending','unknown')
            for release in record.get('announcements',[])}
    result = []
    for release in published(releases,now):
        if release['id'] in seen or release['kind'] == 'maintenance':
            continue
        target = release['audience']
        if (not target['groups'] and not target['tickers'] or
                set(target['groups']) & set(member.get('groups',[])) or set(target['tickers']) & set(tickers)):
            result.append(release)
        if len(result) == 2:
            break
    return result


def page(releases, now=None):
    entries = published(releases, now or datetime.now(timezone.utc))
    articles = []
    for item in entries:
        articles.append('<article><p class="meta">' + escape(item['version']) + ' · ' +
                        escape(instant(item['verified_at']).date().isoformat()) + '</p><h2>' +
                        escape(item['title']) + '</h2>' + ''.join('<p>'+escape(s)+'</p>' for s in item['summary']) +
                        '<a href="'+escape(item['url'],quote=True)+'">Learn more</a></article>')
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>What's new · JSOSIF</title><style>
body{margin:0;background:#f5f6f2;color:#172921;font:17px/1.65 system-ui,sans-serif}main{max-width:850px;margin:0 auto;padding:32px 22px}
a{color:#176440}a:focus-visible{outline:3px solid #176440;outline-offset:4px}h1{font-size:clamp(2rem,6vw,3.5rem);line-height:1.15}article{background:white;padding:24px;margin:24px 0;border:1px solid #d3ded5;border-radius:12px;overflow-wrap:anywhere}.meta{color:#53685a}footer{margin-top:40px;color:#53685a}
</style><main><nav aria-label="Research navigation"><a href="./index.html">← Research workspace</a></nav>
<h1>What's new</h1><p>Published platform updates and changes to research reports.</p>''' + (
        ''.join(articles) if articles else '<p id="empty">No verified release announcements yet.</p>') + '''
<footer>Relevant major updates accompany your next eligible weekly digest. Research quality and delivery checks still apply.</footer></main></html>'''
