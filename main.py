import telebot
from telebot import types

from tools import MustangMenu
from tools import SQL
# не забыть токет в общий кофиг закинуть потом
bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
Mustang = MustangMenu()

"""так как это чисты говнокод как по мне и я обычно работаю без коментариев по возможноти буду писать коменты
тут есть кнопки которые без БД не как не работают не забывай"""

answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить


@bot.message_handler(commands=['start'])
def send_welcome(message):
    Mustang.check(message)
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
        Mustang.feedback(message)
    elif message.text == 'Статистика':
        Mustang.statistic(message)
    elif message.text == 'Заработать':
        Mustang.preparation(message)
    elif message.text == "Назад к вопросам":
        Mustang.back_to_question(message)
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
        Mustang.PRONTO(message)
    elif message.text == 'level4':
        Mustang.level_4(message)



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
