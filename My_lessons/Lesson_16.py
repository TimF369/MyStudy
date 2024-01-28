result = 0
s = []

while True:
    a = int(input())
    s.append(a)
    if sum(s) == 0:
        break

for num in s:
    result += num ** 2

print(result)
