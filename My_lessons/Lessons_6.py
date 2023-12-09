a = int(input())
b = int(input())
d = min(a, b)
while d % a != 0 or d % b != 0:
     d += 1
print(d)
