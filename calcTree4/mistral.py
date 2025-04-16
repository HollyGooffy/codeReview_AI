class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def read_expression_from_file(filename):
    with open(filename, 'r') as file:
        expression = file.read().strip().split()
    return expression

def build_tree(expression):
    stack = []
    operators = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}

    for token in expression:
        if token in operators:
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(operators[token])
            node.left = left
            node.right = right
            stack.append(node)
        else:
            stack.append(TreeNode(int(token)))

    return stack[0]

def evaluate_tree(node):
    if node.value >= 0:
        return node.value

    left_value = evaluate_tree(node.left)
    right_value = evaluate_tree(node.right)

    if node.value == -1:
        return left_value + right_value
    elif node.value == -2:
        return left_value - right_value
    elif node.value == -3:
        return left_value * right_value
    elif node.value == -4:
        return left_value // right_value
    elif node.value == -5:
        return left_value % right_value
    elif node.value == -6:
        return left_value ** right_value

def transform_tree(node):
    if node is None:
        return None

    if node.value in [-4, -5]:
        return TreeNode(evaluate_tree(node))

    node.left = transform_tree(node.left)
    node.right = transform_tree(node.right)

    return node

def print_tree(node):
    if node is None:
        return "None"
    return f"{node.value} ({print_tree(node.left)}, {print_tree(node.right)})"

def main(filename):
    expression = read_expression_from_file(filename)
    root = build_tree(expression)
    transformed_root = transform_tree(root)
    print(print_tree(transformed_root))

if __name__ == "__main__":
    filename = 'filename'  # Замените на имя вашего файла
    main(filename)
