x = float(input())
y = float(input())
action = input()
if action == '*':
    print(x * y)
elif action == '+':
    print(x + y)
elif action == '-':
    print(x - y)
elif action == 'pow':
    print(x ** y)
elif action == '/' or action == 'div' or action == 'mod':
    if y == 0:
        print("Деление на 0!")
    elif action == '/':
        print(x / y)
    elif action == 'div':
        print(x // y)
    elif action == 'mod':
        print(x % y)
