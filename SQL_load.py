import pymysql
from pymysql import cursors
import random

# не забыть в конфиг это все перекинуть


def count_feedback():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Mpython1996',
            database='telebot',
            cursorclass=cursors.DictCursor
        )
        try:
            # select table
            with connection.cursor() as cursor:
                create_table = "SELECT count(*) as count from feedback"
                cursor.execute(create_table)
                rows = cursor.fetchall()
                return rows

        finally:
            connection.close()

    except Exception as ex:
        print("connected false")
        print(ex)


count = count_feedback()[0]['count']


class LoadMySQL():
    def __init__(self):
        self.count = 1

    @staticmethod
    def test():
        try:
            connection = pymysql.connect(
                host='34.70.12.24',
                port=80,
                user='root',
                password='Mpython1996',
                database='mustangbot',
                cursorclass=cursors.DictCursor
            )
            print("connected successfully")

        except Exception as ex:
            print("connected false")
            print(ex)
    """принимает на семя ключ запроса который в свою очеред определяет какой запрос в базу даных отправить для кнопок 
    статистика, задаваемые вопросы, отзывы"""

    def select_to_bd(self, request, user_id=None):
        try:
            connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='Mpython1996',
                database='telebot',
                cursorclass=cursors.DictCursor
            )
            print("connected select")
            try:

                # select table
                with connection.cursor() as cursor:
                    select_table = str(self.find_request(request, user_id))
                    cursor.execute(select_table)
                    rows = cursor.fetchall()
                    print(rows)
                    return rows
            finally:
                connection.close()

        except Exception as ex:
            print("connected false")
            print(ex)

    def insert_user(self, user):
        try:
            connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='Mpython1996',
                database='telebot',
                cursorclass=cursors.DictCursor
            )
            print("connected insert")
            try:
                # select table
                with connection.cursor() as cursor:
                    create_table = f"insert users(user_id, earned, completed_quests) VALUES({user}, 0, 0);"
                    cursor.execute(create_table)
            finally:
                connection.commit()
                connection.close()

        except Exception as ex:
            print("connected false")
            print(ex)

    @staticmethod
    def update_to_user(user_id, price):
        try:
            connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='Mpython1996',
                database='telebot',
                cursorclass=cursors.DictCursor
            )
            print("connected update")
            try:

                # select table
                with connection.cursor() as cursor:
                    update_table = f"update users set price = {price} where user_id = {user_id}"
                    cursor.execute(update_table)


            finally:
                connection.commit()
                connection.close()
        except Exception as ex:
            print("connected false")
            print(ex)

    @staticmethod
    def update_to_level(level, user_id):
        try:
            connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='Mpython1996',
                database='telebot',
                cursorclass=cursors.DictCursor
            )
            print("connected update")
            try:

                # select table
                with connection.cursor() as cursor:
                    insert_table = f"update users set {level} = True where user_id = {user_id}"
                    cursor.execute(insert_table)
            finally:
                connection.commit()
                connection.close()
        except Exception as ex:
            print("connected false")
            print(ex)
    """принимает ключ которым определяет какой запрос нужен"""

    def find_request(self, request, user=None):
        if request == 'feedback':
            return f"SELECT * from feedback where id = {random.randint(1, count)};"
        elif request == 'quest':
            return "SELECT * from questions"
        elif request == "user":
            return f"Select * from users where user_id = {user}"
        elif request == "statictic":
            return "SELECT * from statictic"


    """user_id нужен для созданния поля и учесть выбор пользователя заработка"""


if __name__ == '__main__':
    test = LoadMySQL()
    test.select_to_bd('feedback')
