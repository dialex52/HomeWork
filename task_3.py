
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000 (куб X - третья степень числа X):
#
# 1) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.

def div_by_seven(some_array):
    element_sum = 0
    new_some_array = []
    for number in some_array:
        while number != 0:
            element_sum = element_sum + number % 10
            number = number // 10
        if element_sum % 7 == 0:
            new_some_array.append(element_sum)
    print(sum(new_some_array))
    # for i in new_some_array:
    #     number_sum = number_sum + i


array = [number ** 3 for number in range(1, 1000, 2)]
print(array)
div_by_seven(array)

# каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из нового списка,
# сумма цифр которых делится нацело на 7.

new_array = [number ** 3 + 17 for number in range(1, 1000, 2)]
print(new_array)
div_by_seven(new_array)

# 3) Написать алгоритм вычисляющий то же значение суммы, что и в пункте 2), но не создавая списков

element_sum = 0
sum_of_numbers = 0
for number in range(1, 1000, 2):
    number = number**3 + 17
    while number != 0:
        element_sum = element_sum + number % 10
        number = number // 10
    if element_sum % 7 == 0:
        sum_of_numbers = sum_of_numbers + element_sum
print(sum_of_numbers)