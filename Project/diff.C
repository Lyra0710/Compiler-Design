#include <stdio.h>
#include <string.h>

int countLines(char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found.\n");
        return -1;  // Indicates an error
    }
    
    int line_count = 0;
    char ch;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            line_count++;
        }
    }
    
    fclose(file);
    return line_count;
}

double calculateSimilarity(const char *file1, const char *file2) {
    FILE *model = fopen(file1, "r");
    FILE *student = fopen(file2, "r");
    
    if (model == NULL || student == NULL) {
        printf("Error opening files.\n");
        return -1.0;  // Indicates an error
    }
    
    // Read file contents into strings
    char model_source[10000];  // Adjust the size as needed
    char student_source[10000];  // Adjust the size as needed
    memset(model_source, 0, sizeof(model_source));
    memset(student_source, 0, sizeof(student_source));
    
    fread(model_source, 1, sizeof(model_source), model);
    fread(student_source, 1, sizeof(student_source), student);
    
    fclose(model);
    fclose(student);
    
    // Perform similarity comparison (you would need to implement this logic)
    double similarity = 0.0;  // Implement similarity calculation
    
    return similarity;
}

int main() {
    char model_file[256];
    char student_file[256];
    
    printf("Enter the path to the model answer file: ");
    scanf("%255[^\n]", model_file);
    
    // Clear the newline character from the input buffer
    while (getchar() != '\n');
    
    printf("Enter the path to the student's submission file: ");
    scanf("%255[^\n]", student_file);
    
    int line_count = countLines(model_file);
    if (line_count >= 0) {
        printf("Number of lines in the file: %d\n", line_count);
    }
    
    double similarity = calculateSimilarity(model_file, student_file);
    if (similarity >= 0) {
        printf("Similarity between the model answer and student's submission: %lf\n", similarity);
    }
    
    return 0;
}
