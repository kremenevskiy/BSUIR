import os
import sys
import inspect
import psutil
import time


def parse_dict(d):
    for i in d:
        if isinstance(d[i], dict):
            parse_dict(d[i])
        else:
            if hasattr(d[i], '__call__'):
                try:
                    fun_arg_count = len(inspect.getfullargspec(d[i]).args)
                    if fun_arg_count == 0:
                        # print(d[i])
                        print(f'function documentation:')
                        print(d[i].__doc__)
                        print('function result:')
                        print(f'\t{d[i]()}')
                        print()
                        time.sleep(0.1)
                except Exception:
                    pass
                    # print('unsupported callable')
                    # print(d[i])
            else:
                print(type(d[i]))
                print(f'key: {i}: {str(d[i])}')
                time.sleep(0.1)
                print()


sys_d = sys.__dict__
os_d = os.__dict__
psutil_d = psutil.__dict__

parse_dict(psutil_d)
parse_dict(sys_d)
parse_dict(os_d)
