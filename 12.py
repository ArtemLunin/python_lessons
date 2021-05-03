import struct
import binascii
import unicodedata
import html
import re
def unicode_test(value):
	import unicodedata
	name = unicodedata.name(value)
	value2 = unicodedata.lookup(name)
	print('value="%s", name="%s", value2="%s"' % (value, name, value2))

# unicode_test('а')
# unicode_test('😍')
# unicode_test('\u00a2')
# print(len('\u00a2'))
# unicode_test('\u00e9')

# к символам Unicode можно обращаться как по коду, так и по названию
# http://www.unicode.org/charts/charindex.html
place = 'caf\u00e9'
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)
place_bytes = place.encode('utf-8')
place2 = place_bytes.decode('utf-8')
print(place2)

snowman = '\u2603'
ds = snowman.encode('ascii', 'ignore')
print(ds)
ds = snowman.encode('ascii', 'replace')
print(ds)
ds = snowman.encode('ascii', 'backslashreplace')
print(ds)
ds = snowman.encode('ascii', 'xmlcharrefreplace')
print(ds)

# import html
# html-сущности
print(html.unescape("&egrave;"))
print(html.unescape("&#233;"))

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
# получаем строку из типа byte
print(byte_value.decode())

# import unicodedata
# Теперь создадим символ e с акутом, объединив простой символ e и акут
eacute_combined1 = "e\u0301"
print(eacute_combined1)
# нормализация символа, теперь он стал одним (а не комбинацией двух) - после этого строки Unicode можно сравнивать
eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
print(unicodedata.name(eacute_normalized))

# 12.1
mystery = "\U0001f4a9"
print(mystery)
print(unicodedata.name(mystery))

# 12.2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
pop_string = pop_bytes.decode('utf-8')
if pop_string == mystery:
	print(pop_string)

# 12.4
mammot = "We have seen thee, queen of cheese,\
Lying quietly at your ease,\
Gently fanned by evening breeze,\
Thy fair form no flies dare seize.\
\
All gaily dressed soon you'll go\
To the great Provincial show,\
To be admired by many a beau\
In the city of Toronto.\
\
Cows numerous as a swarm of bees,\
Or as the leaves upon the trees,\
It did require to make thee please,\
And stand unrivalled, queen of cheese.\
\
May you not receive a scar as\
We have heard that Mr. Harris\
Intends to send you off as far as\
The great world's show at Paris.\
\
Of the youth beware of these,\
For some of them might rudely squeeze \
And bite your cheek, then songs or glees\
We could not sing, oh! queen of cheese.\
\
We'rt thou suspended from balloon,\
You'd cast a shade even at noon,\
Folks would think it was the moon\
About to fall and crush them soon."

# используем r, чтобы \b внутри рег выражения не интерпретировался как спецсимвол
m = re.findall(r'\bc\w{3}\b', mammot)
print(m)

# 12.7
m = re.findall(r'\b[\w\']*l\b', mammot)
print(m)

# 12.8
m = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammot)
print(m)

#12.9
bytes_str = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(bytes_str)

# 12.10
print(gif)
if b'GIF89a' == gif[:6]:
	print('gif is correct')

# 12.11
print(struct.unpack('<2H', gif[6:10]))


