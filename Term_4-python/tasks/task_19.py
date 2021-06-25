def argDecorator(arg_1, arg_2):
    def decorator(function):
        print('helo')
        def wrapper(*args, **kwargs):
            print(f'decorator agrs: {(arg_1, arg_2)}')
            print(f'args: {args}')
            print(f'kwargs: {kwargs}')
            function(*args, **kwargs)
        return wrapper
    return decorator


# @argDecorator('argument dec 1', 'argument dec 2')
def nice_functions(first, sec):
    print('simple function')
    print(f'first = {first}')
    print(f'second = {sec}')


nice_functions = argDecorator('argument dec 1', 'argument dec 2')(nice_functions)


nice_functions('la', 'kwa')


