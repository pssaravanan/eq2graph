# Generated from MathExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathExprParser import MathExprParser
else:
    from MathExprParser import MathExprParser

# This class defines a complete listener for a parse tree produced by MathExprParser.
class MathExprListener(ParseTreeListener):

    # Enter a parse tree produced by MathExprParser#PowerExpr.
    def enterPowerExpr(self, ctx:MathExprParser.PowerExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#PowerExpr.
    def exitPowerExpr(self, ctx:MathExprParser.PowerExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#FunctionExpr.
    def enterFunctionExpr(self, ctx:MathExprParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#FunctionExpr.
    def exitFunctionExpr(self, ctx:MathExprParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:MathExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:MathExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#NumberExpr.
    def enterNumberExpr(self, ctx:MathExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#NumberExpr.
    def exitNumberExpr(self, ctx:MathExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#ParensExpr.
    def enterParensExpr(self, ctx:MathExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#ParensExpr.
    def exitParensExpr(self, ctx:MathExprParser.ParensExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#VariableExpr.
    def enterVariableExpr(self, ctx:MathExprParser.VariableExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#VariableExpr.
    def exitVariableExpr(self, ctx:MathExprParser.VariableExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MathExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MathExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#NegateExpr.
    def enterNegateExpr(self, ctx:MathExprParser.NegateExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#NegateExpr.
    def exitNegateExpr(self, ctx:MathExprParser.NegateExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#function.
    def enterFunction(self, ctx:MathExprParser.FunctionContext):
        pass

    # Exit a parse tree produced by MathExprParser#function.
    def exitFunction(self, ctx:MathExprParser.FunctionContext):
        pass



del MathExprParser