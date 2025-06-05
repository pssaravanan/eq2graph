from eqparser.MathExprLexer import MathExprLexer
from eqparser.MathExprListener import MathExprListener
from eqparser.MathExprParser import MathExprParser
from antlr4 import *


class EvalListener(MathExprListener):
    def enterEveryRule(self, ctx:ParserRuleContext):
        print(ctx.getText())
        
    
def main():
    lexer = MathExprLexer(InputStream("x+1"))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    r = parser.expr()
    walker = ParseTreeWalker()
    listener = EvalListener()
    walker.walk(listener, r)
    print(r.toStringTree(recog=parser))
    
if __name__ == "__main__":
    main()