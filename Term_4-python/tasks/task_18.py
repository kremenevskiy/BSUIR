class Singlton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        print('initiiiii')
        if not isinstance(cls._instance, cls):

            cls._instance = object.__new__(cls)
        return cls._instance


class Factory(Singlton):
    def __init__(self, name):
        self.name = name
        print('creating object')

    def get_name(self):
        return self.name


f = Factory('new fac')
print(f)
f = Factory('new facew')
f1 = Factory('new facasdf')
print(f1)
f2 = Factory('new21')
print(f2)

print(f.name)
print(f1.name)
print(f2.name)

f.get_name()




