class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # Если это лист, просто выводим значение
        if self.left is None and self.right is None:
            return str(self.value)
        # Отображаем символ операции по заданному коду
        op_symbols = {-1: '+', -2: '-', -3: '*', -4: '/', -5: '%', -6: '^'}
        op = op_symbols.get(self.value, self.value)
        return f"({repr(self.left)} {op} {repr(self.right)})"


def build_tree(tokens):
    stack = []
    op_codes = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}
    for token in tokens:
        if token in op_codes:
            # Извлекаем два последних узла (правый и левый операнды)
            right = stack.pop()
            left = stack.pop()
            node = Node(op_codes[token], left, right)
            stack.append(node)
        else:
            # Если токен – число, создаём листовой узел
            stack.append(Node(int(token)))
    # В стеке остаётся единственный элемент – корень дерева
    return stack[0]


# Функция вычисления значения поддерева
def evaluate_tree(node):
    if node.left is None and node.right is None:
        return node.value
    # Рекурсивно вычисляем значения левого и правого поддеревьев
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


# Функция преобразования дерева:
# Если в поддереве встречается операция деления (/ или %), вычисляем значение поддерева
# и заменяем его листовым узлом с этим значением.
def transform_tree(node):
    if node.left is None and node.right is None:
        # Листовой узел не содержит операций
        return node, False

    # Рекурсивно преобразуем левое и правое поддеревья
    left_new, left_has_div = transform_tree(node.left)
    right_new, right_has_div = transform_tree(node.right)

    # Флаг, указывающий, является ли текущий оператор операцией деления или взятия остатка
    current_has_div = node.value in (-4, -5)
    # Если в текущем узле или в одном из его поддеревьев встречается операция деления/остатка
    subtree_has_div = current_has_div or left_has_div or right_has_div

    if subtree_has_div:
        # Собираем новый узел с преобразованными поддеревьями, чтобы корректно вычислить значение
        new_subtree = Node(node.value, left_new, right_new)
        value = evaluate_tree(new_subtree)
        # Возвращаем замену на листовой узел с вычисленным значением.
        return Node(value), True
    else:
        # Если преобразования не требовалось, возвращаем узел с обновлёнными поддеревьями.
        return Node(node.value, left_new, right_new), False


def main():
    with open("filename", "r") as f:
        tokens = f.read().strip().split()

    # Построение дерева по ОПЗ
    tree = build_tree(tokens)
    transformed_tree, _ = transform_tree(tree)
    print("Корень преобразованного дерева:", transformed_tree)


if __name__ == "__main__":
    main()
