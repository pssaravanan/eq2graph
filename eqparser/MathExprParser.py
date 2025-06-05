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
        4,1,11,36,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,3,0,15,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,2,0,2,0,2,1,0,1,2,1,0,
        3,4,40,0,14,1,0,0,0,2,30,1,0,0,0,4,5,6,0,-1,0,5,6,5,4,0,0,6,15,3,
        0,0,5,7,8,5,6,0,0,8,9,3,0,0,0,9,10,5,7,0,0,10,15,1,0,0,0,11,15,3,
        2,1,0,12,15,5,9,0,0,13,15,5,10,0,0,14,4,1,0,0,0,14,7,1,0,0,0,14,
        11,1,0,0,0,14,12,1,0,0,0,14,13,1,0,0,0,15,27,1,0,0,0,16,17,10,8,
        0,0,17,18,7,0,0,0,18,26,3,0,0,9,19,20,10,7,0,0,20,21,7,1,0,0,21,
        26,3,0,0,8,22,23,10,6,0,0,23,24,5,5,0,0,24,26,3,0,0,7,25,16,1,0,
        0,0,25,19,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,1,1,0,0,0,29,27,1,0,0,0,30,31,5,8,0,0,31,32,5,6,0,0,32,
        33,3,0,0,0,33,34,5,7,0,0,34,3,1,0,0,0,3,14,25,27
    ]

class MathExprParser ( Parser ):

    grammarFileName = "MathExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'^'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FUNC_NAME", "NUMBER", "VARIABLE", "WS" ]

    RULE_expr = 0
    RULE_function = 1

    ruleNames =  [ "expr", "function" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    FUNC_NAME=8
    NUMBER=9
    VARIABLE=10
    WS=11

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


    class FunctionExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(MathExprParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)


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


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)


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


    class NegateExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MathExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegateExpr" ):
                listener.enterNegateExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegateExpr" ):
                listener.exitNegateExpr(self)



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
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = MathExprParser.NegateExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(MathExprParser.T__3)
                self.state = 6
                self.expr(5)
                pass
            elif token in [6]:
                localctx = MathExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(MathExprParser.T__5)
                self.state = 8
                self.expr(0)
                self.state = 9
                self.match(MathExprParser.T__6)
                pass
            elif token in [8]:
                localctx = MathExprParser.FunctionExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.function()
                pass
            elif token in [9]:
                localctx = MathExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(MathExprParser.NUMBER)
                pass
            elif token in [10]:
                localctx = MathExprParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(MathExprParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MathExprParser.MulDivExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 17
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 18
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MathExprParser.AddSubExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 20
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 21
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MathExprParser.PowerExprContext(self, MathExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 23
                        self.match(MathExprParser.T__4)
                        self.state = 24
                        self.expr(7)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_NAME(self):
            return self.getToken(MathExprParser.FUNC_NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(MathExprParser.ExprContext,0)


        def getRuleIndex(self):
            return MathExprParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MathExprParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(MathExprParser.FUNC_NAME)
            self.state = 31
            self.match(MathExprParser.T__5)
            self.state = 32
            self.expr(0)
            self.state = 33
            self.match(MathExprParser.T__6)
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
         




