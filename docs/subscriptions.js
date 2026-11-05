(() => {
'use strict';
const $=id=>document.getElementById(id);
let config, token=null, version=0, options, pending=null, timer, conflict=false, busy=false;
function status(message){$('status').textContent=message;}
function clear(){clearTimeout(timer);token=null;pending=null;version=0;options=null;conflict=false;$('preferences').reset();$('change-email').reset();$('code').value='';$('identity').textContent='';$('groups').replaceChildren();$('account').hidden=true;$('login').hidden=false;}
async function request(path,body,method='POST'){
 const headers={'apikey':config.publishable_key,'Content-Type':'application/json'};
 if(token)headers.Authorization='Bearer '+token;
 const response=await fetch(config.url+path,{method,headers,body:JSON.stringify(body),redirect:'error',cache:'no-store',credentials:'omit',referrerPolicy:'no-referrer'});
 if(!response.ok){const error=new Error('Request failed');error.status=response.status;throw error;}
 return response.status===204?null:response.json();
}
function failure(error){
 if(error.status===401){clear();status('Your session expired. Sign in again.');}
 else if(error.status===403){clear();status('Access denied. Check your code or ask the team to approve your verified account.');}
 else if(error.status===409){conflict=true;$('save').disabled=true;status('Settings changed elsewhere. Reload saved settings and review your changes before saving.');}
 else status('The request could not be completed. No success has been confirmed. Retry when ready.');
}
async function action(work){if(busy)return;busy=true;document.querySelectorAll('button').forEach(b=>b.disabled=true);try{await work();}catch(error){failure(error);}finally{busy=false;document.querySelectorAll('button').forEach(b=>b.disabled=false);$('save').disabled=conflict;}}
function groupControls(){
 $('groups').replaceChildren();
 for(const [id,group] of Object.entries(options.groups)){
  const label=document.createElement('label'),input=document.createElement('input');input.type='checkbox';input.value=id;input.name='group';label.append(input,document.createTextNode(group.name||id));$('groups').append(label);
 }
}
async function reload(){
 options=await request('/rest/v1/rpc/subscription_options',{});
 const saved=await request('/rest/v1/rpc/get_my_subscription',{});
 groupControls();const p=saved?.preferences||{};version=saved?.version||0;pending=null;conflict=false;
 $('name').value=p.name||'';$('tickers').value=(p.tickers||[]).join(', ');$('enabled').checked=p.enabled===true;
 $('weekday').value=String(p.send_weekday??1);$('time').value=p.send_time||'09:00';$('timezone').value=p.timezone||Intl.DateTimeFormat().resolvedOptions().timeZone||'America/Toronto';$('start').value=p.delivery_start_date||'';
 for(const input of $('groups').querySelectorAll('input'))input.checked=(p.groups||[]).includes(input.value);
 for(const [id,key] of [['sector','sector_brief'],['macro','macro_overview'],['news','news_catalysts']])$(id).checked=p.content_preferences?.[key]===true;
 $('version').textContent='Settings version: '+version+(saved?.updated_at?' · Updated: '+saved.updated_at:'');
 $('account').hidden=false;$('login').hidden=true;status(saved?'Saved settings loaded.':'Team access confirmed. Choose your preferences to create a subscription.');
}
$('request-code').addEventListener('submit',event=>{event.preventDefault();action(async()=>{await request('/auth/v1/otp',{email:$('email').value.trim(),create_user:true});$('verify-code').hidden=false;status('If the address is eligible, a sign-in code has been requested. Check your email.');});});
$('verify-code').addEventListener('submit',event=>{event.preventDefault();action(async()=>{
 const session=await request('/auth/v1/verify',{email:$('email').value.trim(),token:$('code').value.trim(),type:'email'});
 if(typeof session.access_token!=='string'||!Number.isFinite(session.expires_in)||session.expires_in<=0)throw Error('Invalid session');
 token=session.access_token;clearTimeout(timer);timer=setTimeout(()=>{clear();status('Your session expired. Sign in again.');},Math.min(session.expires_in,3600)*1000);
 $('identity').textContent='Signed in: '+(session.user?.email||$('email').value.trim());$('code').value='';await reload();
});});
$('reload').addEventListener('click',()=>action(reload));
$('preferences').addEventListener('submit',event=>{event.preventDefault();action(async()=>{
 const tickers=[...new Set($('tickers').value.toUpperCase().split(/[\s,;]+/).filter(Boolean))];
 if(tickers.some(t=>!options.tickers.includes(t))){status('One or more stocks are not active. Ask the team to review them before subscribing.');return;}
 const groups=[...$('groups').querySelectorAll('input:checked')].map(input=>input.value);
 if(!groups.length&&!tickers.length){status('Select a research group or at least one active stock.');return;}
 const preferences={name:$('name').value.trim(),enabled:$('enabled').checked,timezone:$('timezone').value.trim(),send_weekday:Number($('weekday').value),send_time:$('time').value,groups,tickers,content_preferences:{sector_brief:$('sector').checked,macro_overview:$('macro').checked,news_catalysts:$('news').checked}};
 if($('start').value)preferences.delivery_start_date=$('start').value;
 const fingerprint=JSON.stringify({preferences,version});
 if(pending?.fingerprint!==fingerprint)pending={fingerprint,body:{p_preferences:preferences,p_expected_version:version,p_request_id:crypto.randomUUID()}};
 const result=await request('/rest/v1/rpc/save_my_subscription',pending.body);
 if(!Number.isSafeInteger(result.version)||result.version<=version)throw Error('Invalid save response');
 version=result.version;pending=null;$('version').textContent='Settings version: '+version+' · Updated: '+result.updated_at;status('Preferences saved. Future eligible deliveries will use the effective settings.');
});});
$('change-email').addEventListener('submit',event=>{event.preventDefault();action(async()=>{await request('/auth/v1/user',{email:$('new-email').value.trim()},'PUT');$('new-email').value='';status('Email change requested. Complete the required confirmations, then sign in with the verified address.');});});
$('signout').addEventListener('click',()=>action(async()=>{try{await request('/auth/v1/logout',{});}finally{clear();status('Signed out on this page.');}}));
(async()=>{try{
 const response=await fetch('./portal-config.json',{cache:'no-store',credentials:'omit',redirect:'error'});if(!response.ok)throw Error('No configuration');config=await response.json();
 if(config.enabled!==true){status('The subscription portal is not yet enabled. Contact the team for subscription changes.');return;}
 if(!/^https:\/\/[a-z0-9-]+\.supabase\.co$/.test(config.url)||!/^sb_publishable_[A-Za-z0-9_-]+$/.test(config.publishable_key))throw Error('Invalid public configuration');
 $('login').hidden=false;status('Sign in to access your team subscriptions.');
}catch(error){status('The subscription portal is unavailable. Contact the team for subscription changes.');}})();
})();
