from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.post('/api/pay')
async def check_pay(req: Request):
    raise HTTPException(200, "ok")

@app.get('/api/pay')
async def check_pay_post(req: Request):
    print(req.query_params)
    raise HTTPException(200, "ok")

@app.get('/ok')
async def checkay(req: Request):
    raise HTTPException(200, "ok")


@app.get('/error')
async def ck_pay(req: Request):
    raise HTTPException(200, "ok")
