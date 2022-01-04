'''


구현


치킨배달


치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.


즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.


도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
도시의 치킨거리의 최솟값을 구해야 한다.
'''

#조합


'''
1. 라이브러리 사용 =>

2. 직접 구현하기 


s : 선택 구간의 시작

k : 고른 개수

'''

# def dfs(n, r, s=0, k = 0):
#
#     if k == r:
#         print(*comb)
#     else:
#
#         for i in range(s, n-r+k+1):
#             comb[k] = i
#             dfs(n, r,i + 1, k + 1)
#
#
# N = 5
# R = 3
# comb = [0] * R
#
# dfs(N,R)


'''
치킨집 중에서 M개를 고르는 모든 경우에 대해서 치킨 거리의 합을 계산하여(완전탐색),
치킨 거리의 최소값을 구해 출력하면 된다.

'''


#이코테 풀이

# from itertools import combinations
#
# n, m = map(int, input().split())
#
# #치킨집과 집이 존재하는 좌표가 들어간다.
# chiken, house = [], []
#
# #데이터 입력받아서 넣기
# # 하나의 리스트에 담는게 아니라서 아래와 같이 함! => 한줄씩 받아서 분리!
# for row in range(n):
#     #한줄씩 받아서
#     data = list(map(int, input().split()))
#     for col in range(n):
#
#         if data[col] == 1:
#             house.append((row, col))
#
#         elif data[col] == 2:
#             chiken.append((row, col))
#
# #모든 치킨집 중에서 m개의 치킨을 뽑는 조합 계산
#
# canditates = list(combinations(chiken, m))
#
# #print(canditates)
#
#
# #치킨 거리의 합을 계산하는 함수
#
# def get_sum(caniatae):
#     result = 0
#     #모든 집에 대하여
#     #이 반복이 돌면서 집 하나의 좌표가 나온다
#     #그 집하나에 대해서 m개의 치킨집 모두에 반복돌라면서 가장 가까운 각각의 집에 맞는 치킨집의 찾고
#     #그 거리 값들의 합을 result에 저장하는 것
#     for hx, hy in house:
#         # 가장 가까운 치킨집을 찾기
#         temp = 1e9
#         for cx, cy in caniatae:
#             # 이 for문이 끝나고 나면 하나의 집에 대해서 가장 가까운 치킨집이 temp에 담긴다.
#             temp = min(temp,abs(hx-cx) + abs(hy-cy))
#
#         #가장 가까운 치킨집까지의 거리 더하기
#         result += temp
#     return result
#
# # 치킨 거리의 합의 최소를 찾아 출력!
# # 치킨집의 수많은 조합중에서 가장 적은 길이의 치킨거리를 만드는 것 찾는 것
# res = 1e9
# for canditate in canditates:
#     res = min(res, get_sum(canditate))
#
# print(res)


#dfs로 조합 구현 치킨 좌표 재귀로 빼고 주기


# lst = [1,2,3]
#
# print(lst + [4,5,6])


# def dfs(now, arr):
#
#     global ans
#
#     if len(arr) == m:
#         length = 0
#         for hx, hy in houses:
#             len_house = 987654321
#             for cx, cy in arr:
#                 len_house = min(len_house, abs(hx-cx) + abs(hy -cy))
#             length += len_house
#
#         ans = min(ans, length)
#
#     if now == len(chikens):
#         return
#     de = 1
#     dfs(now+1, arr+[chikens[now]]) #치킨 좌표주고
#     dfs(now+1, arr) #치킨 좌표 다시 빼서!
#
# n, m = map(int, input().split())
#
# chikens, houses = [], []
#
# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(n):
#         if data[j] == 1:
#             houses.append([i, j])
#
#         elif data[j] == 2:
#             chikens.append([i, j])
# ans = 987654231
# dfs(0, [])
# print(ans)


#dfs3

# def length(dist):
#     for i in range(len(home)):
#         h_x, h_y = home[i]
#         for j in range(len(c)):
#             if c[j]:
#                 c_x, c_y = chicken[j]
#                 d = abs(h_x - c_x) + abs(h_y - c_y)
#                 dist[i] = min(d, dist[i])
#     return sum(dist)
#
#
# def comb(idx, cnt, r):
#     global ans
#     if cnt == r:
#         dist = [987654321 for _ in range(len(home))]
#         ans = min(length(dist), ans)
#         return
#
#     for i in range(idx, len(chicken)):
#         if c[i]:
#             continue
#         c[i] = 1
#         comb(i + 1, cnt + 1, r)
#         c[i] = 0
#
#
#
# n, m = map(int, input().split())
# a, chicken, home = [], [], []
# for i in range(n):
#     row = list(map(int, input().split()))
#     a.append(row)
#     for j in range(n):
#         if a[i][j] == 1:
#             home.append([i, j])
#         if a[i][j] == 2:
#             chicken.append([i, j])
#
# c = [0 for _ in range(len(chicken))]
# ans = 987654321
# for r in range(m):
#     comb(0, 0, r + 1)
#
# print(ans)

#bfs로 풀기

import sys
from itertools import combinations
from collections import deque

#하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#chiken m개의 치킨 집 좌표
def bfs(chicken):
    q = deque(chicken)
    for t in chicken:
        dist[t[0]][t[1]] = 0
    tmp = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if temp_MAP[nx][ny] != 2 and dist[nx][ny] == -1:
                        q.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
    de = 1
    for i in range(N):
        for j in range(N):
            if temp_MAP[i][j] == 1:
                tmp += dist[i][j]
    return tmp


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

chiken = []
ans = 987654321
temp_MAP = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            chiken.append((i,j))

        elif MAP[i][j] == 1:
            temp_MAP[i][j] == 1

    for c in combinations(chiken, M):
        dist = [[-1] * N for _ in range(N)]
        ans = min(ans, bfs(list(c)))




#for dfs 

# goal은 폐업하지 않을 치킨집의 수
# dfs_temp는 폐업하지 않는 치킨집의 위치 값 저장
def dfs(goal, idx, dfs_temp):
    global res

    # 탈출 조건
    # 폐업하지 않을 치킨집 다 선택했으면
    if len(dfs_temp) == goal:
        length_temp = 0

        # 폐업하지 않을 치킨집의 위치에 따른
        # 치킨 거리들을 goal_temp에 저장하고
        # 이들 중 최소값을 구해서
        # length_temp에 더한다
        for ee in length:
            goal_temp = []
            for eee in dfs_temp:
                goal_temp.append(ee[eee])

            length_temp += min(goal_temp)

        # res보다 length_temp가 작으면
        # swap
        if res > length_temp:
            res = length_temp

        return

    # dfs
    for e in range(idx, len(shop)):
        dfs(goal, e + 1, dfs_temp + [e])

    return


# n,m
n, m = map(int, input().split())

# 도시
city = [list(map(int, input().split())) for _ in range(n)]

# 집(1)의 위치
house = []

# 치킨집(2)의 위치
shop = []

# 치킨 거리 미리 저장
length = []

# 출력값, 임의의 값
res = 100000

# city를 돌면서 1과 2를 찾아 저장
for q in range(n):
    for w in range(n):
        if city[q][w] == 1:
            house.append([q, w])

        elif city[q][w] == 2:
            shop.append([q, w])

# 치킨 거리를 저장
for qq in house:
    temp = []
    for ww in shop:
        temp.append(abs(qq[0] - ww[0]) + abs(qq[1] - ww[1]))

    length.append(temp)

# 폐업하지 않을 치킨집의 수 == max_num
for max_num in range(1, m + 1):
    dfs(max_num, 0, [])

print(res)