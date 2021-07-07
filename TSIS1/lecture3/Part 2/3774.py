parent_tree, family_set, n = {}, set(), int(input())

for i in range(1, n):
    family = list(map(str, input().split()))

    if family[1] not in parent_tree.keys():
        parent_tree[family[1]] = family[0].split()
    else:
        parent_tree[family[1]] += family[0].split()

while n // 2 > 0:
    n -= 1
    for key, value in parent_tree.items():
        for i in range(len(value)):
            family_set.add(key)
            family_set.add(value[i])
            if value[i] in parent_tree.keys():
                parent_tree[key] += parent_tree[value[i]]

family_list = list(family_set)
family_list.sort()

for i in range(len(family_list)):
    if len(set(''.join([
        str(len(set(value))) if family_list[i] == key else '0'
            for key, value in parent_tree.items()]))) > 1:
        print(family_list[i], *sorted(set(''.join([
            str(len(set(value))) if family_list[i] == key else '0'
            for key, value in parent_tree.items()])))[1])
    else:
        print(family_list[i], '0')