%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *message);
typedef struct yy_buffer_state *YY_BUFFER_STATE;
YY_BUFFER_STATE yy_scan_string(const char *input);

static int division_by_zero;
%}

%union {
    double number;
}

%token <number> NUMBER
%type <number> expression

%left '+' '-'
%left '*' '/'
%precedence UMINUS

%%

input:
    expression { printf("Result: %g\n", $1); }
    ;

expression:
      NUMBER
    | expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression {
          if ($3 == 0.0) {
              division_by_zero = 1;
              YYABORT;
          }
          $$ = $1 / $3;
      }
    | '-' expression %prec UMINUS { $$ = -$2; }
    | '+' expression %prec UMINUS { $$ = $2; }
    | '(' expression ')' { $$ = $2; }
    ;

%%

void yyerror(const char *message)
{
    (void)message;
    if (!division_by_zero)
        fprintf(stderr, "Invalid arithmetic expression\n");
}

int main(void)
{
    char input[256];

    printf("Enter arithmetic expression: ");
    if (fgets(input, sizeof(input), stdin) == NULL)
        return 1;

    yy_scan_string(input);
    if (yyparse() != 0) {
        if (division_by_zero)
            fprintf(stderr, "Error: division by zero\n");
        return 1;
    }
    return 0;
}
