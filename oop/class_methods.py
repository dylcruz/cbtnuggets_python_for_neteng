class Human:
    _needs = ['air', 'food', 'water']
    def __init__(self, name):
        self._name = name

    @classmethod
    def needs(cls):
        return cls._needs
    
h1 = Human('Dylan')
print(h1._needs)
h1._needs = ['pizza', 'ice cream']
print(h1._needs)
print(h1.needs())

class Fashion:
    def __init__(self, style):
        self.style = style

    @classmethod
    def funky(cls):
        return cls(['bellbottoms', 'flowery shirt', 'big boots'])

    @classmethod
    def gothic(cls):
        return cls(['trench coat', 'leather jacket', 'doc martin boots'])

    @classmethod
    def casual(cls):
        return cls(['t-shirt', 'jeans', 'sneakers'])

f1 = Fashion.funky()
print(f1.style)
f2 = Fashion.casual()
print(f2.style)
