def count_k_ary_numbers(k, n):
    def has_more_than_three_consecutive_zeros(number):
        """
        Вспомогательная функция для проверки, содержит ли строка
        более трех подряд идущих нулей.
        """
        count = 0
        for digit in number:
            if digit == '0':
                count += 1
                if count > 3:
                    return True
            else:
                count = 0
        return False

    count = 0
    max_number = k**n  # Максимальное число в K-ичной системе счисления длины N

    for i in range(max_number):
        k_ary_representation = ''
        num = i
        # Преобразование числа в K-ичную систему счисления
        for _ in range(n):
            k_ary_representation = str(num % k) + k_ary_representation
            num //= k
        # Проверка, содержит ли число более трех подряд идущих нулей
        if has_more_than_three_consecutive_zeros(k_ary_representation):
            count += 1

    return count

def main():
    """
    Основная функция для взаимодействия с пользователем через терминал.
    """
    print("Программа для нахождения количества K-ичных чисел длины N, содержащих более трех подряд идущих нулей.")

    while True:
        try:
            # Запрос основания системы счисления у пользователя
            k = int(input("Введите основание системы счисления (K, 2 ≤ K ≤ 10): "))
            # Запрос количества разрядов у пользователя
            n = int(input("Введите количество разрядов (N, 1 < N < 20): "))

            # Проверка корректности введенных значений
            if not (2 <= k <= 10):
                raise ValueError("Основание системы счисления K должно быть в диапазоне от 2 до 10.")
            if not (1 < n < 20):
                raise ValueError("Количество разрядов N должно быть в диапазоне от 2 до 19.")
            if not (n + k < 26):
                raise ValueError("Сумма N и K должна быть меньше 26.")

            # Вычисление и вывод результата
            result = count_k_ary_numbers(k, n)
            print(f"Количество чисел: {result}")
            break

        except ValueError as e:
            print(f"Ошибка: {e}")
            print("Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
