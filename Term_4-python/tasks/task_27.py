# tasks = ["A", "A", "A", "B", "B", "B"]
tasks = ["A", "A", "A", "B", "B", "B", "B", 'B', 'B', 'Q', "C", "D", "C"]
n = 2
BIG = 10 ** 9 + 7
last = [-BIG] * 26
kol = [0] * 26
for i in range(len(tasks)):
    kol[ord(tasks[i]) - ord('A')] += 1

taken = 0
i = -1
while taken < len(tasks):
    i += 1
    mx, ps = 0, -1
    for j in range(26):
        if i - last[j] > n and kol[j] > mx:
            mx = kol[j]
            ps = j
    if ps == -1:
        skip = BIG
        for j in range(26):
            if kol[j] > 0:
                skip = min(skip, n - (i - last[j]) + 1)

        for j in range(skip):
            print("w", end=" ")
        i += skip - 1
        continue
    last[ps] = i
    kol[ps] -= 1
    taken += 1
    print(chr(ord('A') + ps), end=" ")

print("\nans: ", i + 1)
