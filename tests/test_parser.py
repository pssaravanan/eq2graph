import pytest
from eqparser.MathExprLexer import MathExprLexer
from eqparser.MathExprParser import MathExprParser
from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from typing import Union
from parser_listener import ParserListener
import numpy as np

def evaluate_expression(expr: str, variables: dict = None) -> np.ndarray:
    stream = CommonTokenStream(MathExprLexer(InputStream(expr)))
    parser = MathExprParser(stream)
    walker = ParseTreeWalker()
    listener = ParserListener(variables)
    walker.walk(listener, parser.expr())
    result = listener.stack.pop()
    return np.array(result)

def test_evaluate_x_pow_3_plus_10():
    result = evaluate_expression("(x^3) + 10", variables= {'x': np.linspace(-2,2,5)})
    np.testing.assert_allclose(result, [2.0, 9.0, 10.0, 11.0, 18.0])

def test_evaluate_sin_x():
    result = evaluate_expression("sin(x) + 10", variables= {'x': np.array([-1, 0, -1])})
    np.testing.assert_allclose(result, [ 9.158529, 10.      ,  9.158529])


def test_evaluate_and_raise_error_when_variable_is_not_type_ndarray():
    with pytest.raises(Exception):
        evaluate_expression("sin(x) + 10", variables= {'x': 1})