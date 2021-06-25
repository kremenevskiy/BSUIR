import math
def gen(n):
    arr = [0] * n
    mrk = [False] * n

    def rec(i):
        if i == n:
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


for i in gen(3):
    print(i)


def get_nth(n, nth):
    mrk = [False] * n
    ans = []
    for i in range(n):
        a = math.factorial(n - i - 1)
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


def gen2(n):
    for i in range(math.factorial(n)):
        yield get_nth(n, i)


# for gg in gen2(4):
#     print(gg)


def next_permutation(arr):
    n = len(arr)
    if all(arr[i - 1] > arr[i] for i in range(1, n)):
        return sorted(arr)
    copy = [e for e in arr]
    for i in range(1, n):
        if arr[-i - 1] < arr[-i]:
            upper_val = min(e for e in arr[-i:] if e > arr[-i - 1])
            for j in range(n):
                if arr[j] == upper_val:
                    copy[j] = copy[-i - 1]
                    copy[-i - 1] = upper_val
            copy = copy[:-i] + sorted(copy[-i:])
            return copy


def P(n):
    inds = [i for i in range(n)]

    while True:
        yield inds
        inds = next_permutation(inds)
        if all(inds[i - 1] < inds[i] for i in range(1, n)):
            break


gen = P(4)

# print(gen)


def Print(iterable):
    for elem in iterable:
        print(elem)
    print()


# Print(gen)