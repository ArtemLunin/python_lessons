class Thing:
    pass

class Thing3:
    letters = 'xyz1'
    def __init__(self):
        self.letters = 'xyz'


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    def __str__(self):
        dump_ = ''
        for attr in list(self.__dict__.keys()):
            dump_ += attr + ':' + str(self.__dict__[attr]) + ', '
        return dump_

example = Thing()
example3 = Thing3()

elem = Element('Hydrogen', 'H', 1)

dict_ = {'name': 'Hydrogen', 'symbol': 'H' , 'number': 1}

# в этом случае словарь будет разобран на ключ=значение, так как именя ключей совпадают с атрибутами объекта, это сработает
hydrogen = Element(**dict_)

# print('Thing:')
# print(Thing)
# print(example)
# print('example:' + repr(example))

# print(Thing3.letters)
# print(example3.letters)

print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)
# hydrogen.dump()

class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())
