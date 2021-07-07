n, m = map(int, input().split())
n_arr, m_arr = [], []

[n_arr.append(int(input())) for i in range(n)]
[m_arr.append(int(input())) for i in range(m)]

print(len(set(n_arr) & set(m_arr)))
print(*sorted(set(n_arr) & set(m_arr)))
print(len(set(n_arr) ^ set(set(n_arr) & set(m_arr))))
print(*sorted(set(n_arr) ^ set(set(n_arr) & set(m_arr))))
print(len(set(m_arr) ^ set(set(n_arr) & set(m_arr))))
print(*sorted(set(m_arr) ^ set(set(n_arr) & set(m_arr))))