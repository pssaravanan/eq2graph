grammar MathExpr;

expr
    : '-' expr                      # unaryMinusExpr
    | '+' expr                      # unaryPlusExpr
    | expr '!'                      # factorialExpr
    | expr '^' expr                 # powerExpr
    | expr op=('*'|'/') expr        # mulDivExpr
    | expr op=('+'|'-') expr        # addSubExpr
    | funcExpr                      # functionExpr
    | constant                      # constantExpr
    | '(' expr ')'                  # parenExpr
    | NUMBER                        # numberExpr
    | VARIABLE                      # variableExpr
    ;

funcExpr
    : FUNC '(' expr (',' expr)* ')'    # multiArgFunc
    | LOG (BASE)? '(' expr ')'         # logExpr
    ;

FUNC
    : 'sin' | 'cos' | 'tan'
    | 'asin' | 'acos' | 'atan'
    | 'sqrt' | 'abs' | 'exp'
    | 'floor' | 'ceil'
    | 'min' | 'max'
    ;

LOG
    : 'log' | 'ln'
    ;

constant
    : 'pi' | 'π' | 'e'
    ;

BASE
    : [0-9]+ ;

NUMBER
    : [0-9]+ ('.' [0-9]+)? ( [eE] [+-]? [0-9]+ )? ;

VARIABLE
    : [a-zA-Z_] [a-zA-Z0-9_]* ;

WS
    : [ \t\r\n]+ -> skip ;
