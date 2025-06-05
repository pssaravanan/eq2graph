from eqparser.MathExprLexer import MathExprLexer
from eqparser.MathExprListener import MathExprListener
from eqparser.MathExprParser import MathExprParser
from antlr4 import *
from eval_listener import EvalListener

def main():
    lexer = MathExprLexer(InputStream("(x^10) + 1"))
    stream = CommonTokenStream(lexer)
    parser = MathExprParser(stream)
    r = parser.expr()
    walker = ParseTreeWalker()
    listener = EvalListener({'x': 10})
    walker.walk(listener, r)
    print(r.toStringTree(recog=parser))
    print(listener.stack.pop())
    
if __name__ == "__main__":
    main()