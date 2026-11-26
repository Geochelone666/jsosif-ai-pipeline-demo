"""Read-only browser checks against a built shared research view."""
import argparse,json,os
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright,expect
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--site',type=Path,required=True);parser.add_argument('--artifacts',type=Path,default=Path('review/shared-research'))
a=parser.parse_args();a.artifacts.mkdir(parents=True,exist_ok=True)
data=json.loads((a.site/'research-data.json').read_text())
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(a.site.resolve())))
Thread(target=server.serve_forever,daemon=True).start()
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=os.environ.get('BROWSER_EXECUTABLE') or None,headless=True,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto('http://127.0.0.1:'+str(server.server_address[1])+'/research.html')
  expect(page.locator('#status')).to_contain_text('No sources refreshed')
  assert page.locator('#team option').count()==8
  for team in data['teams']:
   page.select_option('#team',team['id'])
   assert page.locator('#sector-rows tr').count()==sum(s['ticker'] in team['tickers'] for s in data['stocks'])
  if len(data['stocks'])>=2:
   page.select_option('#stock-a',data['stocks'][0]['ticker']);page.select_option('#stock-b',data['stocks'][1]['ticker'])
   assert page.locator('#comparison tr').count()==2
   if data['stocks'][0]['metrics']:
    page.select_option('#metric',data['stocks'][0]['metrics'][0]['metric'])
    assert data['stocks'][0]['metrics'][0]['metric']==page.locator('#metric').input_value()
   expect(page.locator('#comparison a').first).to_have_attribute('href','./'+data['stocks'][0]['snapshot']['path'])
  page.screenshot(path=str(a.artifacts/'shared-research-desktop.png'),full_page=True)
  page.set_viewport_size({'width':390,'height':844})
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.screenshot(path=str(a.artifacts/'shared-research-mobile.png'),full_page=True)
  assert errors==[],errors
  browser.close();print('Shared research browser checks passed: eight sectors, coverage, stock/metric selection, provenance links and mobile layout')
finally:server.shutdown();server.server_close()
