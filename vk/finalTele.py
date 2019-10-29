import telebot
bot = telebot.TeleBot('880936855:AAGRVoIs6uh3KuOkGk6T88WmwJKo9Wv9m00')

from telebot import apihelper

apihelper.proxy = {'https': 'socks5://127.0.0.1:9050'}
@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.username) + '!')
    print(message.chat.id)

bot.polling()