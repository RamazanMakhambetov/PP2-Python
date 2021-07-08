import re

n = int(input())

for i in range(n):
    print('YES') if re.findall(r'^[7-9]\d{9}$', input()) else print('NO')