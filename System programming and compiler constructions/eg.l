%{
#include <stdio.h>
%}

%%
[aeiouAEIOU]    { printf("Input character is a VOWEL\n"); }
[a-zA-Z]        { printf("Input character is a CONSONANT\n"); }
.               { printf("Input is not an alphabet\n"); }
%%

int main()
{
    printf("Enter a character: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
