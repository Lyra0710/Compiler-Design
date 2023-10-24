# Define your custom AST node structure
class Node:
    def __init__(self, node_type, children=None, value=None):
        self.node_type = node_type
        self.children = children if children else []
        self.value = value

# Module 1: Function to parse Python source code into a custom AST
def parse_to_ast(source_code):
    # This is a very basic example; you can expand this as needed
    # For simplicity, we are tokenizing the source code into words
    tokens = source_code.split()
    # Creating a root node representing the entire code
    ast_root = Node("Code", children=[], value=None)

    # Iterate through tokens and create AST nodes (simplified example)
    current_node = ast_root
    for token in tokens:
        current_node.children.append(Node("Token", value=token))

    return ast_root

# Module 2: Function to calculate custom AST similarity
def calculate_similarity(ast1, ast2):
    # Your custom similarity calculation logic
    # This could involve tree traversal and comparing node structures

    def count_identical_nodes(node1, node2):
        if node1.node_type != node2.node_type:
            return 0
        count = 1
        for child1, child2 in zip(node1.children, node2.children):
            count += count_identical_nodes(child1, child2)
        return count

    total_nodes = count_identical_nodes(ast1, ast2)
    total_nodes1 = len(ast1.children)
    total_nodes2 = len(ast2.children)
    
    similarity = (2.0 * total_nodes) / (total_nodes1 + total_nodes2)

    return similarity

# Module 3: Function to read source code from files
def read_source_code_from_files(model_file, student_file):
    with open(model_file, 'r') as model:
        model_source = model.read()
    with open(student_file, 'r') as student:
        student_source = student.read()
    return model_source, student_source

# Module 4: Main function
def main():
    model_file = input("Enter the path to the model answer file: ")
    student_file = input("Enter the path to the student's submission file: ")

    model_source, student_source = read_source_code_from_files(model_file, student_file)
    model_ast = parse_to_ast(model_source)
    student_ast = parse_to_ast(student_source)

    similarity = calculate_similarity(model_ast, student_ast)
    similarity_percentage = similarity * 100  # Convert to percentage
    if similarity_percentage > 100:
        similarity_percentage = 100.0
    print(f"Percentage of similarity between the model answer and student's submission: {similarity_percentage:.2f}%")

if __name__ == '__main__':
    main()