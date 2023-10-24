#include <stdio.h>
#include <string.h>

// Define your custom AST node structure
struct Node {
    char node_type[100];
    struct Node* children[100];
    char value[100];
};

// Module 1: Function to parse Python source code into a custom AST
struct Node* parse_to_ast(char* source_code) {
    int i = 0;
    char* token = strtok(source_code, " ");
    // Creating a root node representing the entire code
    struct Node* ast_root = (struct Node*)malloc(sizeof(struct Node));
    strcpy(ast_root->node_type, "Code");

    // Iterate through tokens and create AST nodes (simplified example)
    struct Node* current_node = ast_root;
    while (token != NULL) {
        struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
        strcpy(new_node->node_type, "Token");
        strcpy(new_node->value, token);
        current_node->children[i] = new_node;
        i++;
        token = strtok(NULL, " ");
    }

    return ast_root;
}

// Module 2: Function to calculate custom AST similarity
float calculate_similarity(struct Node* ast1, struct Node* ast2) {
    // Your custom similarity calculation logic
    // This could involve tree traversal and comparing node structures
    
    int count_identical_nodes(struct Node* node1, struct Node* node2) {
        if (strcmp(node1->node_type, node2->node_type) != 0) {
            return 0;
        }
        int count = 1;
        for (int i = 0; i < 100; i++) {
            if (node1->children[i] && node2->children[i]) {
                count += count_identical_nodes(node1->children[i], node2->children[i]);
            }
        }
        return count;
    }

    int total_nodes = count_identical_nodes(ast1, ast2);
    int total_nodes1 = 0;
    int total_nodes2 = 0;
    for (int i = 0; i < 100; i++) {
        if (ast1->children[i]) {
            total_nodes1++;
        }
        if (ast2->children[i]) {
            total_nodes2++;
        }
    }

    float similarity = (2.0 * total_nodes) / (total_nodes1 + total_nodes2);

    return similarity;
}

// Module 3: Function to read source code from files
void read_source_code_from_files(char* model_file, char* student_file, char* model_source, char* student_source) {
    FILE *model, *student;
    model = fopen(model_file, "r");
    student = fopen(student_file, "r");
    fgets(model_source, 1000, model);
    fgets(student_source, 1000, student);
    fclose(model);
    fclose(student);
}

// Module 4: Main function
int main() {
    char model_file[100], student_file[100];
    char model_source[1000], student_source[1000];
    printf("Enter the path to the model answer file: ");
    scanf("%s", model_file);
    printf("Enter the path to the student's submission file: ");
    scanf("%s", student_file);

    read_source_code_from_files(model_file, student_file, model_source, student_source);
    struct Node* model_ast = parse_to_ast(model_source);
    struct Node* student_ast = parse_to_ast(student_source);

    float similarity = calculate_similarity(model_ast, student_ast);
    float similarity_percentage = similarity * 100;  // Convert to percentage
    if (similarity_percentage > 100) {
        similarity_percentage = 100.0;
    }
    printf("Percentage of similarity between the model answer and student's submission: %.2f%%\n", similarity_percentage);

    return 0;
}