while True:
    i = input('Please insert you choise: ')
    colors = ['red', 'yellow', 'green']
    if i.isnumeric():
        if int(i) <= 2:
            print(colors[int(i) - 1])
        else:
            print('У дорожного светофора 3 цвета - Дундук!')
    else:
        print('Freedom for letters!')