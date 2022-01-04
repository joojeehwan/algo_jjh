'''

dfs + 가지치기(백트래킹)



'''



# 전기버스2(dp, dfs)
# 2가지 방법
# 1. dp
# 2. 가지치기

def dfs(now):
    # now이후로 목적지까지 교환해야하는 최소 횟수
    if now >= n - 1:
        return 0
    if dp[now] != -1:
        return dp[now]
    ret = 2134567890
    for next in range(now + 1, now + chs[now] + 1):
        ret = min(ret, dfs(next) + 1)
    dp[now] = ret
    return ret

t = int(input())
for tc in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    chs =  data[1:]
    dp = [-1] * n
    ans = 2134567890

    print(f"#{tc + 1} {dfs(0) - 1}")



# 전기버스2 (가지치기)
# 2가지 방법
# 1. dp
# 2. 가지치기

def dfs(now, cnt = -1):
    global ans
    # now : 현재 위치
    if cnt >= ans:
        return

    if now >= n - 1:
        ans = min(ans, cnt)
        return

    for next in range(now + 1, now + chs[now] + 1):
        dfs(next, cnt + 1)


t = int(input())
for tc in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    chs =  data[1:]
    ans = 2134567890
    dfs(0)
    print(f"#{tc + 1} {ans}")


# 전기버스2(dp, for)
# dfs 2가지 방법
# 1. dp
# 2. 가지치기

# dp : 2가지 방법
# 1. dfs
# 2. for

t = int(input())
for tc in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    chs =  data[1:]
    dp = [2134567890] * (n + 100)
    dp[0] = 0
    for now in range(len(chs)):
        for next in range(now + 1, now + chs[now] + 1):
            dp[next] = min(dp[next], dp[now] + 1)

    print(f"#{tc + 1} {dp[n - 1] - 1}")