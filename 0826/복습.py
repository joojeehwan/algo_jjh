'''



미로의 거리 에서 알아야하는 3가지

값을 찾는 3가지의 방법,,!

'''

# import sys
#
# sys.stdin = open("미로의 거리_input.txt")
#
#
#
# from collections import deque
#
#
# T = int(input())
#
#
# for tc in range(1, T+1):
#
#     N = int(input())
#     MAP = [list(map(int, input().rstrip())) for _ in range(N)]
#
#     #1. 그래프 구성
#
#
#     #2. 큐 생성
#     q = deque()
#     visited = [[0] * N for _ in range(N)]
#
#     #3. 시작점 세팅
#
#     for row in range(N):
#         for col in range(N):
#             if MAP[row][col] == 2:
#                 visited[row][col] = 1
#                 q.append([row, col]) #좌표라서 q에 append할때도 튜플로해서 셋트로 넣어버러기,,!
#
#
#     #7. 4 ~ 6단계 반복
#
#     while q :
#         # 4. now 꺼내기
#         now = q.popleft()
#         now_row = now[0]
#         now_col = now[1]
#
#
#         #5.now -> next찾기
#
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#
#         for i in range(4):
#             next_row = now_row + dr[i]
#             next_col = now_col + dc[i]
#
#             if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
#                 continue
#
#             if MAP[next_row][next_col] == 1:
#                 continue
#
#             if visited[next_row][next_col] != 0 :
#                 continue
#
#
#             ##6. next를 큐에 추가
#
#             visited[next_row][next_col] = visited[now_row][now_col] + 1
#
#             q.append([next_row, next_col])
#
#     ans = -1 # 0도 의미가 있어서! 갈 수 있다는!
#     for row in range(N):
#         for col in range(N):
#             if MAP[row][col] ==3 :
#                 ans = visited[row][col] - 2
#
#     if ans < 0:
#         print("#{} 0".format(tc))
#     else:
#         print("#{} {}".format(tc, ans))


from collections import deque
import sys

N, M, X = map(int, sys.stdin.readline().split())
data_up = [[] for _ in range(N + 1)] # 더 잘본 애들   #두개의 dfs를 한다는게 point! 방향이 다르니깐!
data_down = [[] for _ in range(N + 1)] # 더 못본 애들

for _ in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    data_down[A].append(B)
    data_up[B].append(A)


q = deque()

visted = [0] * (N+1)

visted[X] = 1
q.append(X)

cnt = 0
while q:

    now = q.popleft()
    cnt += 1  # 나우에서 꺼내는 것들이! 나보다 못하는 녀석들이니깐! 인접해 있는 녀석들을 다 큐에 넣었다가 빼니깐!
                    # 여기서 카운트를 센다

    for next in data_down[now]:
        if visted[next]!=0:
            continue

        visted[next] = 1
        q.append(next)

ans1 = N - cnt + 1


