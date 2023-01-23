from contextlib import closing
from sqlite3 import Cursor
import sqlite3

database = "utils/database.db"


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def start():
    with closing(sqlite3.connect(database)) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users(user_id INT, username TEXT, first_name TEXT, trial BOOL, lang TEXT, feedback_gift BOOL)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS config(price_rub INT, price_usd INT, channel_id TEXT, channel_url TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INT, url TEXT, file_id TEXT, slogan TEXT, is_paid BOOL, have_feedback BOOL)")
        # cursor.execute('INSERT INTO config VALUES(250, 4, -1001363887843, "https://t.me/renderforest_bot")')
        connection.commit()


def get_user(user_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone()


def get_lang(user_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))
        data = cursor.fetchone()
        if data is None:
            return "ru"
        return data["lang"]


def add_user(user_id, username, first_name, lang):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, TRUE, ?, FALSE)", (user_id, username, first_name, lang))
        connection.commit()


def change_trial(user_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("UPDATE users SET trial = FALSE WHERE user_id = ?", (user_id,))
        connection.commit()


def get_channel_config():
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("SELECT channel_id as id, channel_url as url FROM config")
        return cursor.fetchone()


def change_price(price, currency):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        if currency == "RUB":
            cursor.execute("UPDATE config SET price_rub = ?", (price,))
        if currency == "USD":
            cursor.execute("UPDATE config SET price_usd = ?", (price,))
        connection.commit()


def change_channel(channel_data):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("UPDATE config SET channel_id = ?, channel_url = ?", (channel_data["id"], channel_data["url"]))
        connection.commit()


def get_price(currency):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        if currency == "ru":
            cursor.execute("SELECT price_rub as price FROM config")
        if currency == "en":
            cursor.execute("SELECT price_usd as price FROM config")
        return cursor.fetchone()


def create_order(user_id, video_data):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO orders(user_id, url, file_id, slogan, is_paid, have_feedback) VALUES (?, ?, ?, ?, FALSE, FALSE)",
            (user_id, video_data["url"], video_data["logo"], video_data["text"]))
        connection.commit()
        return cursor.lastrowid


def change_paid_status(order_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("UPDATE orders SET is_paid = TRUE WHERE id = ?", (order_id,))
        connection.commit()


def change_feedback_status(order_id, user_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("UPDATE orders SET have_feedback = TRUE WHERE id = ?", (order_id,))
        cursor.execute("UPDATE users SET feedback_gift = TRUE WHERE user_id = ?", (user_id,))
        connection.commit()


def remove_feedback_gift(user_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("UPDATE users SET feedback_gift = FALSE WHERE user_id = ?", (user_id,))
        connection.commit()


def get_order(order_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
        return cursor.fetchone()
