password = 'swordfish'
icecream = 'tuttifrutti'
#  в правой части - кортеж, в левой части - две переменные, т.е. это распаковка кортежа
password, icecream = icecream, password
# кортеж нельзя изменить, но можно присвоить ему новое значение


# list() преобразует другие итерабельные типы данных (например, кортежи, строки, множества и словари) в списки
# list('cat')
# ['c', 'a', 't']

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# others = ['Gummo', 'Karl']
# marxes.extend(others) - добавит в список 2-й список others

# del marxes[1] - удаляет из списка элемент с индексом
# marxes.remove('Groucho') - удаляет из списка элемент по значению
# marxes.pop() - получает элемент из списка и удаляет его
# work_quotes.clear() - удаляет все элементы из списка

# marxes.count('Harpo') - количество элементов в списке с заданным значением
# len(marxes) - общее число элементов

# способы копирования списков
# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# deepcopy() - делает копию и всех вложенных объектов
# zip() - используется для параллельной итерации по нескольким спискам

# способ создания списка
# number_list = [number for number in range(1, 6)]
# создание списка только с нечетными значениями
# a_list = [number for number in range(1, 6) if number % 2 == 1]

# years_list = [number for number in range(1975,2021)[0:6]]
# print(years_list[-1])

things = ["mozzarella", "cinderella","salmonella"]
print(things.index('cinderella'))
# print(things[1].title())
things[0] = things[0].upper()
print(things)
things.remove('salmonella')
print(things)
