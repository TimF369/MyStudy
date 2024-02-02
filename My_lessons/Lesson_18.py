lst = [int(a) for a in input().split()]
x = int(input())
index = 0
exist_x = False

for i in lst:
    if x == i:
        print(index, end=' ')
        exist_x = True
    index += 1

if not exist_x:
    print("Отсутствует")
