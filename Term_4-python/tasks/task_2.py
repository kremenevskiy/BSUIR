def gen(n, m):
    arr = [0] * m
    mrk = [False] * n

    def rec(i):
        if i == m:
            yield arr
            return
        for j in range(0, n):
            if mrk[j]:
                continue
            mrk[j] = True
            arr[i] = j+1

            yield from rec(i+1)
            mrk[j] = False

    return rec(0)


g = gen(4, 2)
for i in g:
    print(i)


def A(n, m):
    kol = 1
    for i in range(m):
        kol *= n - i
    return kol


def get_nth(n, m, nth):
    mrk = [False] * n
    ans = []
    for i in range(m):
        a = A(n - i - 1, m - i - 1)
        for j in range(n):
            if mrk[j]:
                continue
            if nth >= a:
                nth -= a
                continue
            ans.append(j + 1)
            mrk[j] = True
            break
    return ans


def gen2(n, m):
    for i in range(A(n, m)):
        yield get_nth(n, m, i)


# for gg in gen(4, 3):
#     print(gg)


