# ЗАДАНИЕ 1

inp_time = int(input('Введите временной интервал в секундах: '))

days = inp_time // 86400
hours = inp_time % 86400 // 3600
minutes = inp_time % 3600 // 60
seconds = inp_time % 3600 % 60

if inp_time >= 86400:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
elif inp_time >= 3600:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
elif inp_time >= 60:
    print(minutes, 'мин', seconds, 'сек')
else:
    print(seconds, 'сек')