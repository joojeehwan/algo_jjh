

N = int(input())


#이차원 배열 만들기! 한 층위를 -1로 둘러싸기
MAP = [[-1] * (N + 2) for _ in range(N + 2)]


#사방의 한층위의 -1들을 제외하고 사각형에만 값을 넣어야 해서 1 ~ N + 1 인것!

for row in range(1, N + 1):
    for col in range(1, N + 1):
        MAP[row][col] = 0

# 우 하 좌 상으로 이동해야 함!

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

row = 1
col = 0

dir = 0

cnt = 1

while cnt <= N * N:

    next_row = row + dr[dir]
    next_col = col + dc[dir]


    if MAP[next_row][next_col] != 0:
        dir = (dir + 1) % 4


    else:

        row = next_row
        col = next_col
        MAP[row][col] = cnt
        cnt += 1


for row in range(1, N + 1):
    for col in range(1, N + 1):
        print(f"{MAP[row][col]}", end=" ")

    print("")


