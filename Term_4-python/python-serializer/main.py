import os
from serializer.parsers.parser import Parser
from parsers_test import test_parsers

dic = {'lab': 2, 'status': 'done'}
lst = ['first', 'second', 3, {'number': 4}]
tupl = ('test_tuple', {'status': 'ok'}, ('nested_tuple', 'one_more'))




if __name__ == '__main__':
    test_parsers(dic)
    test_parsers(lst)
    test_parsers(tupl)

