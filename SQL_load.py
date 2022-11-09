import pymysql
from pymysql import cursors

# не забыть в конфиг это все перекинуть


def load_to_bd():
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
                create_table = "SELECT * FROM questions"
                cursor.execute(create_table)
                rows = cursor.fetchone()
                print(rows)
                return rows

        finally:
            connection.close()

    except Exception as ex:
        print("connected false")
        print(ex)


if __name__ =='main':
    load_to_bd()

