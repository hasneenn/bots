import requests
from telebot import types
import telebot
 

token = '6782944535:AAFTA4kXNuK4y9g4HS9zIzGZauBp7FC1zRc'
bot = telebot.TeleBot(token)
bot.set_my_commands([telebot.types.BotCommand("/start", "🤖 Start the bot"),telebot.types.BotCommand("/help", "🆘 How to use the bot")])
@bot.message_handler(commands=['help'])
def send_hello(message):
    nn = '''
    En 🚩
    
Developer : Hasneen Al Ali

help the message : @PY_87

My channel : @llxxx3
_ _ _ _ _ _ _  _ _  _ _ _ _ _  _ _  _ _ _
ar 🇮🇶

المطور : حسو ال علي

للمساعده راسلني : @PY_87

قناتي المقلوبه : @llxxx3

طريقه تشغيل البوت ركز وياي خوش
اول مدوس /start شراح يطلع

username:password:target

هيج صح يعني هاي شلون ركز
تكتب اليوزر وراهه نقطتين : شرط ذني
وراه الباسورد هم نقطتين وراه يوزر الضحيه
كمثال 

user:pass:target

يعني اول شي يوزري وباسورد حسابي الي ابلغ بي نوب يوزر الضحيه الي اريد اطيره

ملاحضه هامه
اذا جان عندك غلط مراح يرد لبوت عليك ونته تاكد من لمعلومات قبل ارسالها لتجنب لحضر من لمطور 
وسيوووو
'''
    chat_id = message.chat.id
    bot.send_message(chat_id, nn)
    
@bot.message_handler(commands=['start'])
def start(message):
	my = types.InlineKeyboardButton(text='تابع لمزيد ع قناتي',url="t.me/llxxx3")
	xx = types.InlineKeyboardMarkup()
	xx.add(my)
	bot.send_message(message.chat.id,'\nusername:password:target\n\n/help',reply_markup=xx)
	

@bot.message_handler(func=lambda m:True)
def r(message):
	ni=1
	my = types.InlineKeyboardButton(text='تابع لمزيد ع قناتي',url="t.me/llxxx3")
	xi = types.InlineKeyboardMarkup()
	xi.add(my)
	try:
		user = message.text.split(':')[0]
		pasw = message.text.split(':')[1]
		target = message.text.split(':')[2]
		url = f"https://www.instagram.com/{target}"
		req = requests.get(url).text
		
		iid = req.split('props":{"id":"')[1].split('"')[0]
	
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
		
		he = {
		        "accept": "*/*",
		        "accept-encoding": "gzip, deflate, br",
		        "accept-language": "en-US,en;q=0.9",
		        "content-length": "385",
		        "content-type": "application/x-www-form-urlencoded",
		        "cookie": "csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08",
		        "origin": "https://www.instagram.com",
		        "referer": "https://www.instagram.com/accounts/login/",
		        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		        "sec-ch-ua-mobile": "?0",
		        "sec-fetch-dest": "empty",
		        "sec-fetch-mode": "cors",
		        "sec-fetch-site": "same-origin",
		        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
		        "x-asbd-id": "437806",
		        "x-csrftoken": "Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC",
		        "x-ig-app-id": "936619743392459",
		        "x-ig-www-claim": "0",
		        "x-instagram-ajax": "56f3c2d2a823",
		        "x-requested-with": "XMLHttpRequest"}
		    
		data = {
		"username": f"{user}",
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{pasw}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}
		req1=requests.post(url, headers=he, data=data)
		if '"authenticated":true' in req1.text:
			csrf=req1.cookies['csrftoken']
			sid=req1.cookies['sessionid']
			userid=req1.json()['userId']
			n=0
			for i in range(10):
				
			
				url='https://www.instagram.com/reports/web/get_frx_prompt/'
			
				head={
				'Host': 'www.instagram.com',
				'Cookie': f'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken={csrf}; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1; ds_user_id={userid}; sessionid={sid}; shbid="19399\05448526341466\0541657548493:01f765eb2fb0f52402149d7667ceb064bc56c1a422fc410f2a66fe68999c5cddaeb410b2"; shbts="1626012493\05448526341466\0541657548493:01f7e1c3ad7a57e6f558f05d8c9e6c00121a3a308e818c4c27918b95f7c09e38daba9815"; rur="VLL\05448526341466\0541657639760:01f790b1d824dd12c35339c0adf06665245ba76f59fd9f49557f1d7e258a635e96aa9b9',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
				'Accept': '*/*',
				'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
				'Accept-Encoding': 'gzip, deflate',
				'X-Csrftoken': f'{csrf}',
				'X-Instagram-Ajax': '595724a46b58',
				'X-Ig-App-Id': '936619743392459',
				'X-Asbd-Id': '437806',
				'X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k',
				'Content-Type': 'application/x-www-form-urlencoded',
				'X-Requested-With': 'XMLHttpRequest',
				'Content-Length': '3131',
				'Origin': 'https://www.instagram.com',
				'Referer': f'https://www.instagram.com/{target}/',
				'Te': 'trailers',
				'Connection': 'close'}
			
				data = f'entry_point=1&location=2&object_type=5&object_id={iid}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_self_injury_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22{sid}%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_self_injury_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{iid}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841448643985792%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841400668013122%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrTVqcbpAhgMNS4xNjMuMTE4LjgyGE5Nb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjo4OS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzg5LjAYBWVuX1VTHBggZjZjZjZhMzUzYzlmNDFiYWMyZjcxY2JkYzU0MGQyNjMYIDliMWEzMDMxNzllYTJhNjFiN2JjYjI1MzBmNWQ0MDU3GCBkMGM4NDY2NTgyOTIzODgyODgyNThiNjI0M2M3MDlhMhgAFfaGAwA8LBgcWU5JYTRRQUxBQUdvZUVTRlA4YXhZOU5mQzl0MxbQ%2B8fLxl4AHBUUKwAAIjw5FQAZFQA5FQAAGCAyYjljMjZlOWQzODk0NTE5ODAxYjU3OGZlYTdlOGNmMBUCERIYDzkzNjYxOTc0MzM5MjQ1ORwWoNT6wKXwtj8YQGYyOGViNTc3YzYwYmRjMWI0MDg1MzA5NWIzNDhmNWY0ODQzNWE4MmQzOGU5ZWRkZTc0NzMxNGI4ZjdjNmE4YzYAHBUEABIoIGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vcmFfMjMvGA5YTUxIdHRwUmVxdWVzdAAWgIagi%5C%5C%5C%5C%5C%5C%5C%2F%2BssT8oHC9yZXBvcnRzL3dlYi9nZXRfZnJ4X3Byb21wdC8WLBaA5sWPDAA%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22{sid}%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&action_type=2&frx_prompt_request_type=4'
			
				req=requests.post(url,headers=head,data=data).text
				if "ok" in req:
					n+=1
					bot.reply_to(message,f'\nGood target {user}  [{n}]\n\nDeve : @PY_87',reply_markup=xi)
				else:
					bot.reply_to(message,'Bad username or password or target \n\nhelp /help')

	except IndexError:
		bot.reply_to(message,'Bad username or password or target \n\nhelp /help')
		start(message)

		

print('It was completed ')
bot.infinity_polling()

