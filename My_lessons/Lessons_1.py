fig = input()
if fig == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    per = ((a + b + c) / 2)
    print((per * (per - a) * (per - b) * (per - c)) ** 0.5)
elif fig == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif fig == 'круг':
    r = int(input())
    print(3.14 * r ** 2)
