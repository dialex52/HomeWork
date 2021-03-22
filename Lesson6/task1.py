# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
# ('141.138.90.60', 'GET', '/downloads/product_2')

# with open('new_file.txt', 'w', encoding='utf8') as file:
import re

log_list = []
with open('nginx_logs.txt', 'r', encoding='utf8') as f:
    for line in f:
        sep = ' - - ', ' "', ' HTTP', ' '
        sep_list = '|'.join(map(re.escape, sep))
        new_line = re.split(sep_list, line)
        result = (new_line[0], new_line[3], new_line[4])
        log_list.append(result)
print(log_list)
# with open('new_file.txt', 'w', encoding='utf8') as f:
#     for tup in log_list:
#         f.write(str(tup) + '\n')
