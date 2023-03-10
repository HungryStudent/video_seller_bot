from yoomoney import Quickpay
from config import FreeKassa, yoomoney_id, qiwi_phone, qiwi_key

import hashlib

full_currency = {"ru": "RUB", "en": "USD"}


def get_urls(order_id, amount, currency):
    md5 = hashlib.md5()
    md5.update(
        f'{FreeKassa.shop_id}:{amount}:{FreeKassa.secret1}:{full_currency[currency]}:{order_id}'.encode('utf-8'))
    pwd = md5.hexdigest()
    pay_urls = {
        "freekassa": f"https://pay.freekassa.ru/?m={FreeKassa.shop_id}&oa={amount}&currency={full_currency[currency]}&o={order_id}&s={pwd}"}
    quickpay = Quickpay(
        receiver=yoomoney_id,
        quickpay_form="shop",
        targets="Sponsor this project",
        paymentType="SB",
        sum=amount,
        label=order_id
    )
    pay_urls["yoomoney"] = quickpay.redirected_url
    pay_urls[
        "qiwi"] = f"https://oplata.qiwi.com/create?publicKey={qiwi_key}&billId={order_id}&amount={amount}"
    return pay_urls
