# Задание 2
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Задание 3
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).

inp_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = inp_list.copy()
for element in new_list:
    if not element.isalpha():
        number_ind = inp_list.index(element)
        inp_list.insert(number_ind, '"')
        inp_list.insert(number_ind + 2, '"')
        if len(element) == 1:
            element = '0' + element
            inp_list[number_ind + 1] = element
        elif not element[0].isdigit():
            element = element[0] + '0' + element[1:]
            inp_list[number_ind + 1] = element
print(inp_list)
print(' '.join(inp_list))







#
# print(number_ind)

# # print(inp_list)
