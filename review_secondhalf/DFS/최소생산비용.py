'''

dfs를 활용한 순열의 문제!




'''

def dfs(idx, sum):


    global ans

    if idx == N:
        ans = min(ans, sum)

    if sum >= ans:
        return

    for i in range(N): #공장의 수 만큼,,!
        if visited[i] == 0 : #가지 않는 곳만 가자!
            visited[i] = 1
            dfs(idx + 1, sum + cost[idx][i])
            visited[i] = 0 #순열이니깐 갓다가 다시 와서 확ㅇ린해야 하나잔 !



T = int(input())


for tc in range(1, T + 1):

    N = int(input())

    cost = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321

    visited = [0] * N

    dfs(0,0)

    print(f"#{tc} {ans}")