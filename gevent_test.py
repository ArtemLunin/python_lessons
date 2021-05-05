import gevent
from gevent import socket

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.google.com']
# gevent.spawn() создает гринлет (greenlet) (зеленый поток и микропоток) для выполнения каждого вызова gevent.socket.get­hostby­name
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# gevent.joinall() ожидает завершения всех созданных задач
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
