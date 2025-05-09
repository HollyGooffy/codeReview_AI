def count_without_forbidden(N, K):
    def f(pos, run):
        # pos - текущая позиция (0-based индекс); run - текущая длина цепочки нулей
        if pos == N:
            return 1
        total = 0
        if pos == 0:
            for d in range(1, K):
                # В первой позиции ненулевое число, поэтому run обнуляется
                total += f(pos + 1, 0)
        else:
            # Для остальных позиций можно выбирать любую цифру от 0 до K-1
            for d in range(K):
                if d == 0:
                    # Если добавляем 0, увеличиваем счетчик подряд идущих нулей.
                    # Если получаем 4 подряд нуля, это недопустимо.
                    if run == 3:
                        continue
                    else:
                        total += f(pos + 1, run + 1)
                else:
                    # Если цифра не ноль, обнуляем счетчик нулей
                    total += f(pos + 1, 0)
        return total

    return f(0, 0)


def main():
    print("Программа для подсчёта N-разрядных чисел в системе счисления с основанием K,")
    print("в которых встречается более трёх подряд идущих нулей (т.е. минимум 4 нуля подряд).")
    print("Ограничения: 2 ≤ K ≤ 10, 1 < N < 20 и N + K < 26.")

    try:
        K = int(input("Введите основание K (2 ≤ K ≤ 10): "))
        N = int(input("Введите число разрядов N (1 < N < 20): "))
    except ValueError:
        print("Ошибка: необходимо вводить целочисленные значения!")
        return

    if not (2 <= K <= 10):
        print("Ошибка: K должно быть в диапазоне от 2 до 10.")
        return
    if not (1 < N < 20):
        print("Ошибка: N должно быть больше 1 и меньше 20.")
        return
    if not (N + K < 26):
        print("Ошибка: сумма N + K должна быть меньше 26.")
        return

    total = (K - 1) * (K ** (N - 1))
    count_good = count_without_forbidden(N, K)
    count_forbidden = total - count_good

    print("\nРезультаты:")
    print(f"Количество чисел, содержащих более трёх подряд идущих нулей: {count_forbidden}")


if __name__ == '__main__':
    main()
