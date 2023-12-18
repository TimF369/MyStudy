a = int(input())
b = int(input())
c = int(input())
tmp = [a, b, c]
tmp.sort()
print(tmp.pop(2))
print(tmp.pop(0))
print(tmp[0])
