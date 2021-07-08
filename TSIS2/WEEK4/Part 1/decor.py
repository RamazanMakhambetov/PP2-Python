# Модуль PrettyTable дает нам возможность строить таблицы
# Модуль PrettyTable не встроен в Python, поэтому его придется скачивать отдельно
import re
from prettytable import PrettyTable

# Указываем какой нам текст надо открывать
# " encoding = 'utf-8' " дает нам возможность читать русский текст
with open('raw.txt', encoding = 'utf-8') as txt:
    txt = txt.read()

    # Переменная для считывания общей суммы
    SUM = 0

    # Название компании
    COMPANY_NAME = re.findall(r'Филиал (.+)', txt)

    # БИН компании
    BIN = 'БИН:' + str(*re.findall(r'БИН (.+)', txt))
    
    # Чек 
    CHECK = 'Чек №:' + str(*re.findall(r'Чек №(.+)', txt))
    
    # Адресс компании
    ADDRESS = re.findall(r'г\..+', txt)
    
    # Дата и время
    DATE = re.findall(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', txt)
    
    # Название
    TITLE = re.findall(r'\.\n(.*)', txt)
    
    # Количество
    COUT = re.findall(r'(\d)\,000', txt)
    
    # Цена
    UNIT_PRICE = re.findall(r'\d\,000 x (.*)\,', txt)

# Выводим название компании, БИН, номер чека и ровняем по центру
print('*'*127, '\n\n') 
print(str(*COMPANY_NAME).center(127), '\n')
print(BIN.center(127), '\n')
print(CHECK.center(127))
print('\n\n' + '*'*127)

# Таблица, состоящая из:
# №, название, цена, количество, сумма
TABLE = PrettyTable(['№', 'Название', 'Цена', 'Количество', 'Сумма'])

# Добавляем элементы в таблицу, считаем сумму всех вещей
for n, i in enumerate(TITLE, 0):
    PRICE = int(UNIT_PRICE[n].replace(' ', '')) * int(COUT[n])
    SUM += PRICE
    TABLE.add_row([n + 1, i, UNIT_PRICE[n], COUT[n], PRICE])

# Вывод таблицы, итоговой суммы, адрес, дату и время 
print(TABLE, '\n\n' ,' '*279, 'ИТОГО:',SUM)
print('\n',*ADDRESS, ' '*40 , 'Дата и время:',*DATE)