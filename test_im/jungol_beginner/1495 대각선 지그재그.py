'''
<생각하기>

이동 순서를 잘 생각해보면 다음과 같이 4가지 형태가 반복된다.

1) 아래로 한 번 이동 (불가능하면 오른쪽으로)

2) 오른쪽 위로 가능한 만큼 이동 (가장 위나 가장 오른쪽에 도달하면 종료)

3) 오른쪽으로 한 번 이동 (불가능하면 아래로)

4) 왼쪽 아래로 가능한 만큼 이동 (가장 왼쪽이나 가장 아래쪽에 도달하면 종료)


하  -> 우상 -> 우 -> 좌하 의 반복
'''



N = int(input())

MAP = [[0] * N for _ in range(N)]

#하, 우상, 우, 좌하
dr = [1, -1, 0, 1]
dc = [0, 1, 1, -1]
value = 1
row, col = 0, 0
MAP[row][col] = value


for _ in range(N-1):
    for i in range(4):
        if i == 0:
            value += 1
            #아래로 갈 수 있다면!
            if 0 <= row + dr[0] < N and 0 <= col + dc[0] < N :
                row = row + dr[0]
                col = col + dc[0]
                MAP[row][col] = value
            #아래로 못가면 오른쪽으로 가야함
            else:
                row = row + dr[2]
                col = col + dc[2]
                MAP[row][col] = value


        elif i == 1:
            #우상으로 끝까지!
            while 0<= row + dr[1] < N and 0 <= col + dc[1] < N :
                value += 1
                row = row + dr[1]
                col = col + dc[1]
                MAP[row][col] = value

        elif i == 2:
            value +=1
            if  0 <= row+dr[2] < N and 0 <= col + dc[2] < N:
                row = row + dr[2]
                col = col + dc[2]
                MAP[row][col] = value

            else:
                row = row + dr[0]
                col = col + dc[0]
                MAP[row][col] = value

        elif i == 3:
            while 0 <= row + dr[3] < N and 0 <= col + dc[3] < N :
                value += 1
                row = row + dr[3]
                col = col + dc[3]
                MAP[row][col] = value


for lst in MAP:
    print(*lst)