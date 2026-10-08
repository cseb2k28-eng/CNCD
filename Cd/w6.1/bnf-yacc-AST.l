%{
#include "y.tab.h"
%}
%option noyywrap

%%

[a-zA-Z] { yylval.value = yytext[0]; return ID; }
[+*()]   { return yytext[0]; }
[ \t\n]  ;
.        { return yytext[0]; }

%%