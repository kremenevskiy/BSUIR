def gen(obj):
    if type(obj) is not list:
        yield obj
        return
    for item in obj:
        g_l = list(gen(item))
        for i in g_l:
            yield i


# lst = [[1, 1], [2], [1, 1]]
lst = [[1, [1, 3]], 2, [1, 4, [6]]]
for i in gen(lst):
    print(i, end=" ")
