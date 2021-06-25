class Singlton(type):
    _instances = {}
   

    def __call__(cls, *args, **kwargs):
        print(f'Singlton: cls: {cls}, args: {args} {kwargs}')
        print(cls._instances)
        if cls not in cls._instances:
            cls._instances[cls] = super(Singlton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Dog(metaclass=Singlton):
    def __init__(self, name='Dog'):
        print('creating object')
        self.name = name

    def say(self):
        print('GAV')


d = Dog(name='barsik')
d2 = Dog(name='kotik')

