"""
2. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""

text1  = input("Введите слова через пробел: ")
counter = 1
splitted = text1.split()
for word in splitted:
    if len(word) > 10:
        print(f"{counter}. {word[:10]}")
    else:
        print(f"{counter}. {word}")
    counter += 1
