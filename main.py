from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from .eqparser.MathExprLexer import MathExprLexer

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def read_root():
    return "hello world"