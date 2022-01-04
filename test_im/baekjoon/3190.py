'''



뱀


와 이 문제를 큐를 쓸 생각을 어케 하지? 그냥 단순히 델타 배열 사용하는게 아닌가벼,,,

아 아직 멀었다... 실력,,


'''


from collections import deque

def turn_dir(d,c):

    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


N = int(input())

apple_count = int(input())
# 그래프 구성
MAP = [[0] * N for _ in range(N)]

#사과가 있는 장소 "1"로 표시
for _ in range(apple_count):
    row , col = map(int, input().split())
    MAP[row-1][col-1] = 1

L = int(input())

snake_sec_dir = []
for _ in range(L):
    sec, dir = input().split()
    snake_sec_dir.append((int(sec), dir))

#방향 동쪽
direction = 0

time = 0

turn = 0

#큐 생성
q = deque()

#시작점 세팅
now_row, now_col = 0, 0

MAP[now_row][now_col] = 2

q.append([now_row, now_col])

#맵 자체를 비지트 배열로 사용! / 뱀이 현재 있는 위치 2로 표시


#동남서북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while True:

    now_row, now_col = q[-1]

    next_row = now_row + dr[direction]
    next_col = now_col + dc[direction]

    time += 1
    #벽
    if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
        break
    #자기 몸
    if MAP[next_row][next_col] == 2:
        break

    # 사과가 있는 경우 
    if MAP[next_row][next_col] == 1:
        MAP[next_row][next_col] = 2

    #사과가 없는 경우 
    if MAP[next_row][next_col] == 0:
        MAP[next_row][next_col] = 2
        temp_row, temp_col = q.popleft()
        MAP[temp_row][temp_col] = 0

    q.append([next_row, next_col])

    #영호 풀이 참고
    if turn < L and time == snake_sec_dir[turn][0]:
        direction = turn_dir(direction, snake_sec_dir[turn][1])
        turn += 1


print(time)
        





    





