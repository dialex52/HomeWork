# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель
# между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем
# данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с
# кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import pickle

users = []
with open('users.csv', 'r', encoding='utf8') as f:
    for line in f:
        users.append(line.replace(',', ' ').replace('\n', ''))

hobby = []
with open('hobby.csv', 'r', encoding='utf8') as f:
    for line in f:
        hobby.append(line.replace('\n', '').replace(',', ', '))


user_hobby = {}

for i in range(len(users)):
    if len(hobby) > len(users):
        exit(1)
    elif i < len(hobby):
        user_hobby[users[i]] = hobby[i]
    else:
        user_hobby[users[i]] = None

with open('users_hobby.pickle', 'wb') as f:
    pickle.dump(user_hobby, f)

with open('users_hobby.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print(new_dict)
