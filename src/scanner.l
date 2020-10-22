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

[a-zA-Z][a-zA-Z0-9_]*		return IDENTIFIER;

"+"			return PLUS;
"-"			return MINUS;
"*"			return STAR;
"/"			return SLASH;
"%"			return PERCENT;



// any other case is an error
.  				return ERR;

%% 
