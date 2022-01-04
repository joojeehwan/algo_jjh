'''



자리배정



1) 달팽이 숫자에서 한 기법으로 배치하고 

2) 이차원 배열에서 해당 값의 위치를 찾고

3) 출력에 맞게 출력값 수정

#시간 초과 나는구나,,! 이렇게 하면 안듸!
'''


def seat_count(c, r, k, lst):  # 자리 찾기 함수
    x, y = r - 1, 0            # 리스트[리스트] 에서 (x,y) 는 lst[y][x]
    movex = [-1, 0, 1, 0]      # 위 - > 오른쪽 - > 아래 - > 왼쪽
    movey = [0, 1, 0, -1]
    direc = 0
    cnt = 1   # 입력용 숫자
    while True:
        nx = x + movex[direc]    # next x
        ny = y + movey[direc]    # next y
        if cnt == k:    # 자리가 다 돌았으면
            return y + 1, r - x   # x, y 반환
        if nx < 0 or nx >= r or ny < 0 or ny >= c or lst[nx][ny] != 0:  # 범위 밖으로 나가거나, 이미 자리가 있다면
            direc += 1      # 방향 전환
            direc %= 4      # 0: 3 순환
        else:
            lst[x][y] = cnt
            x = nx
            y = ny
            cnt += 1

c, r = map(int, input().split())
k = int(input())
if r * c < k:
    print(0)
else:
    lst = [[0] * c for _ in range(r)]
    result = seat_count(c, r, k, lst)
    print(result[0], result[1])

##########

C, R = map(int, input().split())

customer = int(input())

if customer > C*R:
    print(0)

else:
    #데이터 전처리 => 장외인 부분을 -1로
    MAP = [[-1] * (C+2) for _ in range(R+2)]

    for row in range(1, R+1):
        for col in range(1,C+1):
            MAP[row][col] = 0

    # print(MAP)
    #시작값 세팅

    start_row = C
    start_col = 1

    #상 우 하 좌

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    #방향
    dir = 0

    cnt = 1

    while cnt != customer:

        next_row = start_row + dr[dir]
        next_col = start_col + dc[dir]

        if MAP[next_row][next_col] != 0 :

            dir = (dir + 1) % 4

        else:
            start_row = next_row
            start_col = next_col
            MAP[start_row][start_col] = cnt
            cnt += 1


    print(f"{start_row+(R-1)} {start_col+1}")



