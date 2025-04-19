class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree(tokens):
    stack = []
    op_codes = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}
    for token in tokens:
        if token in op_codes:
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(op_codes[token], left, right)
            stack.append(node)
        else:
            stack.append(TreeNode(int(token)))
    return stack[0]


def evaluate_tree(node):
    if node.left is None and node.right is None:
        return node.value
    l_val = evaluate_tree(node.left)
    r_val = evaluate_tree(node.right)
    if node.value == -1:
        return l_val + r_val
    elif node.value == -2:
        return l_val - r_val
    elif node.value == -3:
        return l_val * r_val
    elif node.value == -4:
        return l_val // r_val
    elif node.value == -5:
        return l_val % r_val
    elif node.value == -6:
        return l_val ** r_val
    else:
        raise ValueError("Неизвестная операция: " + str(node.value))


def transform_tree(node):
    if node.left is None and node.right is None:
        return node, False

    left_new, left_has_div = transform_tree(node.left)
    right_new, right_has_div = transform_tree(node.right)

    current_has_div = node.value in (-4, -5)
    subtree_has_div = current_has_div or left_has_div or right_has_div

    if subtree_has_div:
        new_subtree = TreeNode(node.value, left_new, right_new)
        value = evaluate_tree(new_subtree)
        return TreeNode(value), True
    else:
        return TreeNode(node.value, left_new, right_new), False


def main():
    with open("filename", "r") as f:
        tokens = f.read().strip().split()
    tree = build_tree(tokens)
    transformed_tree, _ = transform_tree(tree)
    print("Указатель на корень нового дерева:", transformed_tree)


if __name__ == "__main__":
    main()
