import telebot
import datetime
import time
from datetime import datetime

TOKEN = '6918500717:AAE44P-6z7gDuDEVH-CrDVXRe2xJVoYW53k'

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
        
        iraq_time = datetime.now()
        
        hours = divmod(iraq_time.hour, 12)[1]
        
        bio = f"\r{hours}:{iraq_time.strftime('%M')}"
        print(bio)
        
        print(t)
        
        bot.set_chat_description(message.chat.id, t+' '+bio+' [ 𝐋𝐎𝐕𝐄 🥀]')
        
        time.sleep(60)
     
     
bot.polling()
