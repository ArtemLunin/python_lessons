# в функцию можно передавать именованные аругменты
# menu(entree='beef', dessert='bagel', wine='bordeaux')

# аргументы по умолчанию
# def menu(wine, entree, dessert='pudding')

# так делать нельзя - при следующем вызове список не будет пустым
# def buggy(arg, result=[])

# 2 параметра обязательные, остальные попадут в кортеж args
# def print_more(required1, required2, *args)

# внутри функции имена аргументов становятся ключами, а их значения - значениями в словаре 
# def print_kwargs(**kwargs):

#  аргументы после * - передаются как именованные
# def print_data(data, *, start=0, end=100)

def get_odds():
	for number in range(10):
		if number % 2 == 1:
			yield number

count = 0
for i in get_odds():
	count += 1
	if count == 3:
		print(i)
		break



def test(func):
	def new_func(*args, **kwargs):
		print('start')
		print(func(*args, **kwargs))
		print('end')
	return new_func

@test
def simple():
	return 'SIMPLE'

simple()


class OopsException(Exception):
	pass


try:
	raise OopsException()
except OopsException as exc:
	print('Caught an oops')
