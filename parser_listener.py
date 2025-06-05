import math
from eqparser.MathExprListener import MathExprListener
from eqparser.MathExprParser import MathExprParser

class ParserListener(MathExprListener):
    def __init__(self, variables=None):
        self.stack = []
        self.vars = variables or {}

    def exitNumberExpr(self, ctx:MathExprParser.NumberExprContext):
        self.stack.append(float(ctx.getText()))

    def exitVariableExpr(self, ctx:MathExprParser.VariableExprContext):
        var = ctx.getText()
        self.stack.append(self.vars.get(var, 0))

    def exitNegateExpr(self, ctx:MathExprParser.NegateExprContext):
        val = self.stack.pop()
        self.stack.append(-val)

    def exitParensExpr(self, ctx:MathExprParser.ParensExprContext):
        # No action needed, result already on stack
        pass

    def exitPowerExpr(self, ctx:MathExprParser.PowerExprContext):
        right = self.stack.pop()
        left = self.stack.pop()
        print(left, right)
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
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,     # natural log
            'log10': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'abs': abs,
        }
        self.stack.append(func_map[fname](arg))
