"""Browser acceptance using public reports and synthetic member data only."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright

import argparse
import json
import os
parser = argparse.ArgumentParser(description='Exercise the research and member pages in Chromium using synthetic members')
parser.add_argument('--site', type=Path, required=True)
parser.add_argument('--artifacts', type=Path, default=Path('review/browser'))
args = parser.parse_args()
root = args.artifacts.resolve()
root.mkdir(parents=True, exist_ok=True)
site = args.site.resolve()
expected = len(json.loads((site / 'index.json').read_text())['reports'])
if not expected:
    raise SystemExit('A nonempty site build is required')
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(site)))
thread=Thread(target=server.serve_forever,daemon=True);thread.start()
try:
  with sync_playwright() as p:
    browser=p.chromium.launch(executable_path=os.environ.get('BROWSER_EXECUTABLE') or None,headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1050})
    errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
    address='http://127.0.0.1:'+str(server.server_address[1])
    page.goto(address);page.wait_for_function("expected => document.querySelector('#stat-versions').textContent===String(expected)", arg=expected)
    assert page.locator('#history tr').count()==expected
    page.select_option('#ticker','CSCO')
    assert page.locator('#history tr').count()==1
    page.get_by_role('button',name='Read research').click()
    page.wait_for_selector('#detail-body table')
    assert page.locator('#detail-body tbody tr').count()>=10
    assert 'CSCO' in page.locator('#detail-title').inner_text()
    page.screenshot(path=str(root/'research-workspace.png'),full_page=True)
    page.get_by_role('button',name='Close details').click()
    page.get_by_role('button',name='Refresh now').click()
    page.wait_for_function("!document.querySelector('#refresh-now').disabled")
    assert page.locator('#ticker').input_value()=='CSCO'
    page.goto(address+'/members.html')
    csv='id,name,email,groups,tickers,enabled,timezone,send_weekday,send_time\nmember-001,"Example, Analyst",analyst@example.com,research,CSCO;JPM,yes,America/Toronto,2,09:00\nmember-002,Second Analyst,second@example.com,research,COST,no,America/Toronto,4,17:00\n'
    page.locator('#import').set_input_files({'name':'members.local.csv','mimeType':'text/csv','buffer':csv.encode()})
    page.wait_for_function("document.querySelector('#status').textContent.includes('2 members')")
    assert page.locator('#members tr').count()==2
    page.get_by_role('button',name='Validate configuration').click()
    assert '2 members' in page.locator('#status').inner_text()
    with page.expect_download() as pending:page.get_by_role('button',name='Download member CSV').click()
    download=pending.value;download.save_as(root/'browser-export.local.csv')
    assert 'CSCO;JPM' in (root/'browser-export.local.csv').read_text()
    with page.expect_download() as pending:page.get_by_role('button',name='Download private JSON configuration').click()
    pending.value.save_as(root/'browser-export.local.json')
    page.screenshot(path=str(root/'member-subscription-table.png'),full_page=True)
    # A rejected spreadsheet must leave the imported table intact.
    page.locator('#import').set_input_files({'name':'bad.csv','mimeType':'text/csv','buffer':b'id,name\n'})
    page.wait_for_selector('#status.error');assert page.locator('#members tr').count()==2
    page.set_viewport_size({'width':390,'height':844});page.goto(address)
    page.wait_for_function("expected => document.querySelector('#stat-versions').textContent===String(expected)", arg=expected)
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    page.screenshot(path=str(root/'research-workspace-mobile.png'),full_page=True)
    assert not errors,errors
    browser.close()
    print('Browser smoke checks passed: historical inspection, filters, refresh, CSV import/export, invalid-import preservation, and mobile layout; no JavaScript errors')
finally:server.shutdown();server.server_close()
