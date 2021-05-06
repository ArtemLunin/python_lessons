import requests
import urllib.request as ur

url = 'http://www.example.com/'

conn = ur.urlopen(url)

data = conn.read()
# первые 50 байт содержимого
# print(data[:50])

str_data = data.decode('utf8')
# print(str_data[:50])

# полученные заголовки
# for key, value in conn.getheaders():
    # print(key, value)

# библиотека requests:
resp = requests.get('http://example.com')
print(resp.status_code)
print(resp.text[:50])
