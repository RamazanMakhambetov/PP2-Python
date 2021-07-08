import re

n = int(input())

def floating_test(inp):
    if inp[0] == '.' or '0' <= inp[0] <= '9':
        pass
    else:
        inp = inp[1::]

    if inp[0] != '.':
        if str(inp) == str(*re.findall(r'[0-9]+\.[0-9]+', inp)):
            return True
        else:
            return False
    
    else:
        if inp == str(*re.findall(r'\.[0-9]+', inp)):
            return True
        else:
            return False

for i in range(n):
    print(floating_test(input()))