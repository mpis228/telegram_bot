import time

import telebot
from telebot import types
from SQL_load import LoadMySQL
from string import Template
import text

bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
SQL = LoadMySQL()
#prontochat = -892313553

"""мини дайджест от Михаила у меня тут в мустанг меню разработано логику кнопки с вопросами только тут же статистика
 и все остальное, подключить осталось нормально БД и множно додлывать кнопки я пытался сделать отдельно мутод который 
 удаляет сообщения но он чет не работает как надо """


class MustangMenu():
    def __init__(self):
        self.answer_id = 0

    def check(self, message):
        if SQL.select_to_bd("user", message.chat.id):
            pass
        else:
            SQL.insert_user(message.chat.id)

    def question(self, message):
        self.answer_id = 0
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton("Меню")
        # back = types.KeyboardButton("Назад к вопросам")
        markup_line.add(menu)
        bot.send_message(message.chat.id, '📌Вы на вкладке вопросы', reply_markup=markup_line)

        quest = SQL.select_to_bd("quest")
        markup = types.InlineKeyboardMarkup(row_width=1)

        question_1 = types.InlineKeyboardButton(quest[0]['question'], callback_data='0')
        question_2 = types.InlineKeyboardButton(quest[1]['question'], callback_data='1')
        question_3 = types.InlineKeyboardButton(quest[2]['question'], callback_data='2')
        question_4 = types.InlineKeyboardButton(quest[3]['question'], callback_data='3')

        markup.add(question_1, question_2, question_3, question_4)
        bot.send_message(message.chat.id, 'часто задаваемые вопросы', reply_markup=markup)

    # принимает на себя сообщения и отправляет обратно сообщения с кнопками
    def menu(self, message):

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        com_recall = types.KeyboardButton("Отзывы")
        com_questions = types.KeyboardButton("Вопросы")
        com_auhtor = types.KeyboardButton("Автор")
        com_statistic = types.KeyboardButton("Статистика")
        com_earn = types.KeyboardButton("Заработать")
        markup.add(com_recall, com_questions, com_auhtor, com_statistic, com_earn)

        name = message.chat.first_name
        bot.send_message(message.chat.id, f"здрасвуйте {name} Вас приветсвует мустангру бот ", reply_markup=markup)
        # реализация кнопки автора

    @staticmethod
    def auhtor(message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        markup_line.add(menu)

        bot.send_message(message.chat.id, '📌Вы на вкладке автора', reply_markup=markup_line)

        markup = types.InlineKeyboardMarkup(row_width=2)
        inst_com = types.InlineKeyboardButton(f"Instagram", 'https://www.instagram.com/joebiden/')
        tele_com = types.InlineKeyboardButton(f"Telegram", 'https://www.instagram.com/joebiden/')
        info_com = types.InlineKeyboardButton(f"info", 'https://www.instagram.com/joebiden/')
        markup.add(info_com, inst_com, tele_com)

        bot.send_message(message.chat.id, 'тут будет про автора, фото', reply_markup=markup)

    # риализует работу кнопки отзывы из бд берет сылки на фото главное что бы было в jpg это можно поменять в самом
    @staticmethod
    def feedback(message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        more = types.KeyboardButton('More')
        markup_line.add(menu, more)
        data = SQL.select_to_bd('feedback')

        bot.send_message(message.chat.id, '📌Вы на вкладке отзывы', reply_markup=markup_line)
        # принимает только определеный формат можно убрать '.jpg' если ввести правильно путь в БД
        file = open(data[0]['link_imeges'] + '.jpg', 'rb')

        bot.send_photo(message.chat.id, file, f'[интсаграм человека]({data[0]["link_insta"]})', parse_mode='Markdown')
        bot.send_message(message.chat.id, data[0]["Coment"])

    # Реализация кнопки статистика

    def statistic(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        markup_line.add(menu)

        bot.send_message(message.chat.id, '📌Вы на вкладке статистика', reply_markup=markup_line)

        send = Template('Пользователи: 5987\n'
                        'Заработано пользователями: 714 654 евро\n'
                        'Приглашенных друзей: 2109\n'
                        'Выполнено квестов: 29 935')

        bot.send_message(message.chat.id, send.substitute())
    # удаляет сообщения ответа что бы не мешало

    def back_to_question(self, message):
        if self.answer_id != 0:
            print(self.answer_id)
            bot.delete_message(message.chat.id, self.answer_id + 1)
        self.question(message)

    # реализует кнопки вопрос ответ ответы берет с БД
    def call_quest(self, call):
        if call.message:
            markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            menu = types.KeyboardButton("Меню")
            back = types.KeyboardButton("Назад к вопросам")
            markup_line.add(back, menu)
            self.answer_id = call.message.id
            self.del_coment(call)
            for i in range(4):
                if call.data == str(i):
                    info = SQL.select_to_bd('quest')[i]['answer']
                    bot.send_message(call.message.chat.id, info, reply_markup=markup_line)

    def del_coment(self, call):
        bot.delete_message(call.message.chat.id, self.answer_id)
        bot.delete_message(call.message.chat.id, self.answer_id - 1)
        bot.delete_message(call.message.chat.id, self.answer_id - 2)

    def preparation(self, message):
        #реестрация пользователя

        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        com_ua = types.InlineKeyboardButton('Україна')
        com_br = types.InlineKeyboardButton('Польша')
        markup_line.add(com_ua, com_br)
        text = Template("Binance являеться официальним спонсором и партнером проекта, компания гарантирует вам прибыль")
        file = open('images\defolt.jpg', 'rb')
        bot.send_photo(message.chat.id, file, text.substitute())
        bot.send_message(message.chat.id, "выберите страну проживания", reply_markup=markup_line)

    def preparation_two(self, message):
        if SQL.select_to_bd("income", message.chat.id)[0]['price'] > 0:
            self.level_1(message)
        else:
            markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            price_low = types.InlineKeyboardButton("3200")
            price_medium = types.InlineKeyboardButton("5100")
            price_high = types.InlineKeyboardButton("8500")
            menu = types.InlineKeyboardButton("Меню")
            markup_line.add(price_low, price_medium, price_high, menu)
            file = open("images/defolt.jpg", 'rb')
            text = 'фернандо являеться официальным партнером Форд и Бинанс'

            bot.send_photo(message.chat.id, file, text)
            bot.send_message(message.chat.id, 'выберите свой выиграш', reply_markup=markup_line)

    def start(self, message):
        SQL.update_to_user(message.chat.id, message.text)
        murkup_start = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        start = types.InlineKeyboardButton("Старт")
        murkup_start.add(start)

        text = Template("fdsafafd")

        bot.send_message(message.chat.id, "📖 подбераем задания... ", reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, text.substitute(),  reply_markup=murkup_start)

    def level_1(self, message):
        price = SQL.select_to_bd("income", message.chat.id)[0]['price']
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        level = types.KeyboardButton("второй этап")
        markup_line.add(level)

        if SQL.select_to_bd("income", message.chat.id)[0]['level1']:
            text = Template("осталось еще 5 этапов для получения 💵 $price и можете вывести"
                            "на банковский счет\n"
                            "я заинетересован в том что после выиграша вы перечислите мне 15%,"
                            " а остальное себе для перехода"
                            " к певому заданию нажмите страт")
            bot.send_message(message.chat.id, text.substitute({'price': price}), reply_markup=markup_line)

        else:
            bot.send_message(message.chat.id, "📖 подбераем задания... ", reply_markup=types.ReplyKeyboardRemove())

            price = SQL.select_to_bd("income", message.chat.id)[0]['price']
            markup = types.InlineKeyboardMarkup(row_width=1)
            inst_com = types.InlineKeyboardButton(f"In stagram",
                                                  'https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
            markup.add(inst_com)

            #bot.send_message(message.chat.id, "📖 подбераем задания... б", reply_markup=bot.)
            bot.send_message(message.chat.id, f"посмотрите его сторис что бы заработать {price}", reply_markup=markup)
            time.sleep(1)
            bot.send_message(message.chat.id, "поздравляю вы прошли первый этап", reply_markup=markup_line)
            SQL.update_to_level("level1", message.chat.id)

    def level_2(self, message):
        if SQL.select_to_bd("income", message.chat.id)[0]['level2']:
            bot.send_message(message.chat.id, 'текст')
            self.level_3(message)
        else:
            price = SQL.select_to_bd('income', message.chat.id)[0]['price']
            markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            level = types.KeyboardButton("третий этап")
            markup_line.add(level)


            bot.send_message(message.chat.id, text.text_level2.substitute({"price": price}))
            time.sleep(15)
            bot.send_message(message.chat.id, "поздравляю вы прошли второй этап", reply_markup=markup_line)
            SQL.update_to_level("level2", message.chat.id)

    def level_3(self, message):
        if SQL.select_to_bd("income", message.chat.id)[0]['level3']:
            self.level_4(message)
        else:
            price = SQL.select_to_bd('income', message.chat.id)[0]['price']
            markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            yes = types.InlineKeyboardButton('Sim, vou deixar uma feedback')
            no = types.InlineKeyboardButton('Não, eu quero permanecer incógnito')
            markup_line.add(yes, no)

            bot.send_message(message.chat.id, f"посмотрите его сторис для заработка {price}")
            time.sleep(2)
            bot.send_message(message.chat.id, "поздравляю вы прошли третий этап", reply_markup=markup_line)
            SQL.update_to_level("level3", message.chat.id)



    def level_4(self, message):
        if SQL.select_to_bd("income", message.chat.id)[0]['level4']:
            self.level_4(message)
        else:
            markup = types.ReplyKeyboardMarkup(selective=False)
            commet = bot.send_message(message.chat.id, text.text_level4.substitute())
            bot.send_message(message.chat.id, "поздравляю вы прошли 3 этап", reply_markup=markup)
            SQL.update_to_level("level4", message.chat.id)
            bot.register_next_step_handler(commet, self.PRONTO)

    def PRONTO(self, message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        price = SQL.select_to_bd('income', message.chat.id)[0]['price']
        reply = types.KeyboardButton("level4")
        markup.add(reply)
        save_text = text.text_pronto.substitute({"price": price, "text": message.text, "name": message.chat.username})

        bot.send_message(message.chat.id, text.text_pronto.substitute(), reply_markup=markup)