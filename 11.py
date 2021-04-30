from collections import OrderedDict
from collections import defaultdict

#в версиях python >3.7 порядок ключей в словаре не меняется (вывод OrderedDict совпадает с обычным выводом)
fancy = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
plain = {'b': 2, 'a': 1, 'c': 3}
print(plain)
print(fancy)

dict_of_lists = defaultdict(list)

dict_of_lists['a'].append('something for a')

print(dict_of_lists['a'])
