from telebot import types
import telebot

bot = telebot.TeleBot('6798963393:AAFNWUhxvdvzZc9NzTpaDACGbQVxr00ESj0')


def webAppKeyboard(): 
   keyboard = types.ReplyKeyboardMarkup(row_width=1) 
   
   webAppGame = types.WebAppInfo("https://m.youtube.com") 
   
   two_butt = types.KeyboardButton(text="اضغط هنا لبدء تشغيل اليوتيوب ", web_app=webAppGame) 
   
   keyboard.add(two_butt) 

   return keyboard

@bot.message_handler(commands=['start'])
def start_fun(message):

   bot.send_message( message.chat.id, '''*
اهلا بك في بوت مشاهدة اليوتيوب
داخل التليجرام عل اضعف نت

مطور البوت حسو ال علي @PY_87

اضغط 👇👇عل هذا الزر الذي في الاسفل
*
''', parse_mode="Markdown", reply_markup=webAppKeyboard())


print('run')
bot.infinity_polling()
