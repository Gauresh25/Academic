%{
#include <stdio.h>
int char_count = 0;
int word_count = 0;
int line_count = 0;
%}

%%
\n          { line_count++; char_count++; }
[a-zA-Z]+   { word_count++; char_count += yyleng; }
.           { char_count++; }
%%

int main()
{
    printf("Enter text (press Ctrl+D on Unix/Linux or Ctrl+Z on Windows to end input):\n");
    yylex();

    printf("\nCounting Results:\n");
    printf("Number of lines: %d\n", line_count);
    printf("Number of words: %d\n", word_count);
    printf("Number of characters: %d\n", char_count);

    return 0;
}

int yywrap()
{
    return 1;
}