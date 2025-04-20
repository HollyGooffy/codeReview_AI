"""За основу взята версия deepseek"""
"""
К-ичные числа. Среди чисел в системе счисления с основанием K (2≤K≤10)
 определить сколько имеется чисел из N (1<N<20, N+K<26) разрядов таких, что в их
 записи содержится более трех подряд идущих нулей.
 """
def count_numbers_with_4_zeros(n_digits, base):

    if n_digits == 0:
        return 0

    dp = [[0] * 4 for _ in range(n_digits + 1)]
    dp[1][0] = base - 1  # Первая цифра не может быть нулем

    for i in range(2, n_digits + 1):
        total_prev = sum(dp[i - 1])
        dp[i][0] = total_prev * (base - 1)

        # Сдвигаем последовательности нулей
        dp[i][1] = dp[i - 1][0]
        dp[i][2] = dp[i - 1][1]
        dp[i][3] = dp[i - 1][2]

    sum_valid = sum(dp[n_digits])
    total = (base - 1) * (base ** (n_digits - 1))
    return total - sum_valid


def main():
    print("Программа подсчитывает количество K-ичных чисел из N разрядов,\n"
          "содержащих более трех подряд идущих нулей.")
    print("Ограничения: 2 ≤ K ≤ 10, 1 < N < 20, N + K < 26")

    while True:
        try:
            n = int(input("Введите количество разрядов N (1 < N < 20): "))
            if not (1 < n < 20):
                print("Ошибка: N должно быть в диапазоне (1, 20).")
                continue

            k = int(input("Введите основание системы K (2 ≤ K ≤ 10): "))
            if not (2 <= k <= 10):
                print("Ошибка: K должно быть в диапазоне [2, 10].")
                continue

            if n + k >= 26:
                print("Ошибка: N + K должно быть меньше 26.")
                continue

            result = count_numbers_with_4_zeros(n, k)
            print(f"Количество {k}-ичных чисел из {n} разрядов\n"
                  f"с более чем тремя подряд нулями: {result}")
            break

        except ValueError:
            print("Ошибка: Введите целое число.")


if __name__ == "__main__":
    main()