import redis
conn = redis.Redis()

conn.set('pass', 12345)

print(conn.keys('*'))
print(conn.get('pass'))

conn.getset('pass', 'sdh')
print(str(conn.get('pass'), 'UTF-8'))

conn.hset('test', 'count', 1)
conn.hset('test', 'name', 'Fester')

# print(conn.hmget('test', 'count', 'name'))
print(conn.hvals('test'))

conn.hincrby('test', 'count', 3)

print(conn.hvals('test'))
