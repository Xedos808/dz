import math
def f(a, b, c):
    return (2 * a - b * math.sin(c)) / (5 + abs(c))


# Главная функция
def main():
    # Запросить у пользователя значения S и t
    S = float(input("Введите значение S: "))
    t = float(input("Введите значение t: "))

    # Вычисляем f(t, 2S, 1/17)
    result1 = f(t, 2 * S, 1 / 17)

    # Вычисляем f(22, t, S - t)
    result2 = f(22, t, S - t)

    # Сумма результатов двух функций
    total_result = result1 + result2

    # Вывод результата
    print(f"Результат вычисления: {total_result}")

main()