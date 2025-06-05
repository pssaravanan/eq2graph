# Generated from MathExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MathExprParser import MathExprParser
else:
    from MathExprParser import MathExprParser

# This class defines a complete listener for a parse tree produced by MathExprParser.
class MathExprListener(ParseTreeListener):

    # Enter a parse tree produced by MathExprParser#variableExpr.
    def enterVariableExpr(self, ctx:MathExprParser.VariableExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#variableExpr.
    def exitVariableExpr(self, ctx:MathExprParser.VariableExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#powerExpr.
    def enterPowerExpr(self, ctx:MathExprParser.PowerExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#powerExpr.
    def exitPowerExpr(self, ctx:MathExprParser.PowerExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#addSubExpr.
    def enterAddSubExpr(self, ctx:MathExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#addSubExpr.
    def exitAddSubExpr(self, ctx:MathExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:MathExprParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:MathExprParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#numberExpr.
    def enterNumberExpr(self, ctx:MathExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#numberExpr.
    def exitNumberExpr(self, ctx:MathExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#unaryPlusExpr.
    def enterUnaryPlusExpr(self, ctx:MathExprParser.UnaryPlusExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#unaryPlusExpr.
    def exitUnaryPlusExpr(self, ctx:MathExprParser.UnaryPlusExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#factorialExpr.
    def enterFactorialExpr(self, ctx:MathExprParser.FactorialExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#factorialExpr.
    def exitFactorialExpr(self, ctx:MathExprParser.FactorialExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:MathExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:MathExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#parenExpr.
    def enterParenExpr(self, ctx:MathExprParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#parenExpr.
    def exitParenExpr(self, ctx:MathExprParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#functionExpr.
    def enterFunctionExpr(self, ctx:MathExprParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#functionExpr.
    def exitFunctionExpr(self, ctx:MathExprParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#constantExpr.
    def enterConstantExpr(self, ctx:MathExprParser.ConstantExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#constantExpr.
    def exitConstantExpr(self, ctx:MathExprParser.ConstantExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#multiArgFunc.
    def enterMultiArgFunc(self, ctx:MathExprParser.MultiArgFuncContext):
        pass

    # Exit a parse tree produced by MathExprParser#multiArgFunc.
    def exitMultiArgFunc(self, ctx:MathExprParser.MultiArgFuncContext):
        pass


    # Enter a parse tree produced by MathExprParser#logExpr.
    def enterLogExpr(self, ctx:MathExprParser.LogExprContext):
        pass

    # Exit a parse tree produced by MathExprParser#logExpr.
    def exitLogExpr(self, ctx:MathExprParser.LogExprContext):
        pass


    # Enter a parse tree produced by MathExprParser#constant.
    def enterConstant(self, ctx:MathExprParser.ConstantContext):
        pass

    # Exit a parse tree produced by MathExprParser#constant.
    def exitConstant(self, ctx:MathExprParser.ConstantContext):
        pass



del MathExprParser