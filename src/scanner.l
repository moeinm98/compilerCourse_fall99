%option noyywrap
%option header-file="lex.yy.h"

%{
#include <iostream>
#include "scanner.h"

#define YY_DECL int yylex()
%}

%%

// skip whitespace
[\n\t]+			; //ignore
[[:space:]]+	; //ignore


// skip comments
"//".*										; //single line
[/][*][^*]*[*]+([^*/][^*]*[*]+)*[/]			; //multiple line



// match keywords

"void"			return VOID;
"int"			return INT;
"double"		return DOUBLE;
"bool"			return BOOL;
"string"		return STRING;
"class"			return CLASS;
"interface"		return INTERFACE;
"null"			return NULL;
"this"			return THIS;
"extend"		return EXTEND;
"implements"	return IMPLEMENTs;
"for"			return FOR;
"while"			return WHILE;
"if"			return IF;
"else"			return ELSE;
"return"		return RETURN;
"break"			return BREAK;
"continue"		return CONTINUE;
"new"			return NEW;
"NewArray"		return NEWARRAY;
"Print"			return PRINT;
"ReadInteger"	return READINTEGER;
"ReadLine"		return READLINE;
"dtoi"			return DTOI;
"itod"			return ITOD;
"btoi"			return BTOI;
"itob"			return ITOB;
"private"		return PRiVATE;
"protected"		return PROTECTED;
"public"		return PUBLIC;


// match identifiers

[a-zA-Z][a-zA-Z0-9_]*		return IDENTIFIER; //todo return the name of the identifier


// match Operators
"+"			return PLUS;
"-"			return MINUS;
"*"			return STAR;
"/"			return SLASH;
"%"			return PERCENT;

">"			return GREATER;
"<"			return LESS;
"<="		return GREATEREQ;
">="		retrun LESSEQ;
"="			return EQUAL;
"=="		retrun EQUALEQ;
"!="		return NOTEQUAL;
"||"		return OR;
"!"			return NOT;
";"			return SEMOCOLON;
","			return COMMA;
"["			return LBRACKET;
"]"			return RBRACKET;
"("			return LPARANTHES;
")"			return RPARANTHES;



// match Numbers todo: return the literal string or number
[0-9]+										return INTLITERAL;
0[xX][0-9a-fA-F]+							return INTLITERAL;
[0-9]+\.?[0-9]*([Ee][-+][0-9]+)?			return DOUBLELITERAL;
\"(\\.|[^"\\])*\"							return STRINGLITERAL;
(true|false)								return BOOLEANLITERAL;


// any other case is an error
.  				return ERR;

%% 
