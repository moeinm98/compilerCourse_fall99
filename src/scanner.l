%option noyywrap
%option header-file="lex.yy.h"

%{
#include <stdio.h>
#include "scanner.h"

#define YY_DECL int yylex()
%}

%%

	/* skip whitespace */
[\n\t]+			; //ignore
[[:space:]]+	; //ignore


	/* skip comments */

"//".*										; //single lßine
[/][*][^*]*[*]+([^*/][^*]*[*]+)*[/]			; //multiple line



	/* match keywords */

"void"			return VOID;
"int"			return INT;
"double"		return DOUBLE;
"bool"			return BOOL;
"string"		return STRING;
"class"			return CLASS;
"interface"		return INTERFACE;
"null"			return TNULL;
"this"			return THIS;
"extends"		return EXTEND;
"implements"	return IMPLEMENTS;
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
"private"		return PRIVATE;
"protected"		return PROTECTED;
"public"		return PUBLIC;


	/* match booleans */
(true|false)								return BOOLEANLITERAL;


	/* match identifiers */

[a-zA-Z][a-zA-Z0-9_]*		return IDENTIFIER; //todo return the name of the identifier


	/*  match Operators */
"+"			return PLUS;
"-"			return MINUS;
"*"			return STAR;
"/"			return SLASH;
"%"			return PERCENT;

">"			return GREATER;
"<"			return LESS;
"<="		return GREATEREQ;
">="		return LESSEQ;
"="			return EQUAL;
"=="		return EQUALEQ;
"!="		return NOTEQUAL;
"||"		return OR;
"&&"		return AND;
"!"			return NOT;
";"			return SEMOCOLON;
","			return COMMA;
"["			return LBRACKET;
"]"			return RBRACKET;
"("			return LPARANTHES;
")"			return RPARANTHES;
"{"			return LEFTCURLY;
"}"			return RIGHTCURLY;
"."  			return DOT;



	/* match Numbers todo: return the literal string or number */
[0-9]+										return INTLITERAL;
0[xX][0-9a-fA-F]+							return INTLITERAL;
[0-9]+\.?[0-9]*([Ee][-+]?[0-9]+)?			return DOUBLELITERAL;
\"(\\.|[^"\\])*\"							return STRINGLITERAL;



	/* any other case is an error */
.  				return ERR;

%% 
