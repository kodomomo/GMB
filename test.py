from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/test')
async def he_ma_look_i_made_it(request: Request):
    from pprint import pprint

    pprint(
        await request.json()
    )

