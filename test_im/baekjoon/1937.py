'''

욕심쟁이 판다.



'''

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


n = int(input())

MAP = [list(map(int, input().split())) for _ in range(n)]
'''
이렇게 해도 됨
MAP = []

for i in range(n):
    tmp = list(map(int, input().split()))
    MAP.append(tmp)
'''

dp = [[0] * n for _ in range(n)]
'''
dp = [[0 for _ in range(n)] for _ in range(n)]

'''
#동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(row, col):

    if dp[row][col] != 0:
        return dp[row][col]

    dp[row][col] = 1 #처음 시작에 1 넣고!

    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
            continue


        if MAP[next_row][next_col] > MAP[row][col]:
            dp[row][col] = max(dp[row][col], dfs(next_row, next_col) + 1)
        '''
        if (0 <= next_row < n) and (0 <= next_col < n) and MAP[next_row][next_col] > MAP[row][col]:
            이렇게도 가능
        
        '''
    return dp[row][col]


res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))

print(res)