%{
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    char value;
    struct Node *left;
    struct Node *right;
} Node;

Node* createNode(char value, Node *left, Node *right)
{
    Node *n = malloc(sizeof(Node));
    n->value = value;
    n->left = left;
    n->right = right;
    return n;
}

void printTree(Node *root, int level)
{
    int i;

    if (root == NULL)
        return;

    for (i = 0; i < level; i++)
        printf("  ");

    printf("%c\n", root->value);

    printTree(root->left, level + 1);
    printTree(root->right, level + 1);
}

int yylex();
void yyerror(char *s);
void yy_scan_string(const char *str);
Node *root;
%}

%code requires {
    typedef struct Node {
        char value;
        struct Node *left;
        struct Node *right;
    } Node;
}

%union {
    Node *node;
    char value;
}

%token <value> ID
%type <node> E T F

%%

E : E '+' T { $$ = createNode('+', $1, $3); root = $$; }
  | T        { $$ = $1; root = $$; }
  ;

T : T '*' F { $$ = createNode('*', $1, $3); }
  | F        { $$ = $1; }
  ;

F : ID       { $$ = createNode($1, NULL, NULL); }
  | '(' E ')' { $$ = $2; }
  ;

%%

void yyerror(char *s)
{
    printf("Invalid Expression\n");
}

int main()
{
    char input[100];
    printf("Enter expression: ");
    if (fgets(input, sizeof(input), stdin))
    {
        yy_scan_string(input);
        if (yyparse() == 0)
        {
            printf("Abstract Syntax Tree:\n");
            printTree(root, 0);
        }
    }
    return 0;
}

/* run: .\w6_1.exe */
/* input : a+b*c */