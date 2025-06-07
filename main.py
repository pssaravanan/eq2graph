from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from eqparser.MathExprLexer import MathExprLexer
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/hello", response_class=PlainTextResponse)
async def read_root():
    return "hello world" 

app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")