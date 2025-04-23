%{
#include <stdio.h>
#include <string.h>
%}

%%
"int"       { printf("KEYWORD: %s\n", yytext); }
"float"     { printf("KEYWORD: %s\n", yytext); }
"char"      { printf("KEYWORD: %s\n", yytext); }
"if"        { printf("KEYWORD: %s\n", yytext); }
"else"      { printf("KEYWORD: %s\n", yytext); }
"while"     { printf("KEYWORD: %s\n", yytext); }
"for"       { printf("KEYWORD: %s\n", yytext); }
"return"    { printf("KEYWORD: %s\n", yytext); }

[0-9]+      { printf("INTEGER: %s\n", yytext); }
[0-9]+\.[0-9]+ { printf("FLOAT: %s\n", yytext); }

[a-zA-Z][a-zA-Z0-9_]* { printf("IDENTIFIER: %s\n", yytext); }

"+"         { printf("OPERATOR: %s\n", yytext); }
"-"         { printf("OPERATOR: %s\n", yytext); }
"*"         { printf("OPERATOR: %s\n", yytext); }
"/"         { printf("OPERATOR: %s\n", yytext); }
"="         { printf("OPERATOR: %s\n", yytext); }
"=="        { printf("OPERATOR: %s\n", yytext); }
">"         { printf("OPERATOR: %s\n", yytext); }
"<"         { printf("OPERATOR: %s\n", yytext); }
">="        { printf("OPERATOR: %s\n", yytext); }
"<="        { printf("OPERATOR: %s\n", yytext); }
"!="        { printf("OPERATOR: %s\n", yytext); }
"&&"        { printf("OPERATOR: %s\n", yytext); }
"||"        { printf("OPERATOR: %s\n", yytext); }

";"         { printf("PUNCTUATION: %s\n", yytext); }
","         { printf("PUNCTUATION: %s\n", yytext); }
"("         { printf("PUNCTUATION: %s\n", yytext); }
")"         { printf("PUNCTUATION: %s\n", yytext); }
"{"         { printf("PUNCTUATION: %s\n", yytext); }
"}"         { printf("PUNCTUATION: %s\n", yytext); }
"["         { printf("PUNCTUATION: %s\n", yytext); }
"]"         { printf("PUNCTUATION: %s\n", yytext); }

\".*\"      { printf("STRING: %s\n", yytext); }
\'.\' 	     { printf("CHARACTER: %s\n", yytext); }

\/\/.*      { printf("COMMENT: %s\n", yytext); }

[ \t\n]+    { /* Ignore whitespace */ }
.           { printf("UNKNOWN: %s\n", yytext); }
%%

int main()
{
    printf("Enter code (press Ctrl+D on Unix/Linux or Ctrl+Z on Windows to end input):\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}