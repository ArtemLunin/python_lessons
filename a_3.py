def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3 * number + 1

try:
	number = int(input('Enter stat number:'))
	while True:
		collatzRes = collatz(number)
		print(collatzRes)
		if collatzRes == 1:
			break
		number = collatzRes
except ValueError:
	print('Only integer value is valid!')
