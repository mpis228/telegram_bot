import telebot
from telebot import types

import text
from tools import MustangMenu
from tools import SQL

import random
# не забыть токет в общий кофиг закинуть потом
bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
Mustang = MustangMenu()

"""так как это чисты говнокод как по мне и я обычно работаю без коментариев по возможноти буду писать коменты
тут есть кнопки которые без БД не как не работают не забывай"""

answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить
comment = dict()
prontochat = -892313553

@bot.message_handler(commands=['start'])
def send_welcome(message):
    Mustang.check(message)
    Mustang.menu(message)


@bot.message_handler()
def all_murk(message):
    # answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить

    if message.text == 'Меню' or message.text == '🔄Voltar ao menu':
        Mustang.menu(message)
    elif message.text == 'Вопросы':
        Mustang.question(message)
    elif message.text == 'Автор':
        Mustang.auhtor(message)
    elif message.text == 'Отзывы':
        Mustang.feedback(message)
    elif message.text == 'Статистика':
        Mustang.statistic(message)
    elif message.text == 'Заработать':
        Mustang.preparation(message)
    elif message.text == "Назад к вопросам":
        Mustang.question(message)
    elif message.text == 'More':
        Mustang.feedback(message)
    elif message.text == "Польша" or message.text == "Україна":
        Mustang.preparation_two(message)
    elif message.text == '5100' or message.text == "8500" or message.text == '3200':
        Mustang.start(message)
    elif message.text == "Старт":
        Mustang.level_1(message)
    elif message.text == 'второй этап':
        Mustang.level_2(message)
    elif message.text == 'третий этап':
        Mustang.level_3(message)
    elif message.text == 'Não, eu quero permanecer incógnito' or message.text == 'Sim, vou deixar uma feedback':
        mark = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        level = types.InlineKeyboardButton('Sim, vá para "Tarefa 4"⏩')
        mark.add(level)
        price = SQL.select_to_bd('user', message.chat.id)[0]['price']
        bot.send_message(message.chat.id, text.text_level3_after.substitute({'price': price}), reply_markup= mark)
    elif message.text == 'editar':
        markup = types.ReplyKeyboardMarkup(selective=False)
        commet = bot.send_message(message.chat.id, '....' * 5, reply_markup=markup)
        bot.register_next_step_handler(commet, PRONTO)
    elif message.text == 'Sim, vá para "Tarefa 4"⏩':
        level_4(message)
    elif message.text == '📩Enviar texto':
        Mustang.level_5(message, comment)


def level_4( message):
    bot.send_message(message.chat.id, "поздравляю вы прошли 3 этап")
    markup = types.ReplyKeyboardMarkup(selective=False)
    comment = bot.send_message(message.chat.id, text.text_level4.substitute(), reply_markup=markup)
    print("dasdad")
    bot.register_next_step_handler(comment, PRONTO)

def PRONTO(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    com = types.InlineKeyboardButton("editar")
    next = types.KeyboardButton("📩Enviar texto")
    price = SQL.select_to_bd('user', message.chat.id)[0]['price']
    markup.add(next, com)
    save_text = text.text_pronto.substitute({"price": price, "text": message.text, "name": message.chat.username,
                                             'rand': random.randint(0, 10 * 7)})
    comment[message.chat.id] = save_text
    bot.send_message(message.chat.id, save_text, reply_markup=markup)


@bot.message_handler()
def start_work(message):
    if message.text == 'заработать':
        markup = types.InlineKeyboardMarkup(row_width=1)
        inst_com = types.InlineKeyboardButton(f"Instagram",
                                              'https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
        markup.add(inst_com)
        bot.send_message(message.chat.id, "посмотрите его видео", reply_markup=markup)


@bot.callback_query_handler(func=lambda c: True)
def main(call):
    if call.data in '0123':
        question(call)


def question(call):
    Mustang.call_quest(call)


bot.polling(none_stop=True)
