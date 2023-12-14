import telebot
import datetime
import time
from datetime import datetime
import pytz

TOKEN = '6360026923:AAG7TPuytmsBl9OpW6LbY96KVKAxN8jyd9E'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا بك قوم برفع البوت مشرف في الگروب وارسل امر bio/ في الگروب')
@bot.message_handler(commands=['bio'])
def set_bio(message):
    
    bot.reply_to(message, 'تم تحديد ساعة البايو بنجاح.')
    while True:
        iraq_timezone = pytz.timezone("Asia/Baghdad")
        current_time =datetime.now(tz=iraq_timezone)
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
        bot.set_chat_description(message.chat.id, formatted_time)
        time.sleep(60)
     
     
bot.polling()
