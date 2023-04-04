import time

import telebot
from telebot import types
from SQL_load import LoadMySQL
from string import Template
import text

bot = telebot.TeleBot('5441324806:AAFX2bdVqwbpV6307GLOGNjib3p5S7gdgMk')
SQL = LoadMySQL()
prontochat = -892313553

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
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton("🔄Voltar ao menu")
        # back = types.KeyboardButton("Назад к вопросам")
        markup_line.add(menu)
        bot.send_message(message.chat.id, '📌Preguntas populares', reply_markup=markup_line)

        quest = text.questions

        markup = types.InlineKeyboardMarkup(row_width=1)

        question_1 = types.InlineKeyboardButton(quest[0][0], callback_data='0')
        question_2 = types.InlineKeyboardButton(quest[1][0], callback_data='1')
        question_3 = types.InlineKeyboardButton(quest[2][0], callback_data='2')
        question_4 = types.InlineKeyboardButton(quest[3][0], callback_data='3')
        question_5 = types.InlineKeyboardButton(quest[4][0], callback_data='4')
        question_6 = types.InlineKeyboardButton(quest[5][0], callback_data='5')

        markup.add(question_1, question_2, question_3, question_4, question_5, question_6)
        bot.send_message(message.chat.id, 'Escolha as perguntas que lhe interessam:', reply_markup=markup)

        # удаляет сообщения ответа в
    def back_to_question(self, call):
        if self.answer_id != 0:
            print(self.answer_id)
            bot.delete_message(call.message.chat.id, self.answer_id.id)

        # реализует кнопки вопрос ответ ответы берет с БД
    def call_quest(self, call):
        if call.message:
            markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
            menu = types.KeyboardButton("🔄Voltar ao menu")
            # back = types.KeyboardButton("Назад к вопросам")
            markup_line.add(menu)
            sample = Template("$question\n\n 📍 $answer")
            for i in range(6):
                if call.data == str(i):
                    info = text.questions[i]
                    self.back_to_question(call)
                    self.answer_id = bot.send_message(call.message.chat.id, sample.substitute({"question": info[0],
                                                                                              "answer": info[1]}),
                                                      reply_markup=markup_line)

    def del_coment(self, call):
        bot.delete_message(call.message.chat.id, self.answer_id)

    # принимает на себя сообщения и отправляет обратно сообщения с кнопками
    def menu(self, message):

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        com_recall = types.KeyboardButton("🗣Feedback")
        com_questions = types.KeyboardButton("❓Preguntas")
        com_auhtor = types.KeyboardButton("👨‍💻Author")
        com_statistic = types.KeyboardButton("📊Estatísticas")
        com_earn = types.KeyboardButton("💶Ganhar dinheiro")
        markup.add(com_recall, com_questions, com_auhtor, com_statistic, com_earn)

        name = message.chat.first_name
        bot.send_message(message.chat.id, text.greeting.substitute({'name': name}), reply_markup=markup, parse_mode="Markdown")

        # реализация кнопки автора
    @staticmethod
    def auhtor(message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('🔄Voltar ao menu')
        markup_line.add(menu)

        bot.send_message(message.chat.id, '📌O projeto "Mustang BOT"', reply_markup=markup_line)

        markup = types.InlineKeyboardMarkup(row_width=2)
        inst_com = types.InlineKeyboardButton(f"📷 Instagram", 'https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
        tele_com = types.InlineKeyboardButton(f"✉️ Telegram", 'https://t.me/FernandoCardosoJr/')
        info_com = types.InlineKeyboardButton(f"💬 História do projeto", 'https://telegra.ph/Como-tudo-isso-come%C3%A7ou-05-14')
        markup.add(tele_com, inst_com, info_com)

        file = open("images/author.jpg", 'rb')

        bot.send_photo(message.chat.id, file, text.text_author.substitute(), reply_markup=markup)

    # риализует работу кнопки отзывы из бд берет сылки на фото главное что бы было в jpg это можно поменять в самом
    @staticmethod
    def feedback(message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('🔄Voltar ao menu')
        more = types.KeyboardButton('Mais feedback ⏩')
        markup_line.add(more, menu)
        data = SQL.select_to_bd('feedback')

        bot.send_message(message.chat.id, '📌Вы на вкладке отзывы', reply_markup=markup_line)
        # принимает только определеный формат можно убрать '.jpg' если ввести правильно путь в БД
        file = open(data[0]['link_imeges'], 'rb')

        bot.send_photo(message.chat.id, file, f'{data[0]["Coment"]}\n\n[интсаграм человека]({data[0]["link_insta"]})',
                       parse_mode='Markdown')

    # Реализация кнопки статистика

    def statistic(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        menu = types.KeyboardButton('🔄Voltar ao menu')
        markup_line.add(menu)
        data = SQL.select_to_bd('statictic')[0]

        bot.send_message(message.chat.id, '📌Вы на вкладке статистика', reply_markup=markup_line)

        bot.send_message(message.chat.id, text.statistic_text.substitute({"users": data['users'],
                                                                          "money": data['money'],
                                                                          "friend": data['friend'],
                                                                          "quest": data['quest']}), parse_mode="Markdown")

    def preparation(self, message):

        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        com_ua = types.InlineKeyboardButton('Espanha')
        com_br = types.InlineKeyboardButton('Portugal')
        com_ca = types.InlineKeyboardButton('Canadá')
        menu = types.KeyboardButton('🔄Voltar ao menu')
        markup_line.add(com_ua, com_br, com_ca, menu)

        comment = 'A Binance é a patrocinadora e parceira oficial do projeto, a empresa garante seu lucro!'
        file = open('images/sertificat.jpg', 'rb')

        bot.send_photo(message.chat.id, file, comment)
        bot.send_message(message.chat.id, "Escolha seu país de residência⤵️", reply_markup=markup_line)

    def preparation_two(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        price_low = types.InlineKeyboardButton("3200")
        price_medium = types.InlineKeyboardButton("5100")
        price_high = types.InlineKeyboardButton("8500")
        menu = types.InlineKeyboardButton("🔄Voltar ao menu")
        markup_line.add(price_low, price_medium, price_high, menu)
        file = open("images/photo1.jpg", 'rb')
        text_ = 'Fernando é um parceiro oficial da "Ford" e "Binance". Esta é uma garantia de sua confiança em mim!'

        bot.send_photo(message.chat.id, file, text_)
        bot.send_message(message.chat.id, 'Quanto você quer ganhar?⤵️', reply_markup=markup_line)

    def start(self, message):
        SQL.update_to_user(message.chat.id, message.text)
        markup_start = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        start = types.InlineKeyboardButton("▶️START")
        menu = types.InlineKeyboardButton("🔄Voltar ao menu")

        markup = types.InlineKeyboardMarkup()
        como = types.InlineKeyboardButton("⚙️ Como funciona?",
                                          url="https://telegra.ph/Como-funciona-o-sistema-de-algoritmos-05-14")

        markup.add(como)
        markup_start.add(start, menu)

        bot.send_message(message.chat.id, "📖 *GERENTE*, selecionamos tarefas adequadas para você...",
                         reply_markup=markup_start, parse_mode='Markdown')
        bot.send_message(message.chat.id, text.text_start.substitute({"price": message.text}),
                         reply_markup=markup, parse_mode='Markdown')

    def level_1(self, message):
        price = SQL.select_to_bd("user", message.chat.id)[0]['price']
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        level = types.KeyboardButton('Sim, vá para "Tarefa 2"⏩')
        markup_line.add(level)

        markup = types.InlineKeyboardMarkup(row_width=1)
        inst_com = types.InlineKeyboardButton(f"📷 Assine a stagram",
                                              'https://instagram.com/fernando_cardoso_jr?igshid=YmMyMTA2M2Y=')
        markup.add(inst_com)
        bot.send_message(message.chat.id, '📌Tarefa 1')

        # bot.send_message(message.chat.id, "📖 подбераем задания... б", reply_markup=bot.)
        bot.send_message(message.chat.id, text.text_level1.substitute({"price": price}), reply_markup=markup)
        time.sleep(1)
        bot.send_message(message.chat.id, '☑️GERENTE, você completou com sucesso a "Tarefa 1"!',
                         reply_markup=markup_line)

    def level_2(self, message):

        price = SQL.select_to_bd('user', message.chat.id)[0]['price']
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        level = types.KeyboardButton('Sim, vá para "Tarefa 3"⏩')

        markup = types.InlineKeyboardMarkup()
        conatate = types.InlineKeyboardButton("📩Contate Margarida",
                                              url="https://xn--80affa3aj0al.xn--80asehdb/#@margaridalmeida")
        markup.add(conatate)

        markup_line.add(level)

        video = open("images/video_2022-11-20_22-15-19.mp4", "rb")
        bot.send_message(message.chat.id, '☑️GERENTE, você completou com sucesso a "Tarefa 1"!')

        bot.send_message(message.chat.id, '📌Tarefa 2')
        bot.send_video(message.chat.id, video)
        bot.send_message(message.chat.id, text.text_level2.substitute({"price": price}), parse_mode="Markdown")
        time.sleep(5)
        bot.send_message(message.chat.id, text.text_level2_after.substitute({'price': price}), parse_mode="Markdown",
                         reply_markup=markup_line)

    def level_3(self, message):
        markup_line = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        yes = types.InlineKeyboardButton('Sim, vou deixar uma feedback')
        no = types.InlineKeyboardButton('Não, eu quero permanecer incógnito')
        markup_line.add(yes, no)

        markup = types.InlineKeyboardMarkup()
        sait = types.InlineKeyboardButton('🖥Navegue pelo site',
                                          url="https://mustangbot-pt.com/")
        markup.add(sait)

        file = open("images/level3.jpg", "rb")

        bot.send_message(message.chat.id, '☑️GERENTE, você completou com sucesso a "Tarefa 2"!')
        bot.send_message(message.chat.id, '📌Tarefa 3', reply_markup=markup_line)
        bot.send_photo(message.chat.id, file, text.text_level3.substitute(), reply_markup=markup)




