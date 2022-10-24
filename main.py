import telebot
from telebot import types

from config import API_KEY
from classfunc.cls import Accaunt, Premium
from classfunc.funcs import roll_dice, password_generator, generate_nickname

my_premium_account = Premium(amount=800, currency='UAH', discount=0.35)
my_account = Accaunt(amount=1000.00, currency='UAH')
her_account = Accaunt(amount=2000.00, currency='UAH')
roll = roll_dice()
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('wellcome.jpg', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Generate strong password')
    item2 = types.KeyboardButton("Generate nickname")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "I'll help you to generate strong password or unique nickname",
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def speak(message):
    if message.text == 'Generate strong password':
        bot.send_message(message.chat.id, password_generator(7, 7, 1))
    elif message.text == "Generate nickname":
        bot.send_message(message.chat.id, generate_nickname('names.txt', 'places.txt'))
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить')




if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
