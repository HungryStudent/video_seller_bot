from fastapi import FastAPI, Request, HTTPException

from config import admin_id
from keyboards import user as user_kb
from keyboards import admin as admin_kb
from create_bot import bot
from handlers import texts
from utils import db

app = FastAPI()


# MERCHANT_ID=27975&AMOUNT=200&intid=71951456&MERCHANT_ORDER_ID=359902077&P_EMAIL=skilord%40yandex.ru&P_PHONE=&CUR_ID=4&commission=0&SIGN=37ddd270ccb531c73a2f166e4c4c6cc0

@app.get('/api/pay')
async def check_pay_post(MERCHANT_ORDER_ID):
    db.change_paid_status(MERCHANT_ORDER_ID)
    order = db.get_order(MERCHANT_ORDER_ID)
    lang = db.get_lang(order["user_id"])
    user = db.get_user(order["user_id"])
    await bot.send_message(order["user_id"], texts.Video.finish[lang])
    await bot.send_photo(admin_id, order["file_id"],
                         caption=texts.new_order[lang].format(username=user["username"],
                                                                    url=order["url"],
                                                                    text=order["slogan"]),
                         reply_markup=admin_kb.new_order(order["user_id"], MERCHANT_ORDER_ID))
    return 'YES'


@app.get('/ok')
async def checkay(req: Request):
    raise HTTPException(200, "ok")


@app.get('/error')
async def ck_pay(req: Request):
    raise HTTPException(200, "ok")
