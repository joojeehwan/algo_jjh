'''



DP[row][col]

row , col -> 갈수 있는 데 까지 최대 횟수
(반환 받아서 계산을 처리 )

뒤에를 확정?!

'''

def dfs(row, col, cnt ):


    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    for i in range(4):
        next_row = row + dr[i] * int(MAP[row][col])
        next_col = col + dc[i] * int(MAP[row][col])

        #장외 + 구멍이 있는 H를 만나면
        if not (0 <= next_row < N and 0 <= next_col < N) or MAP[row][col] == "H":
            return 0

        dfs(next_row, next_col, cnt + 1)



# 아 자꾸 까먹는다 비지트 배열,,,, 중복해서 가지 않게 하자! 아 근데 이건 원래 기본형은 아니야!




N, M = map(int, input().split())


MAP = [list(input().split()) for _ in range(N)]


cnt = 0

dfs(0,0)

print(cnt)



# 백준 게임 1103

'''

이 풀이의 포인트는 데이터를 입력받아서 전처리 하는 부분! 나가는 부분이나 구멍에 빠져서 아웃되는 상황모두 "0"으로 단순화

'''
import sys

sys.setrecursionlimit(int(1e7))

def dfs(row = 11, col = 11):
    global success
    if not success:
        # 불가능한 상태면 아무것도 하지 말고 끝내라
        return 0
    if MAP[row][col] == 0:
        # 구멍이거나 맵 밖으로 벗어났다.
        return 0
    if DP[row][col] != -1:
        # 기록된게 있으면
        return DP[row][col]

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    ret = 0
    for i in range(4):
        next_row = row + dr[i] * MAP[row][col]
        next_col = col + dc[i] * MAP[row][col]
        if check[next_row][next_col] :
            # 이미 기록이 있으면 갔던 점을 다시 가는 것이니 사이클을 이루게 된다.
            success = False # 무한하게 반복하여 불가능한 상태
            return 0
        check[next_row][next_col] = True
        ret = max(ret, dfs(next_row, next_col) + 1)
        check[next_row][next_col] = False # 기록 삭제(다른 경로로도 갈 수 있도록 구성)
    DP[row][col] = ret
    return ret


H, W = map(int, sys.stdin.readline().split())
MAP = [[0] * (22 + W) for _ in range(22 + H)]
DP = [[-1] * (22 + W) for _ in range(22 + H)]
check = [[False] * (22 + W) for _ in range(22 + H)]
success = True
temp_MAP = [list(sys.stdin.readline()) for _ in range(H)]
for row in range(H):
    for col in range(W):
        if temp_MAP[row][col] == 'H':
            MAP[row + 11][col + 11] = 0
        else:
            MAP[row + 11][col + 11] = int(temp_MAP[row][col])

ans = dfs()
if success:
    print(ans)
else:
    print(-1)