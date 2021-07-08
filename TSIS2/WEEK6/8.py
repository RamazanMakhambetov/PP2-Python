def Unique(L):
    return set(L)

inp = list(map(int, input().split()))

print(list(Unique(inp)))