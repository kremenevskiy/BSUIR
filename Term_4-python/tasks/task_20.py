import time


def expired_cache(timeout):
    def decorator(function):
        function.cash = {}

        def wrapper(*args, **kwargs):
            print(kwargs)
            key = args + tuple(sorted(kwargs.items()))
            if key not in function.cash or time.time() - function.cash[key][1] > timeout:
                print('first time', key)
                function.cash[key] = function(*args, **kwargs), time.time()
            return function.cash[key][0]

        return wrapper
    return decorator

@expired_cache(1.9)
def sum(a, b):
    return a + b


sum(b=1, a=2)
sum(2, 3)
time.sleep(1)
print("go")
sum(b=1, a=2)

d = {'b': 1, 'a': 2}






