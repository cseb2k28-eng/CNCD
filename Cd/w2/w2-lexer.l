%{
#include <stdio.h>
%}

%%

"int"|"float"|"char"|"if"|"else"|"while"|"return" { printf("%s -> Keyword\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("%s -> Identifier\n", yytext); }

[0-9]+ { printf("%s -> Constant\n", yytext); }

"+"|"-"|"*"|"/"|"=" { printf("%s -> Operator\n", yytext); }

";"|","|"("|")"|"{"|"}" { printf("%s -> Special Symbol\n", yytext); }

[ \t\n]+ { /* Ignore spaces and newlines */ }

. { printf("%s -> Invalid\n", yytext); }

%%

int main()
{
    printf("Enter input:\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}

/* run : .\w2.exe */
