import time

import telebot
from telebot import types
from SQL_load import LoadMySQL
from string import Template

bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
SQL = LoadMySQL()

"""мини дайджест от Михаила у меня тут в мустанг меню разработано логику кнопки с вопросами только тут же статистика
 и все остальное, подключить осталось нормально БД и множно додлывать кнопки я пытался сделать отдельно мутод который 
 удаляет сообщения но он чет не работает как надо """


class MustangMenu():
    def __init__(self):
        self.answer_id = 0


    def question(self, message):
        self.answer_id = 0
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton("Меню")
        # back = types.KeyboardButton("Назад к вопросам")
        markup_line.add(menu)
        bot.send_message(message.chat.id, '📌Вы на вкладке вопросы', reply_markup=markup_line)

        quest = SQL.load_to_bd("quest")
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
        data = SQL.load_to_bd('feedback')

        bot.send_message(message.chat.id, '📌Вы на вкладке отзывы', reply_markup=markup_line)
        file = open(data[0]['link_imeges'] + '.jpg', 'rb')  # принимает только определеный формат можно убрать '.jpg' если ввести правильно путь в БД

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
                    info = SQL.load_to_bd('quest')[i]['answer']
                    bot.send_message(call.message.chat.id, info, reply_markup=markup_line)


    def del_coment(self, call):
        bot.delete_message(call.message.chat.id, self.answer_id)
        bot.delete_message(call.message.chat.id, self.answer_id - 1)
        bot.delete_message(call.message.chat.id, self.answer_id - 2)
    @staticmethod
    def start_play(message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        price_low = types.KeyboardButton("Меню")
        price_medium = types.KeyboardButton("Меню")
        price_high = types.KeyboardButton("Меню")
        menu = types.KeyboardButton("Меню")
        markup_line.add(menu)
        bot.send_message(message.chat.id, '📌Вы в одном шаге заработку', reply_markup=markup_line)


    def play_level_1(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        level = types.KeyboardButton("второй этап")
        markup_line.add(level)


        markup = types.InlineKeyboardMarkup(row_width=1)
        inst_com = types.InlineKeyboardButton(f"In stagram",
                                              'https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
        markup.add(inst_com)
        bot.send_message(message.chat.id, "посмотрите его сторис", reply_markup=markup)
        time.sleep(60)
        bot.send_message(message.chat.id, "поздравляю ві прошли первый этап", reply_markup=markup_line)

    def play_level_2(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        level = types.KeyboardButton("третий этап")
        markup_line.add(level)

        bot.send_photo(message.chat.id, '', "посмотрите его сторис")
        time(120)
        bot.send_message(message.chat.id, "поздравляю вы прошли второй этап", reply_markup=markup_line)



