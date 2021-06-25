def gen(n, m):
    arr = [0] * m
    mrk = [False] * n

    def rec(i):
        if i == m:
            yield arr
            return
        for j in range(n):
            if mrk[j]:
                continue
            mrk[j] = True
            arr[i] = j + 1
            yield from rec(i + 1)
            mrk[j] = False

    return rec(0)


def A(n, m):
    kol = 1
    for i in range(m):
        kol *= n - i
    return kol

class IterA:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.genA = gen(n, m)
        self.max = A(n, m)
        self.current = 0
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt == self.max:
            raise StopIteration
        current = next(self.genA)
        self.cnt += 1
        return current

print('hi')
iterr = IterA(4, 3)

for i in iterr:
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


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.count = 0
        self.maxn = A(n, m)

    def __next__(self):
        if self.count < self.maxn:
            self.count += 1
            return get_nth(self.n, self.m, self.count - 1)
        else:
            raise StopIteration


# for gg in Iterator(4, 3):
#     print(gg)
