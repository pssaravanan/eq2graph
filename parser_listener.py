import math
from eqparser.MathExprListener import MathExprListener
from eqparser.MathExprParser import MathExprParser
import numpy as np

class ParserListener(MathExprListener):
    def __init__(self, variables: dict[str, np.ndarray] = None):
        self.stack = []
        self.vars = variables or {}

    def exitNumberExpr(self, ctx:MathExprParser.NumberExprContext):
        self.stack.append(float(ctx.getText()))

    def exitVariableExpr(self, ctx:MathExprParser.VariableExprContext):
        var = ctx.getText()
        value = self.vars.get(var, 0)
        if not isinstance(value, np.ndarray):
            raise TypeError(f"Variable '{var}' is expected to be a numpy ndarray, but got {type(value).__name__}")
        self.stack.append(value)

    def exitNegateExpr(self, ctx:MathExprParser.NegateExprContext):
        val = self.stack.pop()
        self.stack.append(-val)

    def exitParensExpr(self, ctx:MathExprParser.ParensExprContext):
        # No action needed, result already on stack
        pass

    def exitPowerExpr(self, ctx:MathExprParser.PowerExprContext):
        right = self.stack.pop()
        left = self.stack.pop()
        self.stack.append(left ** right)

    def exitMulDivExpr(self, ctx:MathExprParser.MulDivExprContext):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.op.text == '*':
            self.stack.append(left * right)
        else:
            self.stack.append(left / right)

    def exitAddSubExpr(self, ctx:MathExprParser.AddSubExprContext):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.op.text == '+':
            self.stack.append(left + right)
        else:
            self.stack.append(left - right)

    def exitFunctionExpr(self, ctx:MathExprParser.FunctionExprContext):
        arg = self.stack.pop()
        fname = ctx.function().FUNC_NAME().getText()
        func_map = {
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'log': np.log,     # natural log
            'log10': np.log10,
            'ln': np.log,
            'sqrt': np.sqrt,
            'abs': np.abs,
        }
        self.stack.append(func_map[fname](arg))
