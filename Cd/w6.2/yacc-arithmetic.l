%{
#include "y.tab.h"
%}
%option noyywrap

%%

[a-zA-Z0-9]+    { return ID; }
[+\-*/()]       { return yytext[0]; }
[ \t\n]         ;
.               { return yytext[0]; }

%%