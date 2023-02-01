from fastapi import FastAPI, Request, HTTPException

from config import admin_id
from keyboards import user as user_kb
from keyboards import admin as admin_kb
from create_bot import bot
from handlers import texts
from utils import db

app = FastAPI()


async def approve_order(order_id):
    db.change_paid_status(order_id)
    order = db.get_order(order_id)
    lang = db.get_lang(order["user_id"])
    user = db.get_user(order["user_id"])
    await bot.send_message(order["user_id"], texts.Video.finish[lang])
    await bot.send_photo(admin_id, order["file_id"],
                         caption=texts.new_order[lang].format(username=user["username"],
                                                              url=order["url"],
                                                              text=order["slogan"]),
                         reply_markup=admin_kb.new_order(order["user_id"], order_id))


@app.get('/api/pay')
async def check_pay_freekassa(MERCHANT_ORDER_ID):
    await approve_order(MERCHANT_ORDER_ID)
    return 'YES'


@app.post('/pay/yoomoney')
async def check_pay_yoomoney(req: Request):
    item = await req.form()
    order_id = int(item["label"])
    await approve_order(order_id)
    raise HTTPException(200, "OK")


@app.post('/pay/qiwi')
async def check_pay_qiwi(req: Request):
    item = await req.json()
    if item["payment"]["status"] == "SUCCESS":
        order_id = int(item["payment"]["comment"])
        await approve_order(order_id)
    raise HTTPException(200, "OK")


@app.get('/ok')
async def checkay(req: Request):
    raise HTTPException(200, "OK")


@app.get('/error')
async def ck_pay(req: Request):
    raise HTTPException(200, "ok")
