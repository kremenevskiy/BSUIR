import math


def gen(n, m):
    arr = [0] * n

    def rec(position, true_cnt):
        if position == n:
            if m == arr.count(1):
                yield arr
            return
        else:
            if true_cnt < m:
                arr[position] = 1
                yield from rec(position+1, true_cnt+1)
                arr[position] = 0
            yield from rec(position+1, true_cnt)

    return rec(0, 0)


g = gen(5, 2)
print(g)

for i in g:
    print(i)


def C(n, k):
    return int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))


def get_nth(n, k, nth):
    ans = []
    kk = 0
    for i in range(0, n):
        c = C(n - i - 1, k - kk - 1)
        if nth <= c:
            ans.append(1)
            kk += 1
        else:
            nth -= c
            ans.append(0)

        if kk == k:
            break
    while len(ans) < n:
        ans.append(0)
    return ans


def gen2(n, k):
    for i in range(C(n, k)):
        yield get_nth(n, k, i + 1)


# for gg in gen2(3, 1):
#     print(gg)





