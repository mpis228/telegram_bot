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
                rows = cursor.fetchone()
                return rows

        finally:
            connection.close()

    except Exception as ex:
        print("connected false")
        print(ex)


count = count_feedback()['count']


class LoadMySQL():
    def __init__(self):
        self.count = 1

    def test(self):
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

    def load_to_bd(self, request):
        try:
            connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='Mpython1996',
                database='telebot',
                cursorclass=cursors.DictCursor
            )
            print("connected successfully")
            try:

                # select table
                with connection.cursor() as cursor:
                    create_table = str(self.find_request(request))
                    cursor.execute(create_table)
                    rows = cursor.fetchall()
                    print(rows)
                    return rows

            finally:
                connection.close()

        except Exception as ex:
            print("connected false")
            print(ex)
    """принимает ключ которым определяет какой запрос нужен"""
    def find_request(self, request):
        if request == 'feedback':
            return f"SELECT * from feedback where id = {random.randint(1, count)};"
        elif request == 'quest':
            return "SELECT * from questions"
    """user_id нужен для созданния поля и учесть выбор пользователя заработка"""
    def insert_to_bd(self, user_id, price):
        return f"insert table price_user(user_id, price) values({user_id}, {price})"





if __name__ == '__main__':
    test = LoadMySQL()
    test.load_to_bd('feedback')
