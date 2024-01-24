b = [int(a) for a in input().split()]
a = None
b.sort()
for i in b:
    if b.count(i) > 1:
        if i != a:
            print(i, end=' ')
            a = i
