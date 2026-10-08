%{
#include <stdio.h>
int yylex();
void yyerror(char *s);
void yy_scan_string(const char *str);
%}

%token ID

%%

E : E '+' T
  | E '-' T
  | T
  ;

T : T '*' F
  | T '/' F
  | F
  ;

F : '(' E ')'
  | ID
  ;

%%

void yyerror(char *s)
{
    printf("Invalid Expression\n");
}

int main()
{
    char input[100];
    printf("Enter arithmetic expression: ");

    if (fgets(input, sizeof(input), stdin))
    {
        yy_scan_string(input);
        if (yyparse() == 0)
            printf("Valid Expression\n");
    }

    return 0;
}

/* run : .\w6_2.exe */