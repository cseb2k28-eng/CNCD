%{
#include <stdio.h>
%}

%x COMMENT
%option noyywrap noinput nounput

%%

"//"[^\r\n]* { }
"/*" { BEGIN(COMMENT); }
<COMMENT>"*/" { BEGIN(INITIAL); }
<COMMENT>\n { }
<COMMENT>\r { }
<COMMENT>. { }
<COMMENT><<EOF>> { fprintf(stderr, "Unterminated block comment\n"); return 0; }

"int"|"float"|"char"|"if"|"else"|"while"|"return" { printf("%s -> Keyword\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("%s -> Identifier\n", yytext); }

[0-9]+ { printf("%s -> Constant\n", yytext); }

"+"|"-"|"*"|"/"|"=" { printf("%s -> Operator\n", yytext); }

";"|","|"("|")"|"{"|"}" { printf("%s -> Special Symbol\n", yytext); }

[ \t\r\n]+ { }

. { printf("%s -> Invalid\n", yytext); }

%%

int main()
{
    printf("Enter input:\n");
    yylex();
    return 0;
}
