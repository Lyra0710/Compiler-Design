#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Function to calculate the similarity between two text files
double calculate_similarity(FILE *file1, FILE *file2) {
    char line1[1024], line2[1024];
    int common_lines = 0, total_lines = 0;

    while (fgets(line1, sizeof(line1), file1) != NULL && fgets(line2, sizeof(line2), file2) != NULL) {
        total_lines++;
        if (strcmp(line1, line2) == 0) {
            common_lines++;
        }
    }

    return (double)common_lines / total_lines;
}

int main() {
    char model_file_path[256];
    char student_file_path[256];
    char c;
    
    printf("Enter the path to the model answer file: ");
    scanf("%s", model_file_path);

    // Consume the newline character from the input buffer
    while ((c = getchar()) != '\n' && c != EOF);

    printf("Enter the path to the student's submission file: ");
    scanf("%s", student_file_path);

    FILE *model_file = fopen(model_file_path, "r");
    FILE *student_file = fopen(student_file_path, "r");

    if (model_file == NULL || student_file == NULL) {
        printf("Error: Unable to open files.\n");
        return 1;
    }

    double similarity = calculate_similarity(model_file, student_file);

    printf("Similarity between the model answer and student's submission: %.2f\n", similarity);

    fclose(model_file);
    fclose(student_file);

    // Now, add the code for counting lines
    char file_path[256];

    printf("Enter the path to the C code file: ");
    scanf("%s", file_path);

    FILE *file = fopen(file_path, "r");

    if (file == NULL) {
        printf("Error: Unable to open the file.\n");
        return 1;
    }

    int line_count = 0;
    char ch;

    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            line_count++;
        }
    }

    // Add 1 to count the last line
    line_count++;

    printf("Number of lines in the C code file: %d\n", line_count);

    fclose(file);

    return 0;
}
