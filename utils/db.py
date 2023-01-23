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
            "CREATE TABLE IF NOT EXISTS users(user_id INT, username TEXT, first_name TEXT, trial BOOL, lang TEXT)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS config(price_rub INT, price_usd INT, channel_id TEXT, channel_url TEXT)")
        # cursor.execute('INSERT INTO config VALUES(250, 4, -1001363887843, "https://t.me/renderforest_bot")')
        connection.commit()


def get_user(user_id):
    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = dict_factory
        cursor: Cursor = connection.cursor()
        cursor.execute("SELECT trial FROM users WHERE user_id = ?", (user_id,))
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
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, TRUE, ?)", (user_id, username, first_name, lang))
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
