# 장훈이의 높은 선반

def dfs(now, sum):
    global ans

    if b <= sum:  # b이상인 인간탑 중
        ans = min(ans, sum)  # 최솟값 기록
        return  # 가지치기 포함 : ans < sum : ans은 항상 b보다 크므로 이 if문에 항상 들어올 수 있다.

    if now >= n:
        # 모든 사람에 대해서 확인이 끝!
        return

    # 1. 뽑는다.
    dfs(now + 1, sum + height[now])
    # 2. 뽑지 않는다.
    dfs(now + 1, sum)


t = int(input())
for tc in range(t):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))

    ans = 2134567890
    dfs(0, 0)
    print(f"#{tc + 1} {ans - b}")