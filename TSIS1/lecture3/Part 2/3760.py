n = int(input())
synonym = {}

for i in range(n):
    key, value = input().split()
    synonym[key] = value
search = input()

print(synonym[search]) if search in synonym else print(list(synonym.keys())
                                                       [list(synonym.values()).index(search)])