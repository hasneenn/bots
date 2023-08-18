import telebot
import requests
from user_agent import generate_user_agent

token = "6340024725:AAHnsm9sdoCV95KNH-L6j4V8-dqZXOMHXJw"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def Welcome(message):
	name = message.from_user.first_name
	bot.reply_to(message,f'ارسل رابط الفيدو الذي تريد تحميلة \n @llxxx3' [{name}](tg://settings)',parse_mode="markdown")
	
@bot.message_handler(content_types=["text"])
def down(message):
     chat_id = message.chat.id
     brok = bot.reply_to(message,'حسناا انتظر')
     link = message.text
     if "https://www.instagram.com/reel/" not in link:
     	bot.delete_message(chat_id=chat_id, message_id=brok.message_id)
     	bot.reply_to(message,'✖️ تأكد من الرابط ')
     	return 
     else:
     	headers = {
     	'authority': 'api10.reelsdownloader.io',
     	'accept': '*/*',
     	'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
     	'origin': 'https://reelsdownloader.io',
     	'referer': 'https://reelsdownloader.io/',
     	'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
     	'sec-ch-ua-mobile': '?1',
     	'sec-ch-ua-platform': '"Android"',
     	'sec-fetch-dest': 'empty',
     	'sec-fetch-mode': 'cors',
     	'sec-fetch-site': 'same-site',
     	'url': link,
     	'user-agent': generate_user_agent() ,
     	}
     	response = requests.get('https://api10.reelsdownloader.io/allinone', headers=headers).json()["media"][0]["url"]
     	result = response
     	bot.delete_message(chat_id=chat_id, message_id=brok.message_id)
     	bot.send_video(chat_id, result, reply_to_message_id=message.message_id)


bot.infinity_polling()
