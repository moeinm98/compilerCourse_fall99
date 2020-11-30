from lark import Lark
from lark.indenter import Indenter

tree_grammar = r"""
    ?program : decl+

    decl : variabledecl | functiondecl | classdecl | interfacedecl

    variabledecl : variable ";"

    variable : type IDENTIFIER

    type : INT | DOUBLE | BOOL | STRING | IDENTIFIER | type "[" "]"

    functiondecl : type IDENTIFIER "(" formals")" stmtblock | VOID IDENTIFIER "(" formals ")" stmtblock

    formals : (variable ",")* variable | "null"

    classdecl : "class" IDENTIFIER (EXTEND IDENTIFIER)? (IMPLEMENTS (IDENTIFIER "," )* IDENTIFIER)? "{" field* "}"

    field : accessMode variabledecl | accessmode functiondecl

    accessmode : PRIVATE | PROTECTED | PUBLIC | "null"

    interfacedecl : INTERFACE IDENTIFIER "{"prototype*"}"

    prototype : type IDENTIFIER "(" formals ")" ";"
    | VOID IDENTIFIER "(" formals ")" ";"

    stmtblock : "{" variabledecl* stmt* "}"

    stmt : expr? ";" | ifstmt | whilestmt | forstmt
    | breakstmt | continuestmt | returnstmt | printstmt | stmtblock

    ifstmt : if "(" expr ")" stmt (ELSE stmt)?

    whilestmt : WHILE "(" expr ")" stmt

    forstmt : FOR "(" expr* ";" expr ";" expr* ")" stmt

    returnstmt : RETURM (expr)? ";"

    breakstmt : BREAK";"

    continuestmt : CONTINUE ";"

    printstmt : PRINT "(" (expr ",")* expr ")" ";"

    expr : lvalue "=" expr | constant | lvalue | THIS | call | (expr)
    | expr PLUS expr | expr MINUS expr | expr STAR expr | expr SLASH expr
    | expr PERCENT expr | MINUS expr | expr LESS expr | expr GREATEREQ expr
    | expr GREATER expr | expr LESSEQ expr | expr EQUALEQ expr | expr NOTEQUAL expr
    | expr AND expr | expr OR expr | NOT expr | READINTEGER "(" ")"
    | READLINE"(" ")" | NEW IDENTIFIER | NEWARRAY "(" expr "," type ")"
    | ITOD "(" expr ")" | DTOI"(" expr ")" | ITOB "(" expr ")" | BTOI"(" expr ")"

    lvalue : IDENTIFIER | expr "." IDENTIFIER | expr "[" expr "]"

    call : IDENTIFIER "(" actuals ")" | expr "." IDENTIFIER "(" actuals ")"

    actuals : (expr ",")* expr | "null"

    constant : intconstant | doubleconstant | boolconstant | stringconstant | "null"
"""

class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

parser = Lark(tree_grammar, parser='lalr', postlex=TreeIndenter())


test_tree = """
class Main{
    static void main(){
        int x = 1;
        int y;
        z[0] = 2;
    }
}‬
"""

tree = r"""
    ?start: _NL* tree

    tree: NAME _NL [_INDENT tree+ _DEDENT]

    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE

    _NL: /(\r?\n[\t ]*)+/
"""
test = """
a
    b
    c
        d
        e
    f
        g
"""

parser = Lark(tree, parser='lalr', postlex=TreeIndenter())

print(parser.parse(test).pretty())
