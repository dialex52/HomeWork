price_list = [56.9, 37.90, 23.06, 0.78, 87, 97, 43.78, 89.01, 97.10]

new_price = []
for element in price_list:
    rub_element = int(element * 100 // 100)
    kop_element = int(element * 100 % 100)
    if kop_element == 0:
        new_element = str(rub_element) + ' руб ' + str(kop_element) + '0 коп'
    elif len(str(kop_element)) == 1:
        new_element = str(rub_element) + ' руб ' + '0' + str(kop_element) + ' коп'
    else:
        new_element = str(rub_element) + ' руб ' + str(kop_element) + ' коп'
    new_price.append(new_element)

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп.

print(', '.join(new_price), id(new_price))
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
print(', '.join(sorted(new_price)), id(new_price))
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
sort_price = sorted(new_price, reverse=True)
print(sort_price)
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(sort_price[:5])

