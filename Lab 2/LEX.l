// Write a LEX program to find if a given number is EVEN or ODD

%{
#include <stdio.h>
%}

%%

[0-9]+ {
    int num = atoi(yytext); // Convert the matched text to an integer
    if (num % 2 == 0) {
        printf("%d is EVEN\n", num);
    } else {
        printf("%d is ODD\n", num);
    }
}

\n { /* Do nothing for newline characters */ }

. { /* Handle any other characters as an error */ }

%%

int main() {
    yylex();
    return 0;
}

