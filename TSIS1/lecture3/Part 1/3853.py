loop = list(map(int, input().split()))
steps = int(input()) % len(loop)
print(*loop[-steps::] + loop[:-steps])