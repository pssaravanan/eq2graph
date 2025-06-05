import pytest
from eqparser.MathExprLexer import MathExprLexer
from eqparser.MathExprParser import MathExprParser
from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from typing import Union
from parser_listener import ParserListener

def evaluate_expression(expr: str, variables: dict = None) -> Union[int, float]:
    stream = CommonTokenStream(MathExprLexer(InputStream(expr)))
    parser = MathExprParser(stream)
    walker = ParseTreeWalker()
    listener = ParserListener(variables)
    walker.walk(listener, parser.expr())
    return listener.stack.pop()

def test_evaluate_x_pow_3_plus_10():
    # Expression: x ^ 3 + 10
    # Simulate parse tree traversal:
    # 1. Push variable x (value 2)
    # 2. Push number 3
    # 3. Power: x^3
    # 4. Push number 10
    # 5. Add: (x^3) + 10

    result = evaluate_expression("(x^3) + 10", variables= {'x': 10})
    assert result == 1010.10