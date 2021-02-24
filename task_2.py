# ЗАДАНИЕ 2

print('Программа считает сумму цифр введенного числа\nдля выхода из программы, введите "0"')
while True:
    result = 0
    inp_number = int(input('Введите любое число: '))
    if inp_number < 0:
        print('Число долно быть положительным')
    elif inp_number == 0:
        print('конец')
        break
    else:
        while inp_number != 0:
            result = result + inp_number % 10
            inp_number = inp_number // 10
        print(result)