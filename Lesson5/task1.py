# Задание 1. Функция-генератор rand_nums
# Написать функцию-генератор rand_nums, генерирующую N случайных целых чисел в диапазоне 1 до 100 (включительно).
# Количество чисел N, которое выдаст генератор передается в функцию через параметр:
import random


def rand_nums(n):
    for i in range(n):
        yield random.randint(1, 100)


rand15 = rand_nums(15)
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
print(next(rand15))
