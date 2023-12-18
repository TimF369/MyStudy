a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(end='\t')
for y in range(c, d + 1):
    if y == d:
        print(y)
    else:
        print(y, end='\t')


for x in range(a, b + 1):
    print(x, end='\t')
    for y in range(c, d + 1):
        if y == d:
            print(y * x)
        else:
            print(y * x, end='\t')
