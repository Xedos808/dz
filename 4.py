def f(a, b):
    return (a + b) ** 3


def main():
    # Запрашиваем у пользователя ввод значений m и k
    m = float(input("Введите значение m: "))
    k = float(input("Введите значение k: "))

    # Вычисляем f(m, 10)
    first_znach= f(m, 10)

    # Вычисляем f((k + m) / 5, k + m)
    second_znach = f((k + m) / 5, k + m)

    # Находим результат выражения f(m, 10) - f((k + m) / 5, k + m)
    result = first_znach - second_znach

    # Выводим результаты
    print(f"f(m, 10) = {first_znach}")
    print(f"f((k + m) / 5, k + m) = {second_znach}")
    print(f"Результат вычисления: f(m, 10) - f((k + m) / 5, k + m) = {result}")


main()