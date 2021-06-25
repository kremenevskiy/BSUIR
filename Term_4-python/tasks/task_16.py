class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

# s = Singleton()
# print("Object created", s)
# s1 = Singleton()
# print("Object created", s1)


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Person:
    def __init__(self, name, surname):
        print('Creating object')
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name



p1 = Person(name='vlad', surname='kremenevskiy')
p2 = Person('vlad', 'new')
print(p2.name + ' ' + p2.surname)