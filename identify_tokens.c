// Write a python program that takes in another C program as input, tokenizes it and returns which are keywords, identifiers, operators, special symbols, etc.

// This code does not produce the desired output. There are some errors. Please refer to the .py file
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TOKENS 1000
#define MAX_IDENTIFIER_LENGTH 100
#define MAX_CONSTANT_LENGTH 100

int main() {
    char *keywords[] = {"auto", "break", /* Add all keywords here */};
    char *operators[] = {"+", "-", "*", "/", /* Add all operators here */};
    char *special_symbols[] = {",", ";", "(", ")", "{", "}", "[", "]"};
    
    char *identifiers[MAX_TOKENS];
    char *constants[MAX_TOKENS];
    char *tokens[MAX_TOKENS];
    
    char line[1024]; // Assuming a maximum line length of 1024 characters
    size_t len;
    
    int i = 0, n_identifiers = 0, n_constants = 0;
    
    FILE *fp = fopen("Hello.c", "r");
    
    if (fp == NULL) {
        printf("Error opening file\n");
        exit(EXIT_FAILURE);
    }
    
    while (fgets(line, sizeof(line), fp) != NULL) {
        char *token = strtok(line, " \t\n");
        
        while (token != NULL) {
            tokens[i++] = token;
            token = strtok(NULL, " \t\n");
        }
    }
    
    for (int j = 0; j < i; j++) {
        char *token = tokens[j];
        
        int is_keyword = 0, is_operator = 0, is_special_symbol = 0, is_identifier = 0, is_constant = 0;
        
        // Check if token is a keyword
        for (int k = 0; k < sizeof(keywords) / sizeof(keywords[0]); k++) {
            if (strcmp(token, keywords[k]) == 0) {
                is_keyword = 1;
                break;
            }
        }
        
        // Check if token is an operator
        for (int k = 0; k < sizeof(operators) / sizeof(operators[0]); k++) {
            if (strcmp(token, operators[k]) == 0) {
                is_operator = 1;
                break;
            }
        }
        
        // Check if token is a special symbol
        for (int k = 0; k < sizeof(special_symbols) / sizeof(special_symbols[0]); k++) {
            if (strcmp(token, special_symbols[k]) == 0) {
                is_special_symbol = 1;
                break;
            }
        }
        
        // Check if token is an identifier or a constant
        if (!is_keyword && !is_operator && !is_special_symbol) {
            if (isalpha(token[0]) || token[0] == '_') {
                is_identifier = 1;
                identifiers[n_identifiers++] = token;
            } else if (isdigit(token[0])) {
                is_constant = 1;
                constants[n_constants++] = token;
            }
        }
        
        // Print the token's classification
        if (is_keyword) {
            printf("%s is a keyword\n", token);
        } else if (is_operator) {
            printf("%s is an operator\n", token);
        } else if (is_special_symbol) {
            printf("%s is a special symbol\n", token);
        } else if (is_identifier) {
            printf("%s is an identifier\n", token);
        } else if (is_constant) {
            printf("%s is a constant\n", token);
        }
    }
    
    printf("Identifiers: ");
    for (int j = 0; j < n_identifiers; j++) {
        printf("%s ", identifiers[j]);
    }
    printf("\n");
    
    printf("Constants: ");
    for (int j = 0; j < n_constants; j++) {
        printf("%s ", constants[j]);
    }
    printf("\n");
    
    fclose(fp);
    
    return 0;
}
