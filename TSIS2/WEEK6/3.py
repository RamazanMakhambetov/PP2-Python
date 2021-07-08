def Product_List(inp):
    ans = 1
    for i in inp:
        ans *= i
    return ans

inp = list(map(int, input().split()))

print(Product_List(inp))