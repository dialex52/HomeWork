import requests
import re
from decimal import *
import datetime


def get_currency_rate(currency):
    global date
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    resp_decoding = str(response.content.decode(errors='replace'))
    separators = '<', '>', '"'
    sep_string = '|'.join(map(re.escape, separators))
    sep_list = re.split(sep_string, resp_decoding)
    if currency.upper() in sep_list:
        for i in range(len(sep_list)):
            if sep_list[i] == 'ValCurs Date=':
                inp_date = (sep_list[i + 1]).split('.')
                date = datetime.date(int(inp_date[2]), int(inp_date[1]), int(inp_date[0]))

            if currency.upper() == sep_list[i]:
                rate = round(Decimal(sep_list[i + 12].replace(',', '.')) / Decimal(sep_list[i + 4]), 2)
                print('1 {} : {} RUB, {}'.format(currency.upper(), rate, date))
    else:
        return None
