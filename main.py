import telebot
import datetime
import time
from datetime import datetime

TOKEN = '6360026923:AAG7TPuytmsBl9OpW6LbY96KVKAxN8jyd9E'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا بك قوم برفع البوت مشرف في الگروب وارسل امر setbio/ في الگروب')
@bot.message_handler(commands=['bio'])
def set_bio(message):
    
    bot.reply_to(message, 'تم تحديد ساعة البايو بنجاح.')
    while True:
        now = datetime.now()
        mm = str(now.month)
        dd = str(now.day)
        yyyy = str(now.year)
        hour = str(divmod(now.hour, 12)[1])
        mi = str(now.minute)
        t=(mm+"/"+dd+"/" +yyyy)
        
        now = datetime.now()
        u = divmod(now.hour, 12)[1]
        bio = now.strftime(f"{u}:%M : [ HSO ]")
        print(bio)
        
        print(t)
        
        bot.set_chat_description(message.chat.id, t+' '+bio)
        time.sleep(60)
     
     
bot.polling()
