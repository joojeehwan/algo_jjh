


T = int(input())


def dfs(current, tmp):
    global res
    if tmp < res:
        if 0 not in visited[1:]:
            res = min(res, tmp + a[current][0])
            return
        for next in range(1, N):
            if a[current][next] != 0 and visited[next] == 0:
                visited[next] = 1
                dfs(next, tmp + a[current][next])
                visited[next] = 0


for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    res = 10000
    for i in range(1, N):
        visited = [0] * N
        visited[i] = 1
        dfs(i, a[0][i])
    print("#{} {}".format(tc, res))



# if - 조건으로 가지치기를 한다 => 이 생각,,!



# 전자카트


def dfs(now = 0, cnt = 1, sum = 0):
    global ans
    if cnt == n :
        ans = min(ans, sum + MAP[now][0])
        return
    if sum >= ans:
        return # 가지치기
    for next in range(1, n):
        if check[next]:
            continue # 이미 갔던 점이면 무시
        check[next] = True
        dfs(next, cnt + 1, sum + MAP[now][next])
        check[next] = False

# 전에 했던 경로

t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [ list(map(int, input().split())) for _ in range(n)]
    # index : 0~n-1
    # 본래 1~n번에서 1씩 빼서 사용
    check = [False] * (n)
    ans = 2134567890
    dfs()
    print(f"#{tc + 1} {ans}")
