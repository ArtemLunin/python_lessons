from datetime import date, datetime, timedelta
import time

# 13.1
# print(datetime.now())
now = datetime.now()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
	# print(now_str, file=output)
	output.write(now_str)

# 13.2
with open('today.txt', 'rt') as input:
	today_string = input.read()

# 13.3
# fmt = "%Y-%m-%dT%Н:%M:%S"
fmt = "%Y-%m-%dT%H:%M:%S"
today_str = '2021-05-04T09:49:57'
print(today_string)
new_date = time.strptime(today_str, fmt)
print(new_date[2])

# 13.4 13.5
my_birthday = date(1975, 9, 25)
print(my_birthday.strftime('%A %d'))
print(my_birthday.isoweekday())

# 13.6
day_10000 = timedelta(days=15000)
future = my_birthday + day_10000
print(future)
