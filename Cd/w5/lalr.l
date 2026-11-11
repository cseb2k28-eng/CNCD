%{
#include "y.tab.h"
%}

%option noyywrap noinput nounput

%%

[0-9]+                  { return NUM; }
[a-zA-Z_][a-zA-Z0-9_]*  { return ID; }
[ \t\r\n]+              ;
[+*()]                  { return yytext[0]; }
.                       { return yytext[0]; }

%%
