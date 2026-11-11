%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *message);
%}

%define parse.error verbose

%token NUM ID
%left '+'
%left '*'

%%

expression:
      expression '+' expression
    | expression '*' expression
    | '(' expression ')'
    | NUM
    | ID
    ;

%%

int main(void)
{
    printf("Enter an arithmetic expression: ");
    if (yyparse() == 0) {
        printf("Expression is valid.\n");
        return 0;
    }
    return 1;
}
 
void yyerror(const char *message)
{
    fprintf(stderr, "Invalid expression: %s\n", message);
}
