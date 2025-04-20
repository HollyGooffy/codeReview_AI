"""За основу взята версия deepseek"""
"""
 В текстовом файле с именем filename дано арифметическое выражение в
 обратной польской записи. Операндами в выражении являются целые числа из
 промежутка от 0 до 9. Используемые операции: сложение (+), вычитание (-), умножение
 (*), деление нацело (/) и целочисленный остаток от деления (%) и возведение в степень (^).
 Постройте дерево, соответствующее данному выражению. Знаки операций кодируйте
 числами: сложение (-1), вычитание (-2), умножение (-3), деление нацело (-4),
 целочисленный остаток от деления (-5), возведение в степень (-6). Преобразуйте дерево
 так, чтобы в нем не было операции деления Иными словами, замените поддеревья, в
 которых есть операции / или %, значением данного поддерева. Выведите указатель на
 корень полученного дерева.
 """
class Node:
    def __init__(self, value):
        """Инициализирует узел с заданным значением."""
        self.value = value
        self.left = None
        self.right = None

def build_rpn_tree(tokens):
    stack = []

    for token in tokens:
        if token.isdigit():  # Если токен - число
            stack.append(Node(int(token)))
        else:  # Если токен - операция
            if token == '+':
                op = -1
            elif token == '-':
                op = -2
            elif token == '*':
                op = -3
            elif token == '/':
                op = -4
            elif token == '%':
                op = -5
            elif token == '^':
                op = -6
            else:
                raise ValueError(f"Неизвестный оператор: {token}")

            node = Node(op)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack[0]


def evaluate(node):
    if node.value >= 0:
        return node.value

    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    if node.value == -1:  # Сложение
        return left_val + right_val
    elif node.value == -2:
        return left_val - right_val
    elif node.value == -3:
        return left_val * right_val
    elif node.value == -4:
        return left_val // right_val
    elif node.value == -5:
        return left_val % right_val
    elif node.value == -6:
        return left_val ** right_val


def replace_div_mod(node):
    if node is None:
        return None

    if node.value in (-4, -5):
        value = evaluate(node)
        return Node(value)

    node.left = replace_div_mod(node.left)
    node.right = replace_div_mod(node.right)
    return node


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)


def main():
    filename = 'filename'
    try:
        with open(filename, 'r') as file:
            expression = file.read().strip()
            tokens = expression.split()

            root = build_rpn_tree(tokens)
            print("Исходное дерево:")
            print_tree(root)

            new_root = replace_div_mod(root)
            print("\nДерево после замены операций деления и остатка:")
            print_tree(new_root)

            print("\nУказатель на корень нового дерева:", new_root)

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()