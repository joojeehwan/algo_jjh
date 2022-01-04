'''

정사각형 방


DP 배열,, 현재 위치에서 앞으로 최대한 이동할 수 있는 개수를 담은,,!


'''



def dfs(row, col, cnt):

    global ans

    ans = max(ans, cnt)

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    for i in range(4):

        next_row = row + dr[i]
        next_col = col + dc[i]

        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
            continue

        if MAP[next_row][next_col] == MAP[row][col] + 1:

            dfs(next_row, next_col, cnt + 1)

    #base 조건을 어떻게 설정해야 하지?! for문이 끝나면 저절로,,,!


T  = int(input())

for tc in range(1, T+1):

    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    dfs(0,0,0)

    print(ans)



################


#정사각형방

# 최대 얼마나 갈 수 있느냐!

def dfs(row, col):
    # row, col에서 부터 최대한 갈 수 있는 횟수
    if dp[row][col] != -1:
        # 내가 계산한적이 있다.
        return dp[row][col]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    ret = 1
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if not(0 <= next_row < n and 0 <= next_col < n):
            continue # 맵을 벗어나는 좌표면 무시
        if MAP[next_row][next_col] != MAP[row][col] + 1:
            continue # 현재방보다 다음방이 정확히 1이 크지 않은 경우 무시
        ret = max(ret, dfs(next_row, next_col) + 1)
        # next_row, next_col에서 부터 최대한 갈 수 있는 횟수
    dp[row][col] = ret
    return ret


t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    ans_cnt = 0 # 전체에서 최대한 갈 수 있는 횟수
    ans_num = -1 # 최대한 갈 수 있는 횟수를 갖는 방 중 적힌수가 가장 작은 값
    dp = [[-1] * n for _ in range(n)]
    # dp[row][col] : row,col에서 최대한 '갈 수 있는 횟수'
    for i in range(n):
        for j in range(n):
            cnt = dfs(i, j) # i, j에서부터 최대한 얼마나 갈 수 있는가?
            if ans_cnt < cnt:
                ans_cnt = cnt
                ans_num = MAP[i][j]
            elif ans_cnt == cnt and ans_num > MAP[i][j]:
                ans_num = MAP[i][j]
    print(f"#{tc + 1} {ans_num} {ans_cnt}")












