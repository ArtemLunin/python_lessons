import multiprocessing
import os


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

# в первый раз выведет как программа, дальше - как дочерний процесс
if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami, args=("I'm function %s" % n,))
        p.start()
