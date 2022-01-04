

#바로이전과 현재만 생각!

#dfs 풀이
def dp(n):
    if n == 10:
        return 1

    elif n == 20:
        return 3

    return dp(n-10) + 2*dp(n-20)


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    print(f"#{tc} {dp(N)}")




#dp 풀이
dp = [0] * 301

dp[1] = 1
dp[2] = 3

for col in range(3, 301):
    dp[col] = dp[col - 1] + 2 * dp[col - 2]

T = int(input())
for tc in range(T):
    N = int(input())
    print("#{} {}".format(tc + 1, dp[N // 10]))