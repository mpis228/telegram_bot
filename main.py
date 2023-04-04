import telebot
from telebot import types


import text
from tools import MustangMenu
from tools import SQL, time
from settings import API_KEY, CHAT

import random
# не забыть токет в общий кофиг закинуть потом
bot = telebot.TeleBot(API_KEY)
Mustang = MustangMenu()

"""так как это чисты говнокод как по мне и я обычно работаю без коментариев по возможноти буду писать коменты
тут есть кнопки которые без БД не как не работают не забывай"""

answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить
comment = dict()
prontochat = CHAT

@bot.message_handler(commands=['start'])
def send_welcome(message):
    Mustang.check(message)
    Mustang.menu(message)


@bot.message_handler()
def all_murk(message):
    # answer_id = 0  # создал пременую для того что бы хранить айди ответа и потом удалить

    if message.text == 'Меню' or message.text == '🔄Voltar ao menu':
        Mustang.menu(message)
    elif message.text == '❓Preguntas':
        Mustang.question(message)
    elif message.text == '👨‍💻Author':
        Mustang.auhtor(message)
    elif message.text == '🗣Feedback':
        Mustang.feedback(message)
    elif message.text == '📊Estatísticas':
        Mustang.statistic(message)
    elif message.text == '💶Ganhar dinheiro':
        Mustang.check(message)
        a = SQL.select_to_bd('user', message.chat.id)[0]['taps']
        if complid_taps(a, message):
                Mustang.preparation(message)


    #elif message.text == "Назад к вопросам":
    #    Mustang.question(message)
    elif message.text == 'Mais feedback ⏩':
        Mustang.feedback(message)
    elif message.text == "Portugal" or message.text == "Espanha" or message.text == 'Canadá':
        Mustang.preparation_two(message)
    elif message.text == '5100' or message.text == "8500" or message.text == '3200':
        Mustang.start(message)
    elif message.text == "▶️START":
        SQL.update_to_taps(message.chat.id, 1)
        Mustang.level_1(message)
    elif message.text == 'Sim, vá para "Tarefa 2"⏩':
        SQL.update_to_taps(message.chat.id, 2)
        Mustang.level_2(message)
    elif message.text == 'Sim, vá para "Tarefa 3"⏩':
        SQL.update_to_taps(message.chat.id, 3)
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
        SQL.update_to_taps(message.chat.id, 4)
        level_4(message)
    elif message.text == '📩Enviar texto':
        level_5(message, comment)


def level_4( message):
    bot.send_message(message.chat.id,
                     '☑️GERENTE, você completou com sucesso a "Tarefa 3"!',
                     reply_markup=types.ReplyKeyboardRemove())

    bot.send_message(message.chat.id, '📌Tarefa 4')
    markup = types.ReplyKeyboardMarkup(selective=False)
    comment = bot.send_message(message.chat.id, text.text_level4.substitute(), reply_markup=markup)
    bot.register_next_step_handler(comment, PRONTO)

def PRONTO(message):
    markup = types.ReplyKeyboardMarkup(True, True, row_width=1)
    com = types.InlineKeyboardButton("editar")
    next = types.KeyboardButton("📩Enviar texto")
    price = SQL.select_to_bd('user', message.chat.id)[0]['price']
    markup.add(next, com)

    save_text = text.text_pronto.substitute({"price": price, "text": message.text, "name": message.chat.username,
                                             'rand': random.randint(0, 10 * 7)})
    comment[message.chat.id] = save_text
    bot.send_message(message.chat.id, save_text, reply_markup=markup)

def fuck(message):
    time.sleep(10)
    price = SQL.select_to_bd('user', message.chat.id)[0]["price"]

    markup = types.InlineKeyboardMarkup(row_width=1)
    insta = types.InlineKeyboardButton('Instagram',
                                        url='https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
    telega = types.InlineKeyboardButton('✉️Telegram',
                                        url='https://api.whatsapp.com/send/?phone=351920499367&text=Ol%C3%A1%2C+Fernando.+Como+funciona%3F&type=phone_number&app_absent=0')
    whats = types.InlineKeyboardButton('📞WhatsApp',
                                        url='https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
    markup.add(insta, whats, telega)

    markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    menu = types.InlineKeyboardButton("🔄Voltar ao menu")
    markup_line.add(menu)

    bot.send_message(message.chat.id, '☑️*GERENTE*, seu solicitação é aprovado!', parse_mode="Markdown")

    bot.send_message(message.chat.id, '📌*Tarefa 5*', reply_markup=markup_line, parse_mode="Markdown")
    bot.send_message(message.chat.id, text.text_end.substitute({"price": price}), reply_markup=markup)
    SQL.update_to_taps(message.chat.id, 5)

def level_5(message, comment):
    price = SQL.select_to_bd('user', message.chat.id)[0]["price"]

    send_pronto = comment.pop(message.chat.id)
    bot.send_message(prontochat, send_pronto)

    mark = types.InlineKeyboardMarkup()
    feedback = types.InlineKeyboardButton('Feedback',
                                            url='https://mustangbot-pt.com/')
    mark.add(feedback)


    bot.send_message(message.chat.id, "⌛️*Seu solicitação está sendo verificado atualmente...*",
                         parse_mode="Markdown",
                         reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, fuck)
    bot.send_message(message.chat.id, text.text_level5.substitute({"price": price}), reply_markup=mark)

def complid_taps(a, message):
    if a == 1:
        return Mustang.level_1(message)
    elif a == 2:
        return Mustang.level_2(message)
    elif a == 3:
        return Mustang.level_3(message)
    elif a == 4:
        return level_4(message)
    elif a == 5:
        return fuck(message)
    else:
        return None


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
    if call.data in '012345':
        question(call)


def question(call):
    Mustang.call_quest(call)


bot.polling(none_stop=True)
