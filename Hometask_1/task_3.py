age = int(input('Возраст: '))
name = input('Имя: ')
if (age >= 0) and (age < 75) and name != 'Иван':
    if age >= 16 :
        print ('Поздравляем вы поступили в ВГУИТ')
    else:
        print('Сначала нужно окончить школу')
        if age < 16:
            print(16 - age)


