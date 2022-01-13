import telebot
import speedtest

bot = telebot.TeleBot("5084069411:AAHU7KeM8VPwlXxOY9EgG7aucN1M3_3bmDk")
st = speedtest.Speedtest()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, "Hai {}".format(name))

@bot.message_handler(commands='speedtest')
def speedtest(message):
    bot.reply_to(message, 'Tunggu sebentar ya lagi ngetes')
    st.get_best_server()
    ping = st.results.ping
    download = round(st.download() / 1000 / 1000, 1)
    upload = round(st.upload() / 1000 / 1000, 1)
    name = message.from_user.first_name
    bot.reply_to(message, '''Ping = {} ms\nDownload = {} Mbit/s\nUpload = {} Mbit/s'''.format(ping,download,upload))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()