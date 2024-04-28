import time
import telebot

token = '6526048505:AAEbiU1bGv63IDjLpSGfoKtGbHIXeyMVBbE'
bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'Как твои делa? Чем я могу помочь?')

@bot.message_handler(commands= ['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)

@bot.message_handler(commands= ['timer'])
@bot.message_handler(content_types= 'text')
def reserve_text(message):
    if 'плохой'in message.text.lower():
        bot.reply_to(message,  'Текст содержит слово плохой')
    text = message.text[::-1]
    bot.reply_to(message, text)

bot.polling()