%{
#include "y.tab.h"
#include <stdlib.h>
%}

%option noyywrap noinput nounput

%%

[0-9]+(\.[0-9]*)?|\.[0-9]+  { yylval.number = strtod(yytext, NULL); return NUMBER; }
[+\-*/()]                    { return yytext[0]; }
[ \t\r\n]+                   ;
.                            { return yytext[0]; }

%%
