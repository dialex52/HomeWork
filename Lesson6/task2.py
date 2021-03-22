# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.

import re

log_list = []
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        sep = ' - - ', ' "', ' HTTP', ' '
        sep_list = '|'.join(map(re.escape, sep))
        new_line = re.split(sep_list, line)
        log_list.append(new_line[0])
ip_dict = {}
for element in log_list:
    ip_dict.setdefault(element, 0)
    ip_dict[element] += 1
result = []
count = 1
for element in log_list:
    if ip_dict[element] >= count:
        count = ip_dict[element]

key_list = list(ip_dict.keys())
val_list = list(ip_dict.values())
print(key_list[val_list.index(count)], count)