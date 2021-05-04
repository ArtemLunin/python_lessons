# 14.1
import os

# print(os.listdir('.'))

# 14.2
# print(os.listdir('..'))

# 14.3
test1 = 'This is a test of the emergency text system!'
with open('test.txt', 'wt') as test_out:
# print(test1, file=test_out)
	test_out.write(test1)
# test_out.close()

# 14.4
with open('test.txt', 'rt') as text_in:
	test2 = text_in.read()

if test1 == test2:
	print('identical!')
