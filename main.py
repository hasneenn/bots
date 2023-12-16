from pytube import YouTube
from telebot import types
import telebot
import requests, random
import os

token ='6789262419:AAFdsXvr0ijFWx3TLnkkj1RDhNHVCAl0DfM'

bot = telebot.TeleBot(token)

bot.set_my_commands([telebot.types.BotCommand("/start", " 🤖 𝗦𝗧𝗔𝗥𝗧 𝗕𝗢𝗧 ")])

@bot.message_handler(commands=['start'])
def start_fun(message):
    id1 = str(message.from_user.id)
    
    
    bot.reply_to(message,'*ارسل اسم الفلم او الاغنية او اي شيء للبحث في اليوتيوب*',parse_mode='markdown')

@bot.message_handler(func=lambda message: True)
def search_fun(message):
    text = message.text
    
    rr = f"https://www.youtube.com/results?search_query={text}"
    u = requests.get(rr).text
    
    r = u.split('/watch?v=')[1].split('"')[0]
    mo = f"https://www.youtube.com/watch?v={r}"
    uo = mo.split("u0")[0]
    video_url = uo
    yt = YouTube(video_url)
    video = yt.streams.first()
    video.download()

    
    filem = video.default_filename
     
    ki='wertuiosazxcvn'
    
    uo = str(''.join(random.choice(ki)for ii in range(7)))
       
    namenew = f'{uo}.mp4'
    os.rename(filem, namenew)
    bot.send_video(message.chat.id,video=open(f'{uo}.mp4','rb'),caption='*Done Download\nDev : @llxxx3*',parse_mode='markdown')
    
    bot.send_audio(message.chat.id,audio=open(f'{uo}.mp4','rb'),caption='*Done Download\nDev : @llxxx3*',parse_mode='markdown')
    
    os.remove(f'{uo}.mp4')



def main():  
    while True:
        
        try:
            
            bot.infinity_polling()
            
        except:
            import os
            os.system('clear')
            main()
        
        main()
        
    main()
    
main()
