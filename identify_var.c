// Including the header files
#include <stdio.h> 
#include <stdbool.h>
#include <string.h>

// Defining the main function
int main() {
    // Defining the input code
    const char *code = "printf(\"Variables are %d,%d,%f, %c\", v1, v2, v3);";

    // Variable Declaration to keep count of variable formats
    int intVarCount = 0;
    int floatVarCount = 0;
    int charVarCount = 0;
    
    // If the code is inside double quotes or not
    bool insideQuotes = false;
    bool intSpecifierFound = false;
    bool floatSpecifierFound = false;
    bool charSpecifierFound = false;

    // Start parsing after the first double quote
    // The strchr function finds the position of the first double quote in the string.
    // Then, the format string pointer is set to start within the printf statement.
    const char *formatString = strchr(code, '\"');
    if (formatString != NULL) {
        formatString++; // Move past the opening double quote

        // Loop through the format string and count the number of format specifiers
        for (int i = 0; formatString[i] != '\0'; i++) {
            char currentChar = formatString[i];

            //Inside the loop, this code checks for the presence of double quotes (") and toggles the insideQuotes flag. 
            // It considers escape sequences (backslash \) to avoid counting escaped double quotes within the string.
            if (currentChar == '\"' && (i == 0 || formatString[i - 1] != '\\')) {
                insideQuotes = !insideQuotes; // Toggle the insideQuotes flag when encountering double quotes
            }

            if (!insideQuotes && currentChar == '%') {
                if (formatString[i + 1] != '\0') {
                    char formatSpecifier = formatString[i + 1];
                    i++; // Skip the format specifier character

                    switch (formatSpecifier) {
                        case 'd':
                            intVarCount++;
                            intSpecifierFound = true;
                            break;
                        case 'f':
                            floatVarCount++;
                            floatSpecifierFound = true;
                            break;
                        case 'c':
                            charVarCount++;
                            charSpecifierFound = true;
                            break;
                    }
                }
            }
        }
    }

    printf("Number of integer variables: %d\n", intVarCount);
    printf("Number of float variables: %d\n", floatVarCount);
    printf("Number of character variables: %d\n", charVarCount);
    printf("Number of variables: %d\n", intVarCount + floatVarCount + charVarCount);
    printf("Format specifiers: %s%s%s\n",
           intSpecifierFound ? "%d " : "",
           floatSpecifierFound ? "%f " : "",
           charSpecifierFound ? "%c " : "");

    return 0;
}
