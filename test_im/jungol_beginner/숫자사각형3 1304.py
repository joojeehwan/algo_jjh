

n = int(input())


num = 1

MAP = [[0] * n for _ in range(n)]

for row in range(n):
    for col in range(n):
        MAP[col][row] = num
        num += 1

for row in range(n):
    for col in range(n):
        print(MAP[row][col], end = " ")

    print()



