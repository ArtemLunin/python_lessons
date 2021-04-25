letters = 'abcdefghijklmnopqrstuvwxyz'
# строка наоборот
# print (letters[::-1])
# символы из строки с шагом 2
# print(letters[1::2])
# неправильное смещение на старте заменяется на 0
# print(letters[-50:])
# длина строки
# print(len(letters))

# tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
# создание списка, используя разделитель
# print(tasks.split(','))

# crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
# создание строки из списка, с заданным разделиителем
# crypto_string = ', '.join(crypto_list)
# print(crypto_string)

# Функция strip() БЕЗ АРГУМЕНТОВ удаляет символы-пробелы ( ' ' , '\t' , '\n' ) с обоих концов строки, lstrip() — только в начале, а rstrip()
# test_string = '!test string!!!!!!'
# print(test_string.strip('!'))

# строка начинается с poem.startswith('All')
# строка заканчивается poem.endswith('That\'s all, folks!')
# позиция с начала строки poem.find(word) или -1 если нет, poem.index(word) - или искл. если нет
# позиция с конца строк poem.rfind(word) или -1 если нет, poem.rindex(word) - или искл. если нет

setup = 'a duck goes into a bar...'
# первое слово с большой буквы capitalize()
# все слова с большой буквы title()
# все слова большими буквами upper()
# все слова маленькими буквами lower()
# поменять регистр на противоположный
# print(setup.swapcase())

# форматирование строк в новом стиле
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
# вывод имен переменных
print(f'{thing=}, {place=}')
