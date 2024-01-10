b = [int(a) for a in input().split()]
i = 0
s = ""
while i < len(b):
    if len(b) == 1:
        s += str(b[i])
        break
    if i == 0:
        s += str(b[i + 1] + b[-1]) + ' '
    elif i == len(b) - 1:
        s += str(b[0] + b[i - 1]) + ' '
    else:
        s += str(b[i + 1] + b[i - 1]) + ' '
    i += 1
print(s)
