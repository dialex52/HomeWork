
inp_list = ['инженер-конструктор Игорь',
            'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй',
            'директор аэлита']

for element in inp_list:
    element = element.split(' ')
    print('Привет' + ' ' + element[-1].title())