from datetime import datetime
from time import sleep
import multiprocessing
import os
import time
import random

# def whoami(what):
# 	time.sleep(random.random() * 5)
# 	os.system('date -u')
# 	print("Process %s says: %s" % (os.getpid(), what))

# # в первый раз выведет как программа, дальше - как дочерний процесс
# if __name__ == "__main__":
#     # whoami("I'm the main program")
#     for n in range(3):
#         p = multiprocessing.Process(target=whoami, args=("I'm function %s" % n,))
#         p.start()

#15.1 - test
def now(seconds):
	sleep(seconds)
	print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
	for n in range(3):
		seconds = random.random()
		proc = multiprocessing.Process(target=now, args=(seconds,))
		proc.start()
