s = input()
i = 0
z = s[0]
res = ''
for c in s:
    if c == z:
        i += 1
    else:
        res += z + str(i)
        i = 1
        z = c
res += z + str(i)
print(res)

