import telebot
from telebot import types

from tools import MustangMenu

# не забыть токет в общий кофиг закинуть потом
bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
Mustang = MustangMenu()

"""так как это чисты говнокод как по мне и я обычно работаю без коментариев по возможноти буду писать коменты
тут есть кнопки которые без БД не как не работают не забывай"""

answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить


@bot.message_handler(commands=['start'])
def send_welcome(message):
    Mustang.menu(message)


@bot.message_handler()
def all_murk(message):
    # answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить

    if message.text == 'Меню':
        Mustang.menu(message)
    elif message.text == 'Вопросы':
        Mustang.question(message)
    elif message.text == 'Автор':
        Mustang.auhtor(message)
    elif message.text == 'Отзывы':
        Mustang.reviews(message)
    elif message.text == 'Статистика':
        Mustang.statistic(message)
    elif message.text == 'заработать':
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton("Меню")
        markup_line.add(menu)
        bot.send_message(message.chat.id, '📌Вы в одном шаге заработку', reply_markup=markup_line)

        markup = types.InlineKeyboardMarkup(row_width=1)
        inst_com = types.InlineKeyboardButton(f"Instagram",
                                              'https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
        markup.add(inst_com)
        bot.send_message(message.chat.id, "посмотрите его видео", reply_markup=markup)
    elif message.text == "Назад к вопросам":
        Mustang.back_to_question(message)


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
        print("работает")
        question(call)


def question(call):
    Mustang.call_quest(call)


def work(call):
    if call.message:
        pass


bot.polling(none_stop=True)
