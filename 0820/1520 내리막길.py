

'''


와 이거 풀이 신박,,

visetd를 중복하게 기록해서 결국의 경로의 수를 알아낸다!



'''


import sys
limit_number = 30000
sys.setrecursionlimit(limit_number)# 재귀 횟수 제한 해제

def dfs(row, col) : # row, col <- 현재 점의 위치(now)
    # 반환값 : dp값(현재 좌표에서 도착지까지의 값(경로의 수) )
    # now -> next
    if row == h-1 and col == w-1:
        return 1# 원하는 목적지까지 왔으면 더 갈 필요 없이 끝!
    if dp[row][col] != -1:
        # 계산한 결과가 있다!
        return dp[row][col]
    # 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    ret = 0 # row, col에서 도착지까지 경로의 수
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w:
            continue # 맵을 벗어나는 좌표이면 무시
        if MAP[row][col] <= MAP[next_row][next_col]:
            continue # 내리막길로만 가야 하니, 더 높거나 같으면 갈 수 없다.
        visited[next_row][next_col] = visited[next_row][next_col] + 1
        ret += dfs(next_row, next_col)
        # next방향으로 갈때의 경로 개수를 받아서 누적
    dp[row][col] = ret # 결과 기록
    return ret

h, w = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(h)]
visited = [[0] * w for _ in range(h)] # 갔던 점을 기록
dp = [[-1] * w for _ in range(h)]
# dp[row][col] : row,col에서부터 목적지까지의 경로 개수
# 0도 계산된 값일 수 있으니 -1로 초기화(-1 : 아직 계산해보지 않은 값이라는 의미)

visited[0][0] = 1
print(dfs(0,0))

de = 1