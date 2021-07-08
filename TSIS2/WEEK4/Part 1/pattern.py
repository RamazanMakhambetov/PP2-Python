import re

with open('raw.txt', encoding = 'utf-8') as txt:
    txt = txt.read()

    print('Компания:', *re.findall(r'Филиал (.+)', txt))
    print('БИН:', *re.findall(r'БИН (.+)', txt))
    print('Адресс:', *re.findall(r'г\..+', txt))
    print('Дата и время:', *re.findall(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', txt))
    
    TITLE = re.findall(r'\.\n(.*)', txt)
    COUT = re.findall(r'(\d)\,000', txt)
    UNIT_PRICE = re.findall(r'\d\,000 x (.*)\,', txt)

    for n, i in enumerate(TITLE, 0):
        SUM_PRICE = int(UNIT_PRICE[n].replace(' ', '')) * int(COUT[n])
        print(f'{n + 1}. {i}\nКол-во: {COUT[n]} шт\nЦена: {UNIT_PRICE[n]}тг\nВ сумме: {SUM_PRICE}тг\n')