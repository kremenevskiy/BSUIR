from serializer import Serializer
import inspect


def say(msg):
    msg += 'Vlad'
    print(msg)
    return msg


class Machine:
    # speed = 10
    places = 4

    def __init__(self, speed):
        self.speed = speed

    def __getattribute__(self, item):
        print('get attribute: ', item)

    # @staticmethod
    def go(self):
        print('run ', self.speed)

    @staticmethod
    def set_speed(self, speed):
        speed = speed






if __name__ == '__main__':
    def f():
        print('hey')

    ser = Serializer.serializes(f)
    deser = Serializer.deserialize(ser)

