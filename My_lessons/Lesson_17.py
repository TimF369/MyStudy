n = int(input())
count_print = 0

for num in range(n + 1):
    for _ in range(num):
        count_print += 1
        print(num, end=" ")
        if count_print == n:
            break
    if count_print == n:
        break
