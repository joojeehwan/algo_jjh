'''


bfs로 풀어보자!


w가 있는 곳이 시작점!



for _ in range(N):
    MAP.append(input())

이 부분에서 list로 할 필요가 없다 수정할 것이 아니기 때문에! 조회만 한다!

tip)
visited를 -1로 초기화를 했는데, 이는 W가 있는 위치는 0으로 만들어야 최소거리가 구해지기 때문이다.


=> 0으로 초기화 하고 물이 있는 곳을 1로 한다면 사각형 크기 만큼 빼주어야 한다!
'''

from collections import deque
import sys




T = int(input())

for tc in range(1, T+1):

    # 1 그래프 구성
    N, M  = map(int, input().split())
    MAP = []

#여기서 굳이 list()로 받을 필요가 없다! 왜냐면 수정할것이 아니다!
#list로 입력받게 되면 괜히 시간만 더 손해
    for _ in range(N):
        MAP.append(input())


    visited = [[0] * M for _ in range(N)]

    #원래 보통은
    #MAP = [list(map(int, input().split())) for _ in range(N)] 이렇게 2차원 배열 입력받는다!

    # 2 queue 생성

    q = deque()

    #3 시작점 세팅
    for row in range(N):
        for col in range(M):
            if MAP[row][col] == "W":
                q.append((row, col))
                visited[row][col] = 1


    ans = 0
    #7 큐가 비어질때까지 4 ~ 6단계 반복
    while q:

    #4 큐에 가장 앞에 있는 것 뽑기
        now = q.popleft()
        now_row = now[0]
        now_col = now[1]
        ans += visited[now_row][now_col]

    #5 next를 찾기 (델타 배열)
        #상하좌우
        dr = [-1, 1, 0, 0]
        dc = [0 , 0, -1, 1]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue

            if visited[next_row][next_col] != 0 :
                continue

            if MAP[next_row][next_col] == "W":
                continue

            #6 next를 큐에 추가하기
            visited[next_row][next_col] = visited[now_row][now_col] + 1
            q.append((next_row, next_col))

    #
    # ans = 0
    # for row in range(N):
    #     for col in range(M):
    #         ans += visited[row][col]


    print("#{} {}".format(tc, ans - (N*M)))



#직접 선형큐 만들어서 하는 풀이,, 오오 신기하구만!

'''

Q의 크기가 애매하면 십만에서 백만 정도 곱해서,, 배열 크기 만든다

사진은 선형큐 연산...

원형큐는 모듈러 연산을 해야해


'''












