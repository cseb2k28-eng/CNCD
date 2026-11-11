%{
#include "y.tab.h"
#include <stdlib.h>
%}

%option noyywrap noinput nounput

%%

[0-9]+      { yylval.val = atoi(yytext); return NUMBER; }
[ \t\r]+    ;
\n          { return '\n'; }
[+\-*/()]   { return yytext[0]; }
.           { return yytext[0]; }

%%
