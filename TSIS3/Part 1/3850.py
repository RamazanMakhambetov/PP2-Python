arr = list(map(int, input().split()))
print(*[arr[i] for i in range(len(arr)) if arr[i] != 0],
      *[arr[i] for i in range(len(arr)) if arr[i] == 0])