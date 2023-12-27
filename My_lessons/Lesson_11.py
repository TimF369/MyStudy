while True:
    i = input('Please insert you choise: ')
    colors = ['red', 'yellow', 'green']
    if i.isnumeric():
        i = int(i) - 1
        if i <= 2:
            print(colors[i])
        else:
            print('У дорожного светофора 3 цвета - Дундук!')
    else:
        print('Freedom for letters!')