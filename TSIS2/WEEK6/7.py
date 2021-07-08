def Upper_Lower(inp):
    cnt_lower, cnt_upper = 0, 0
    for i in inp:
        if 'A' <= i <= 'Z':
            cnt_upper += 1
        elif 'a' <= i <= 'z':
            cnt_lower += 1
    print(f'Number of upper case characters: {cnt_upper}')
    print(f'Number of lower case characters: {cnt_lower}')

str = input()
Upper_Lower(str)