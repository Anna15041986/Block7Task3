"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# list
month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8],
              ['Осень', 9, 10, 11]]
month_number = int(input('Введите номер месяца: '))
if month_number in range(1, 13):
    for i, el in enumerate(month_list):
        if month_number in el[1:4]:
            print(f'Результат через список: {el[0]}')
            break

# dict
month_dictionary = {'Зима': [12, 1, 2],
                    'Весна': [3, 4, 5],
                    'Лето': [6, 7, 8],
                    'Осень': [9, 10, 11]}
if month_number in range(1, 13):
    for i in month_dictionary.items():
        if month_number in i[1]:
            print(f'Результат через словарь: {i[0]}')
            break

