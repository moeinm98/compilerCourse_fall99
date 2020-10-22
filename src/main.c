#include <stdio.h>
#include "scanner.h"


extern int yylex();

extern char* yytext;
extern FILE *yyin, *yyout;


int main(int argc, char* argv[])
{

    char *input_file = argv[2];
    char *output_file = argv[4];

    yyin = fopen(input_file, "r");
    yyout = fopen(output_file, "w");

    int ntoken, vtoken;
    ntoken = yylex();
    while(ntoken > 0) {
        switch (ntoken){
            case IDENTIFIER:
                fprintf(yyout, "T_ID %s\n",  yytext);
                break;
            case INTLITERAL:
                fprintf(yyout, "T_INTLITERAL %s\n", yytext);
                break;
            case DOUBLELITERAL:
                fprintf(yyout, "T_DOUBLELITERAL %s\n", yytext);
                break;
            case STRINGLITERAL:
                fprintf(yyout, "T_STRINGLITERAL %s\n", yytext);
                break;
            case BOOLEANLITERAL:
                fprintf(yyout, "T_BOOLEANLITERAL %s\n", yytext);
                break;
            default:
                fprintf(yyout, "%s\n", yytext);


        }

        ntoken = yylex();

    }
    if (ntoken == -1)
    {
        fprintf(yyout, "UNDEFINED_TOKEN");
    }

    return 0;
}
