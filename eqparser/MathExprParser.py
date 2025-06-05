# Generated from MathExpr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,62,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,20,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,1,1,1,1,1,1,1,1,1,5,1,
        43,8,1,10,1,12,1,46,9,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,1,1,1,1,1,1,
        1,3,1,58,8,1,1,2,1,2,1,2,0,1,0,3,0,2,4,0,3,1,0,5,6,1,0,1,2,1,0,10,
        12,71,0,19,1,0,0,0,2,57,1,0,0,0,4,59,1,0,0,0,6,7,6,0,-1,0,7,8,5,
        1,0,0,8,20,3,0,0,11,9,10,5,2,0,0,10,20,3,0,0,10,11,20,3,2,1,0,12,
        20,3,4,2,0,13,14,5,7,0,0,14,15,3,0,0,0,15,16,5,8,0,0,16,20,1,0,0,
        0,17,20,5,16,0,0,18,20,5,17,0,0,19,6,1,0,0,0,19,9,1,0,0,0,19,11,
        1,0,0,0,19,12,1,0,0,0,19,13,1,0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,
        20,34,1,0,0,0,21,22,10,8,0,0,22,23,5,4,0,0,23,33,3,0,0,9,24,25,10,
        7,0,0,25,26,7,0,0,0,26,33,3,0,0,8,27,28,10,6,0,0,28,29,7,1,0,0,29,
        33,3,0,0,7,30,31,10,9,0,0,31,33,5,3,0,0,32,21,1,0,0,0,32,24,1,0,
        0,0,32,27,1,0,0,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,
        1,0,0,0,35,1,1,0,0,0,36,34,1,0,0,0,37,38,5,13,0,0,38,39,5,7,0,0,
        39,44,3,0,0,0,40,41,5,9,0,0,41,43,3,0,0,0,42,40,1,0,0,0,43,46,1,
        0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,
        48,5,8,0,0,48,58,1,0,0,0,49,51,5,14,0,0,50,52,5,15,0,0,51,50,1,0,
        0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,7,0,0,54,55,3,0,0,0,55,56,
        5,8,0,0,56,58,1,0,0,0,57,37,1,0,0,0,57,49,1,0,0,0,58,3,1,0,0,0,59,
        60,7,2,0,0,60,5,1,0,0,0,6,19,32,34,44,51,57
    ]

class MathExprParser ( Parser ):

    grammarFileName = "MathExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'+'", "'!'", "'^'", "'*'", "'/'", 
                     "'('", "')'", "','", "'pi'", "'\\u03C0'", "'e'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "FUNC", "LOG", "BASE", "NUMBER", "VARIABLE", 
                      "WS" ]

    RULE_expr = 0
    RULE_funcExpr = 1
    RULE_constant = 2

    ruleNames =  [ "expr", "funcExpr", "constant" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    FUNC=13
    LOG=14
    BASE=15
    NUMBER=16
    VARIABLE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MathExprParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpr" ):
                listener.enterPowerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpr" ):
                listener.exitPowerExpr(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MathExprParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class UnaryPlusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlusExpr" ):
                listener.enterUnaryPlusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlusExpr" ):
                listener.exitUnaryPlusExpr(self)


    class FactorialExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorialExpr" ):
                listener.enterFactorialExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorialExpr" ):
                listener.exitFactorialExpr(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class FunctionExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcExpr(self):
            return self.getTypedRuleContext(MathExprParser.FuncExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)


    class ConstantExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(MathExprParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpr" ):
                listener.enterConstantExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpr" ):
                listener.exitConstantExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MathExprParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(MathExprParser.T__0)
                self.state = 8
                self.expr(11)
                pass
            elif token in [2]:
                localctx = MathExprParser.UnaryPlusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(MathExprParser.T__1)
                self.state = 10
                self.expr(10)
                pass
            elif token in [13, 14]:
                localctx = MathExprParser.FunctionExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.funcExpr()
                pass
            elif token in [10, 11, 12]:
                localctx = MathExprParser.ConstantExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.constant()
                pass
            elif token in [7]:
                localctx = MathExprParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(MathExprParser.T__6)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(MathExprParser.T__7)
                pass
            elif token in [16]:
                localctx = MathExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(MathExprParser.NUMBER)
                pass
            elif token in [17]:
                localctx = MathExprParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(MathExprParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.PowerExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 22
                        self.match(MathExprParser.T__3)
                        self.state = 23
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.MulDivExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 25
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 26
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.AddSubExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 28
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = MathExprParser.FactorialExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 31
                        self.match(MathExprParser.T__2)
                        pass

             
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_funcExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiArgFuncContext(FuncExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(MathExprParser.FUNC, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiArgFunc" ):
                listener.enterMultiArgFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiArgFunc" ):
                listener.exitMultiArgFunc(self)


    class LogExprContext(FuncExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.FuncExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOG(self):
            return self.getToken(MathExprParser.LOG, 0)
        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)

        def BASE(self):
            return self.getToken(MathExprParser.BASE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogExpr" ):
                listener.enterLogExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogExpr" ):
                listener.exitLogExpr(self)



    def funcExpr(self):

        localctx = MathExprParser.FuncExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcExpr)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = MathExprParser.MultiArgFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(MathExprParser.FUNC)
                self.state = 38
                self.match(MathExprParser.T__6)
                self.state = 39
                self.expr(0)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 40
                    self.match(MathExprParser.T__8)
                    self.state = 41
                    self.expr(0)
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 47
                self.match(MathExprParser.T__7)
                pass
            elif token in [14]:
                localctx = MathExprParser.LogExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(MathExprParser.LOG)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 50
                    self.match(MathExprParser.BASE)


                self.state = 53
                self.match(MathExprParser.T__6)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(MathExprParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MathExprParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = MathExprParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         




