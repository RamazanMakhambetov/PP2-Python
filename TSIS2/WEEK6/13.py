def pascal_triangle(n):
    trow, y = [1], [0]
    
    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    return n >= 1

lines = int(input())
pascal_triangle(lines)