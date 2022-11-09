import telebot
from telebot import types
from string import Template
import time
from SQL_load import load_to_bd

# не забыть токет в общий кофиг закинуть потом
bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')


@bot.message_handler(commands=['start'])
def send_welcome(message):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    com_recall = types.KeyboardButton("about")
    com_questions = types.KeyboardButton("questions")
    com_auhtor = types.KeyboardButton("auhtor")
    com_statistic = types.KeyboardButton("statistic")
    com_earn = types.KeyboardButton("earn")
    markup.add(com_recall, com_questions, com_auhtor, com_statistic, com_earn)
    bot.send_message(message.chat.id, "Вас приветсвует мустангру бот ", reply_markup=markup)

@bot.message_handler()
def questions(message):
    markup = types.InlineKeyboardMarkup()
    question_who = types.InlineKeyboardButton(f"первый вопрос", callback_data='1')
    markup.add(question_who)
    bot.send_message(message.chat.id, 'never', reply_markup=markup)


@bot.callback_query_handler(func = lambda c: True)
def question(call):
    if call.message:
        if call.data == '1':
            info = load_to_bd()['answer']
            bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
