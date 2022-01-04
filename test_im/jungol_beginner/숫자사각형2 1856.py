





#짝수행, 홀수행 나누어서 생각해야 함!
# 와리가리 출력! 아 이거 뭐더라,,!

#높이 n, 너비 m


n, m = map(int, input().split())

MAP = [[0] * m for _ in range(n)]


num = 1
for row in range(n):
    if row % 2 == 0:
        for col in range(m):
            MAP[row][col] = num
            num += 1

    else:
        for col in range(m-1, -1, -1):
            MAP[row][col] = num
            num += 1

for row in range(n):
    for col in range(m):
        print(MAP[row][col], end = " ")

    print()
















