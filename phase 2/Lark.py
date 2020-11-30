from lark import Lark
from lark.indenter import Indenter

tree_grammar = r"""
    ?Program : Decl+

    Decl : VariableDecl | FunctionDecl | ClassDecl | InterfaceDecl

    VariableDecl : Variable ";"

    Variable : Type IDENTIFIER

    Type : INT | DOUBLE | BOOL | STRING | IDENTIFIER | Type "[" "]"

    FunctionDecl : Type IDENTIFIER "(" Formals")" StmtBlock | VOID IDENTIFIER "(" Formals ")" StmtBlock

    Formals : (Variable ",")* Variable | "null"

    ClassDecl : class IDENTIFIER (EXTEND IDENTIFIER)? (IMPLEMENTS (IDENTIFIER "," )* IDENTIFIER)? "{" Field* "}"

    Field : AccessMode VariableDecl | AccessMode FunctionDecl

    AccessMode : PRIVATE | PROTECTED | PUBLIC | "null"

    InterfaceDecl : INTERFACE IDENTIFIER {Prototype*}

    Prototype : Type IDENTIFIER "(" Formals ")" ";"
    | VOID IDENTIFIER "(" Formals ")" ";"

    StmtBlock : "{" VariableDecl* Stmt* "}"

    Stmt : Expr? ";" | IfStmt | WhileStmt | ForStmt
    | BreakStmt | ContinueStmt | ReturnStmt | PrintStmt | StmtBlock

    IfStmt : if "(" Expr ")" Stmt (ELSE Stmt)?

    WhileStmt : WHILE "(" Expr ")" Stmt

    ForStmt : FOR "(" Expr* ";" Expr ";" Expr* ")" Stmt

    ReturnStmt : RETURM (Expr)? ";"

    BreakStmt : BREAK";"

    ContinueStmt : CONTINUE ";"

    PrintStmt : PRINT "(" (Expr ",")* Expr ")" ";"

    Expr : LValue = Expr | Constant | LValue | THIS | Call | (Expr)
    | Expr PLUS Expr | Expr MINUS Expr | Expr STAR Expr | Expr SLASH Expr
    | Expr PERCENT Expr | MINUS Expr | Expr LESS Expr | Expr GREATEREQ Expr
    | Expr GREATER Expr | Expr LESSEQ Expr | Expr EQUALEQ Expr | Expr NOTEQUAL Expr
    | Expr AND Expr | Expr OR Expr | NOT Expr | READINTEGER "(" ")"
    | READLINE"(" ")" | NEW IDENTIFIER | NEWARRAY "(" Expr "," Type ")"
    | ITOD "(" Expr ")" | DTOI"(" Expr ")" | ITOB "(" Expr ")" | BTOI"(" Expr ")"

    LValue : IDENTIFIER | Expr "." IDENTIFIER | Expr "[" Expr "]"

    Call : IDENTIFIER "(" Actuals ")" | Expr "." IDENTIFIER "(" Actuals ")"

    Actuals : (Expr ",")* Expr | "null"

    Constant : intConstant | doubleConstant | boolConstant | stringConstant | "null"
"""



parser = Lark(tree_grammar, parser='lalr')

test_tree = """
class Main{
    static void main(){
        int x = 1;
        int y;
        z[0] = 2;
    }
}‬
"""

print(parser.parse(test_tree).pretty())
