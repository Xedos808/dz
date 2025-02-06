def main():
    # 1. Считываем три строки чисел
    first_line = input("Введите первую строку: ")
    second_line = input("Введите вторую строку: ")
    third_line = input("Введите третью строку: ")

    # 2. Преобразуем строки в списки
    first_nums = first_line.split()
    second_nums = second_line.split()
    third_nums = third_line.split()

    # 3. Создаём множество из первой строки
    first_set = set(first_nums)

    # 4. Находим пересечение во второй и третьей строках
    common_numbers = set(second_nums) & set(third_nums)

    # 5. Фильтруем, удаляя числа, которые есть в первой строке
    result_set = {num for num in common_numbers if num not in first_set}

    # 6. Форматируем вывод
    result_output = "; ".join(result_set)

    # 7. Подсчитываем сумму
    result_sum = sum(map(int, result_set))

    # 8. Выводим результаты
    print(result_output)
    print(result_sum)


main()