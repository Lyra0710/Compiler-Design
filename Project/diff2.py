# Defining AST node structure
class Node:
    def __init__(self, node_type, children=None, value=None):
        self.node_type = node_type
        self.children = children if children else []  # Initialize an empty list for children
        self.value = value  # The value associated with the node

# Function to parse Python source code into a custom AST
def parse_to_ast(source_code):
    # Initialize the root of the Abstract Syntax Tree (AST)
    ast_root = Node("Code", children=[], value=None)
    current_node = ast_root  # Start at the root

    # Tokenization function to break the source code into meaningful tokens
    def tokenize(source_code):
        tokens = []  # A list to store the tokens
        current_token = ""  # A variable to accumulate characters for the current token
        in_string = False  # A flag to keep track of whether we are inside a string

        for char in source_code:
            if char.isspace() and not in_string:
                if current_token:
                    tokens.append(current_token)  # Append the current token to the list
                current_token = ""  # Reset the current token
            elif char in "();{}[]":
                if current_token:
                    tokens.append(current_token)  # Append the current token to the list
                tokens.append(char)  # Append the special character
                current_token = ""  # Reset the current token
            elif char == '"':
                if in_string:
                    current_token += char  # Add the character to the current token
                    in_string = False  # End the string
                else:
                    in_string = True  # Start a new string
                    current_token += char  # Add the character to the current token
            else:
                current_token += char  # Add the character to the current token

        if current_token:
            tokens.append(current_token)  # Append the last token

        return tokens

    tokens = tokenize(source_code)  # Tokenize the source code

    for token in tokens:
        if token in "(){}[];":
            continue
        elif token in ["if", "else", "for", "while", "def"]:
            new_node = Node("ControlFlow", children=[], value=token)
        elif token in ["+", "-", "*", "/", "=", "==", "!="]:
            new_node = Node("Operator", children=[], value=token)
        elif token.startswith('"') and token.endswith('"'):
            new_node = Node("String", children=[], value=token)
        elif token.isalpha():
            new_node = Node("Variable", children=[], value=token)
        else:
            new_node = Node("Token", children=[], value=token)

        current_node.children.append(new_node)  # Add the new node as a child
        current_node = new_node  # Update the current node

    return ast_root

# Function to calculate custom AST similarity
def calculate_similarity(ast1, ast2):
    # A recursive function to count identical nodes in the ASTs
    def count_identical_nodes(node1, node2):
        if node1.node_type != node2.node_type:
            return 0
        count = 1

        # Recursively count identical nodes in the children
        for child1, child2 in zip(node1.children, node2.children):
            count += count_identical_nodes(child1, child2)

        return count

    # Count identical nodes in the given ASTs
    identical_nodes = count_identical_nodes(ast1, ast2)

    # Count total nodes in each AST
    total_nodes1 = len(ast1.children)
    total_nodes2 = len(ast2.children)

    # Calculate similarity as a ratio of identical nodes to total nodes
    similarity = (identical_nodes) / (total_nodes1 + total_nodes2)

    return similarity

# Function to read source code from files
def read_source_code_from_files(model_file, student_file):
    with open(model_file, 'r') as model:
        model_source = model.read()  # Read the model answer from the file
    with open(student_file, 'r') as student:
        student_source = student.read()  # Read the student's submission from the file
    return model_source, student_source

# Main function
def main():
    model_file = input("Enter the path to the model answer file: ")
    student_file = input("Enter the path to the student's submission file: ")

    model_source, student_source = read_source_code_from_files(model_file, student_file)
    model_ast = parse_to_ast(model_source)
    student_ast = parse_to_ast(student_source)

    similarity = calculate_similarity(model_ast, student_ast)
    similarity_percentage = similarity * 100  # Convert to a percentage
    print(f"Percentage of similarity between the model answer and student's submission: {similarity_percentage:.2f}%")

if __name__ == '__main__':
    main()