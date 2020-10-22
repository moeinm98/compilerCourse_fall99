%option noyywrap
%option header-file="lex.yy.h"

%{
#include <iostream>

#define YY_DECL int yylex()
%}

%%

. /*ignore*/ ;

%% 
