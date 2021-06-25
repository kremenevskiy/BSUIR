def cached(size):
    def decorator(func):
        func.cash = {}

        def wrapper(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))

            if key not in func.cash.keys():
                if len(func.cash) >= size:
                    print('clearing')
                    func.cash.clear()
                print(f'calculating {key}')
                func.cash[key] = func(*args, **kwargs)

            return func.cash[key]
        return wrapper
    return decorator


@cached(2)
def sum(a, b):
    return a + b


sum(2, 3)
sum(2, 5)
# sum(2, 7)
sum(2, 3)



