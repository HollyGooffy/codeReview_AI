class Node:
    def __init__(self, value):
        self.value = value  # Значение узла (число или код операции)
        self.left = None
        self.right = None

    # Функция построения дерева из выражения в обратной польской записи


def build_rpn_tree(tokens):
    stack = []  # Стек для построения дерева

    for token in tokens:
        if token.isdigit():  # Если токен - число
            stack.append(Node(int(token)))  # Создаем узел с числом и добавляем в стек
        else:  # Если токен - операция
            # Преобразуем символ операции в числовой код
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

            # Создаем узел операции
            node = Node(op)
            # Берем два последних числа из стека (для бинарных операций)
            node.right = stack.pop()
            node.left = stack.pop()
            # Помещаем узел операции обратно в стек
            stack.append(node)

    return stack[0]  # Корень дерева остается в стеке


# Функция вычисления значения поддерева
def evaluate(node):
    if node.value >= 0:  # Если узел - число (не операция)
        return node.value

    # Рекурсивно вычисляем значения левого и правого поддеревьев
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    # Выполняем соответствующую операцию
    if node.value == -1:  # Сложение
        return left_val + right_val
    elif node.value == -2:  # Вычитание
        return left_val - right_val
    elif node.value == -3:  # Умножение
        return left_val * right_val
    elif node.value == -4:  # Целочисленное деление
        return left_val // right_val
    elif node.value == -5:  # Остаток от деления
        return left_val % right_val
    elif node.value == -6:  # Возведение в степень
        return left_val ** right_val


# Функция замены операций деления и остатка на их значения
def replace_div_mod(node):
    if node is None:  # Базовый случай рекурсии
        return None

    # Если текущая операция - деление или остаток
    if node.value == -4 or node.value == -5:
        value = evaluate(node)  # Вычисляем значение поддерева
        return Node(value)  # Заменяем на узел с вычисленным значением

    # Рекурсивно обрабатываем левое и правое поддеревья
    node.left = replace_div_mod(node.left)
    node.right = replace_div_mod(node.right)
    return node


def print_tree(node, level=0):
    if node is not None:
        # Сначала правое поддерево (будет выше при печати)
        print_tree(node.right, level + 1)
        # Отступы для визуализации уровней
        print(' ' * 4 * level + '->', node.value)
        # Затем левое поддерево (будет ниже при печати)
        print_tree(node.left, level + 1)


def main():
    filename = input("Введите имя файла: ")
    try:
        with open(filename, 'r') as file:
            # Читаем выражение из файла и разбиваем на токены
            expression = file.read().strip()
            tokens = expression.split()

            # Строим исходное дерево
            root = build_rpn_tree(tokens)
            print("Исходное дерево:")
            print_tree(root)

            # Заменяем операции деления и остатка
            new_root = replace_div_mod(root)
            print("\nДерево после замены операций деления и остатка:")
            print_tree(new_root)

            # Выводим указатель на корень нового дерева
            print("\nУказатель на корень нового дерева:", new_root)

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
