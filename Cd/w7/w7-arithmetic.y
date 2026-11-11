%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *message);
%}

%union {
    int val;
}

%token <val> NUMBER
%type <val> expr

%left '+' '-'
%left '*' '/'

%%

input:
    expr '\n' { printf("Result = %d\n", $1); }
    ;

expr:
      expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr {
          if ($3 == 0) {
              printf("Cannot divide by zero\n");
              YYABORT;
          }
          $$ = $1 / $3;
      }
    | '(' expr ')' { $$ = $2; }
    | NUMBER        { $$ = $1; }
    ;

%%

int main(void)
{
    printf("Enter expression: ");
    return yyparse();
}

void yyerror(const char *message)
{
    (void)message;
    printf("Invalid expression\n");
}
