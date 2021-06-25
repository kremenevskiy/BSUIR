from functools import cmp_to_key


def sort_decor(cmpr):
    if type(cmpr) != type(sort_decor):
        raise ValueError('cmp should be a function')

    def decorator(func):
        def wrapper(*args, **kwargs):
            args = tuple(sorted(args, key=cmp_to_key(cmpr)))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def comparer(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


@sort_decor(comparer)
def sum(a, b, c):
    return a * 100 + b * 10 + c


print(sum(1, 2, 3))
print(sum(3, 2, 1))







