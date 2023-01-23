import hashlib

from config import FreeKassa

full_currency = {"ru": "RUB", "en": "USD"}


def get_pay(user_id, amount, currency):
    md5 = hashlib.md5()
    md5.update(
        f'{FreeKassa.shop_id}:{amount}:{FreeKassa.secret1}:{full_currency[currency]}:{user_id}'.encode('utf-8'))
    pwd = md5.hexdigest()
    return f"https://pay.freekassa.ru/?m={FreeKassa.shop_id}&oa={amount}&currency={full_currency[currency]}&o={user_id}&s={pwd}"
