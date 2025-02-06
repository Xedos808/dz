def main(number, words_string):
    # Разбиваем строку на отдельные слова
    words = words_string.split('; ')
    # Фильтруем слова, длина которых не кратна числу
    filtered_words = [word.upper() for word in words if len(word) % number != 0]
    # Формируем итоговую строку с разделением через ' - '
    result = ' - '.join(filtered_words)
    return result


number = int(input("Введите число: "))
string = input("Введите строку слов: ")
print(main(number, string))