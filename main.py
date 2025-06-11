from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from eqparser.MathExprLexer import MathExprLexer
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request, Body
from eqparser.MathExprLexer import MathExprLexer
from eqparser.MathExprParser import MathExprParser
from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from parser_listener import ParserListener
import numpy as np

app = FastAPI()


def evaluate_expression(expr: str, variables: dict = None) -> np.ndarray:
    stream = CommonTokenStream(MathExprLexer(InputStream(expr)))
    parser = MathExprParser(stream)
    walker = ParseTreeWalker()
    listener = ParserListener(variables)
    walker.walk(listener, parser.expr())
    result = listener.stack.pop()
    return np.array(result)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello", response_class=PlainTextResponse)
async def read_root():
    return "hello world" 

@app.post("/api/plot", response_class=JSONResponse)
async def plot_api(body: dict = Body(...)):
    # Example: just echo back the received body
    x = np.linspace(-10, 10)
    y = evaluate_expression(expr=body['eq'], variables={'x': x})
    xy = [{"x": float(xi), "y": float(yi)} for xi, yi in zip(x, y)]
    return {"message": "success", "data": xy}
    
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")