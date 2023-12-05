x = int(input())
if (((x % 10 == 1)) and (x % 100 != 11)):
    print(f'{x} программист')
elif (((x % 10 in [2, 3, 4]) and (x % 100 not in [12, 13, 14]))):
    print(f'{x} программиста')
else:
    print(f'{x} программистов')

