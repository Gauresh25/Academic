%{
#include <stdio.h>
%}

%%
^[0-9]+$        { printf("Input is a NUMBER\n"); }
^[a-zA-Z]+$     { printf("Input is a WORD\n"); }
^[a-zA-Z0-9]+$  { printf("Input is a mixture of letters and digits\n"); }
.+              { printf("Input contains special characters\n"); }
%%

int main()
{
    printf("Enter a string: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}