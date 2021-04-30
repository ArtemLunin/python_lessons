import unicodedata
import html
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
