import telebot

bot = telebot.TeleBot("5928422327:AAGSlHRWHSf3kr4j4oTWuIJG_AN8reOegbo")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Merhaba!")

bot.polling()
