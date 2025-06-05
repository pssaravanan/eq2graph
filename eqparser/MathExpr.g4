grammar MathExpr;

// Parser Rules
expr
    : expr op=('*'|'/') expr         # MulDivExpr
    | expr op=('+'|'-') expr         # AddSubExpr
    | expr '^' expr                  # PowerExpr
    | '-' expr                       # NegateExpr
    | '(' expr ')'                   # ParensExpr
    | function                       # FunctionExpr
    | NUMBER                         # NumberExpr
    | VARIABLE                       # VariableExpr
    ;

function
    : FUNC_NAME '(' expr ')'
    ;

// Lexer Rules
FUNC_NAME: 'sin' | 'cos' | 'tan' | 'log' | 'log10' | 'ln' | 'sqrt' | 'abs';
NUMBER: [0-9]+ ('.' [0-9]+)?;
VARIABLE: [a-zA-Z];
WS: [ \t\r\n]+ -> skip;
