def Even(inp):
    ans = []
    for i in inp:
        if i % 2 == 0:
            ans.append(i)
    return ans

nums = list(map(int, input().split()))
print(Even(nums))