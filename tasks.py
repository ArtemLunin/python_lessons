# pip install invoke
# функции доступны как аргуметы командной строки
from invoke import task

@task

def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)

# доступные задачи - invoke -l
