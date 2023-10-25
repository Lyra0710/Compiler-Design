same_nodes = []
diff_nodes = []


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

        # Iterate through each character in the source code and accordingly classify
        for char in source_code:
            # Check if the character is a space and not inside a string
            if char.isspace() and not in_string:
                if current_token:
                    tokens.append(current_token)  # Append the current token to the list
                current_token = ""  # Reset the current token

            # Check if the character is a special character and not inside a string
            elif char in "();{}[]":
                if current_token:
                    tokens.append(current_token)  # Append the current token to the list
                tokens.append(char)  # Append the special character
                current_token = ""  # Reset the current token
            
            # Check if the character is the start or end of a string literal
            elif char == '"':
                if in_string:
                    current_token += char  # Add the character to the current token
                    in_string = False  # End the string
                else:
                    in_string = True  # Start a new string
                    current_token += char  # Add the character to the current token

            # Just add character to token if none of the above conditions are met
            else:
                current_token += char  # Add the character to the current token

        # Append the last token if it exists
        if current_token:
            tokens.append(current_token)  # Append the last token

        # Return the list of tokens
        return tokens

    # Tokenize the source code
    tokens = tokenize(source_code)  # Tokenize the source code

    # Iterate through each token and classify into node groups
    for token in tokens:
        # If token is a bracket
        if token in "(){}[];":
            continue
        
        # If token is a ControlFlow keyword
        elif token in ["if", "else", "for", "while", "def"]:
            new_node = Node("ControlFlow", children=[], value=token)

        # If token is an operator
        elif token in ["+", "-", "*", "/", "=", "==", "!="]:
            new_node = Node("Operator", children=[], value=token)

        # If token is a string literal
        elif token.startswith('"') and token.endswith('"'):
            new_node = Node("String", children=[], value=token)

        # If token is a potential variable
        elif token.isalpha():
            new_node = Node("Variable", children=[], value=token)
        
        # If the token is unidentified
        else:
            new_node = Node("Token", children=[], value=token)

        # Append node to the current node's children
        current_node.children.append(new_node)  # Add the new node as a child
        current_node = new_node  # Update the current node

    # Return the root of the AST
    return ast_root


def visualize_ast(node, indent=""):
    # Print the current node's type and value
    print(indent + f"{node.node_type}: {node.value}")

    # Recursively visualize the children nodes
    for child in node.children:
        visualize_ast(child, indent + "  ")


# Function to calculate custom AST similarity
def calculate_similarity(ast1, ast2):
    # Use global variables
    global same_nodes
    global diff_nodes

    # Check if both ast's exist
    if not ast1 or not ast2:
        return 0
    
    # Count identical nodes in the given ASTs
    count_identical_nodes(ast1, ast2)
    print(f"Identical Nodes: {len(same_nodes)}")

    # Count total nodes in each AST
    total_same = len(same_nodes)
    total_diff = len(diff_nodes)

    # Sum of the length of "same_nodes" and sum of the length of "diff_nodes" * 2
    print(f"Same Nodes: {len(same_nodes)}")
    print(f"Different Nodes: {len(diff_nodes)}")

    # Calculate similarity as a ratio of identical nodes to total nodes
    similarity = (total_same) / (total_same + total_diff)

    # return similarity
    return similarity


# Function to count identical nodes in the ASTs
def count_identical_nodes(node1, node2):
    # Use global variables
    global same_nodes
    global diff_nodes

    # Check node type before proceeding
    print(node1.node_type, node2.node_type)
        
    # Check if the node types are the same or different
    if node1.node_type != node2.node_type:
        diff_nodes.append((node1.node_type, node2.node_type))
    else: 
        same_nodes.append((node1.node_type, node2.node_type))

    # Recursively count identical nodes in the children
    for child1, child2 in zip(node1.children, node2.children):
        count_identical_nodes(child1, child2)


# Function to read source code from files
def read_source_code_from_files(model_file, student_file):
    # Read the model answer from the file
    with open(model_file, 'r') as model:
        model_source = model.read()  
        print("Model Source: ", model_source[0:5])

    # Read the student's submission from the file
    with open(student_file, 'r') as student:
        student_source = student.read()
        print("Student Source: ", student_source[0:5])  

    # Return values
    return model_source, student_source


# Main function
def main():
    # Take inputs
    # model_file = input("Enter the path to the model answer file: ")
    # student_file = input("Enter the path to the student's submission file: ")
    model_file = input("Enter the path to file 1: ")
    student_file =  input("Enter the path to the student's submission file 2: ")


    # Read source code from files
    model_source, student_source = read_source_code_from_files(model_file, student_file)

    # Parse source code into ASTs
    model_ast = parse_to_ast(model_source)
    student_ast = parse_to_ast(student_source)

    # Visualize both ASTs
    print("\nModel AST: ")
    visualize_ast(model_ast)
    print("\nStudent AST: ")
    visualize_ast(student_ast)

    # Calculate similarity between the ASTs
    similarity = calculate_similarity(model_ast, student_ast)

    # Convert to a percentage
    similarity_percentage = similarity * 100  

    # Display the similarity percentage
    print(f"Percentage of similarity between the model answer and student's submission: {similarity_percentage:.2f}%")

# Main function
if __name__ == '__main__':
    main()