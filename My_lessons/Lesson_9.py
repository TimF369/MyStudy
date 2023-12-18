a = int(input())
b = int(input())
sum_num = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        sum_num += i
print(sum_num / count)
