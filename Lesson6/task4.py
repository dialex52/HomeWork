# Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать
# такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из файлов - получить
# отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в какой-нибудь контейнерный
# тип (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при
# парсинге. В словаре должны храниться данные, полученные в результате парсинга.

import pickle

with open('users.csv', 'r', encoding='utf8') as f_user, open('hobby.csv', 'r', encoding='utf8') as f_hobby, open(
        'use_hob.pickle', 'wb') as f:
    if sum(1 for line in f_user) < sum(1 for lines in f_hobby):
        exit(1)
    f_user.seek(0)
    f_hobby.seek(0)
    while True:
        user_hobby = {}
        line_user = f_user.readline()
        user = line_user.replace(',', ' ').rstrip()
        line_hobby = f_hobby.readline()
        hobby = line_hobby.replace('\n', '').replace(',', ', ')
        if line_user:
            if not line_hobby:
                user_hobby.update({user: None})
                pickle.dump(user_hobby, f)
            else:
                user_hobby.update({user: hobby})
                pickle.dump(user_hobby, f)
        else:
            break

with open('use_hob.pickle', 'rb') as f:
    while True:
        try:
            new_dict = pickle.load(f)
            print(new_dict)
        except EOFError:
            break

    # for i in range(len(f_user))
    #     while line_hobby:
    #         user = line_user.replace(',', ' ').replace('\n', '')
    #         hobby = line_hobby.replace('\n', '').replace(',', ', ')
    #         user_hobby.update({user: hobby})
    #
    #         print(user_hobby)
# hobby = []
# with open('hobby.csv', 'r', encoding='utf8') as f:
#     for line in f:
#         hobby.append(line.replace('\n', '').replace(',', ', '))

# user_hobby = {}
#
# for i in range(len(users)):
#     if len(hobby) > len(users):
#         exit(1)
#     elif i < len(hobby):
#         user_hobby[users[i]] = hobby[i]
#     else:
#         user_hobby[users[i]] = None
#
# with open('users_hobby.pickle', 'wb') as f:
#     pickle.dump(user_hobby, f)
#
# with open('users_hobby.pickle', 'rb') as f:
#     new_dict = pickle.load(f)
# print(new_dict)
