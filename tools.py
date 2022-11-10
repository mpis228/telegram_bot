import telebot
from telebot import types
from SQL_load import LoadMySQL
bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
SQL = LoadMySQL()


class MustangMenu():

    def __init__(self):
        self.answer_id = 0


    def question(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton("Меню")
        # back = types.KeyboardButton("Назад к вопросам")
        markup_line.add(menu)
        bot.send_message(message.chat.id, '📌Вы на вкладке вопросы', reply_markup=markup_line)

        quest = SQL.load_to_bd()
        markup = types.InlineKeyboardMarkup(row_width=1)

        question_1 = types.InlineKeyboardButton(quest[0]['question'], callback_data='0')
        question_2 = types.InlineKeyboardButton(quest[1]['question'], callback_data='1')
        question_3 = types.InlineKeyboardButton(quest[2]['question'], callback_data='2')
        question_4 = types.InlineKeyboardButton(quest[3]['question'], callback_data='3')

        markup.add(question_1, question_2, question_3, question_4)
        bot.send_message(message.chat.id, 'часто задаваемые вопросы', reply_markup=markup)

    def menu(self, message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        com_recall = types.KeyboardButton("Отзывы")
        com_questions = types.KeyboardButton("Вопросы")
        com_auhtor = types.KeyboardButton("Автор")
        com_statistic = types.KeyboardButton("Статистика")
        com_earn = types.KeyboardButton("заработать")
        markup.add(com_recall, com_questions, com_auhtor, com_statistic, com_earn)
        bot.send_message(message.chat.id, "Вас приветсвует мустангру бот ", reply_markup=markup)

    def auhtor(self, message):
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

    def reviews(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        markup_line.add(menu)

        bot.send_message(message.chat.id, '📌Вы на вкладке отзывы', reply_markup=markup_line)

        bot.send_message(message.chat.id, 'тут будут отзывы')

    def statistic(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('Меню')
        markup_line.add(menu)

        bot.send_message(message.chat.id, '📌Вы на вкладке статистика', reply_markup=markup_line)

        bot.send_message(message.chat.id, 'тут будет статистика')

    def back_to_question(self, message):
        if self.answer_id != 0:
            print(self.answer_id)
            bot.delete_message(message.chat.id, self.answer_id + 1)
        self.question(message)

    def call_quest(self, call):
        if call.message:
            markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            menu = types.KeyboardButton("Меню")
            back = types.KeyboardButton("Назад к вопросам")
            markup_line.add(back, menu)
            self.answer_id = call.message.id
            bot.delete_message(call.message.chat.id, self.answer_id)
            bot.delete_message(call.message.chat.id, self.answer_id - 1)
            bot.delete_message(call.message.chat.id, self.answer_id - 2)
            for i in range(4):
                if call.data == str(i):
                    info = SQL.load_to_bd()[i]['answer']
                    bot.send_message(call.message.chat.id, info, reply_markup=markup_line)









