#최소합


# def dfs(row, col, sum = 0):
#
#     global  ans
#
#
#     if row == N - 1 and col == N - 1:
#         ans = min(ans, sum + MAP[row][col])
#         return
#     #오른쪽, 아래
#     dr = [0, 1]
#     dc = [1, 0]
#
#     for i in range(2):
#
#         next_row = row + dr[i]
#         next_col = col + dc[i]
#
#         if not (0<= next_row < N and 0<= next_col < N):
#             continue
#
#         dfs(next_row, next_col, sum + MAP[row][col])
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N = int(input())
#
#     ans = 13278632185
#
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#
#     dfs(0,0)
#
#     print(f"#{tc} {ans}")




#DP 배열을 활용해서 속도를 높임 + return 받는 형식의 dfs




# def dfs(row, col):
#
#     if row == N-1 and col == N-1:
#         return MAP[row][col]
#
#     if DP[row][col] != -1:
#         return DP[row][col]
#
#     ret = 21654837398
#
#     dr = [1, 0]
#     dc = [0, 1]
#     for i in range(2):
#         next_row = row + dr[i]
#         next_col = col + dc[i]
#         if not (0 <= next_row < N and 0 <= next_col < N):
#             continue
#
#         ret = min(ret, dfs(next_row, next_col) + MAP[row][col])
#         # row, col 에서 n-1, n-1까지 갈 때의 비용
#     DP[row][col] = ret
#     return ret
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     DP = [[-1] * (N) for _ in range(N)]
#
#     print(f"#{tc} {dfs(0,0)}")


#전자 카트 => 가지치기


# def dfs(now = 0, cnt = 1, sum = 0):
#
#     global ans
#
#     if cnt == N:
#         ans = min(ans, sum + MAP[now][0])
#         return
#
#     if sum >= ans: #어차피 가지 않아도 되는 곳들을 가지 않게 만듬!
#         return
#
#     for next in range(1, N):
#         if check[next]:
#             continue
#         check[next] = True
#         dfs(next, cnt + 1, sum + MAP[now][next])
#         check[next] = False
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#
#     check = [False] * (N)
#     ans = 2165378378
#     dfs()
#     print(f"#{tc} {ans}")




# t = int(input())
# for tc in range(t):
#     n, m = map(int, input().split())
#     weight = list(map(int, input().split()))
#     truck = list(map(int, input().split()))
#     weight.sort(reverse = True) #내림차순 정렬
#     truck.sort(reverse = True) #내림차순 정렬
#     # sort 시간 복잡도 nlogn
#
#     print(weight, truck)
#     w_idx = 0 # 화물 index
#     t_idx = 0 # 트럭 index
#     ans = 0 # 실은 화물들의 무게
#
#     # 제일 용량이 큰 트럭           1개당
#         # 제일 용량이 큰 화물    n개의 화물
#                         #총 O(m * n)
#
#     #if 절에 들어가지 못하는 것들은 무게가 너무 커서 적재용량을 초과 하는 것들
#     while w_idx < n and t_idx < m:
#         if weight[w_idx] <= truck[t_idx]:
#             # 화물을 실을 수 있음
#             ans += weight[w_idx]
#             t_idx += 1
#         w_idx += 1=
#
#     print(f"#{tc + 1} {ans}")



'''

dfs를 구현하면서 더 집중해야 할 부분,,!


1) check , visited 배열 만들어서 이미 간 곳 안간다!

2) DP 배열 적용

3) return 형으로 함수 만들기

'''

import sys


sys.setrecursionlimit(int(1e7))



# def dfs(row = 11, col = 11):
#     global success
#
#
#     if not success:
#         return 0
#     if MAP[row][col] == 0 :
#         return 0
#
#
#     if DP[row][col] != -1:
#         return DP[row][col]
#
#
#     dr = [-1, 1, 0, 0]
#     dc = [0 ,0, -1, 1]
#
#     ret = 0 #최대를 구하는 것,,,
#
#     for i in range(4):
#         next_row = row + dr[i] * MAP[row][col]
#         next_col = col + dc[i] * MAP[row][col]
#
#         if check[next_row][next_col] : #이미 기록이 있는 점을 가게 된다면 싸이클!
#
#             success = False
#             return 0
#
#         check[next_row][next_col] = True
#         ret = max(ret, dfs(next_row, next_col) + 1)
#         check[next_row][next_col] = False
#
#     DP[row][col] = ret
#
#     return ret
#
#
# N, M = map(int, sys.stdin.readline().split())
#
#
# MAP = [[0] * (22 + M) for _ in range(22 + N)]
# check = [[False] * (22 + M) for _ in range(22 + N)]
# DP = [[-1] * (22 + M) for _ in range(22 + N)]
# success = True
#
# temp_MAP = [list(sys.stdin.readline()) for _ in range(N)]
#
# for row in range(N):
#     for col in range(M):
#         if temp_MAP[row][col] == "H":
#             MAP[row + 11][col + 11] = 0 # 장외와 구멍을 모두 0으로!
#
#         else:
#             MAP[row + 11][col + 11] = int(temp_MAP[row][col]) #숫자는 숫자로




# 돌다리 건너기


# import sys
#
# def dfs(row, col, cnt):
#
#     if cnt >= len(op):
#         return 1
#
# #반환 받는 구조
#
#     for next_col in range(col + 1, len(MAP[next_row])):
#
#
#
#
#
#
# op = sys.stdin.readline()
#
# MAP = [sys.stdin.readline() for _ in range(2)]
#
# DP = [[-1] * len(op) for _ in range(len(MAP[0])) for _ in range(2)]






