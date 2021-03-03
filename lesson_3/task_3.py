# 3.  Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
def thesaurus(*args):
    names_dict = {}
    letter_list = []
    for name in args:
        if name[0] not in letter_list:
            letter_list.append(name[0])
    for letter in letter_list:
        names_dict[letter] = []
        for name in args:
            if letter in name:
                names_dict[letter].append(name)
    return names_dict

    # Первый вывод печатает результат в более читабельном виде.
    # Второй вывод выводит отсортированный по ключу словарь.
    # Вернуть отсортированный словарь не получилось... Всю гоолову сломал.
    # for key, value in names_dict.items():
    #     # return key, value
    # # for key in sorted(names_dict.keys()):
    # #     return key, names_dict[key]


print(thesaurus("Демид", "Марфа", "Иван", "Мария", "Петр", "Даниил", "Илья", "Ильдар"))
