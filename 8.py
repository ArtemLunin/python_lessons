# способы создания словаря
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}

acme_customer = dict(first="Wile", middle="E", last="Coyote")

# в итоге получаются одинаковые словари
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

los = ['ab', 'cd', 'ef']
print(dict(los))

# если такого ключа нет, то вернет значение 2-го аргумента
pythons = {}
print(pythons.get('Groucho', 'Not a Python'))
print(pythons.get('Groucho2'))

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
# вернет итерабельное представление ключей
print(signals.keys())
# вернет список ключей
print(list(signals.keys()))
# вернет список значений
print(list(signals.values()))

print(len(signals))

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
# объединение словарей
result = {**first, **second}
print(result)

# к первому словарю добавляется 2-й, одинаковые ключи - используются значения 2-го словаря
first.update(second)
print(result)

# если ключа нет, вернет значение 2-го аргумента
# print(pythons.pop('First', 'Hugo'))

# вернет ошибку - такого ключа нет в словаре
# del pythons['Marx']

pythons.clear()

# копирование значений из одного словаря в другой
original_signals = signals.copy()

accusation = {'room': 'ballroom', 'weapon': 'lead pipe','person': 'Col. Mustard'}
# итерация по ключам
for card in accusation:
	print(card)
# по значениям
for value in accusation.values():
	print(value)
# по парам
for item in accusation.items():
	print(item)


# создание множества (как словарь, только без значений)
even_numbers = {0, 2, 4, 6, 8, 8}

print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

s = set((1, 2, 3))
# при удалении несуществующего элемента будет ошибка
# s.remove(5)
# print(s)

#  проверяет на наличие во множестве сразу двух ключей
#  по сути - пересечение двух множеств
# if contents & {'vermouth', 'orange juice'}

e2f = { "dog": "chien", "cat": "chat", "walrus":"morse"}
print(e2f["walrus"])
f2e = {}
for en, fr in e2f.items():
	f2e[fr] = en
print(set(e2f))

squares = {number: number * number for number in range(10)}
print(squares)

odd = {number for number in range(10) if number % 2 == 0}
print(odd)
