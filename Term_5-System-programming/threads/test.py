j = list(input())
s = list(input())

print(j)
print(s)

ans = 0
for i in s:
    if i in j:
        ans += 1

print(ans)