dp = [[0]*1000 for _ in range(100)]

# 주의 사항 : 맨 처음 <- 직접 세팅

dp[0][0] = 1

for row in range(1,100):
    for col in range(100):
        dp[row][col] = dp[row-1][col] + dp[row - 1][col - 1]

T = int(input())

for tc in range(T):
    N = int(input())
    print("#{}".format(tc + 1))
    for row in range(N):
        for col in range(row + 1):
            print("{} ".format(dp[row][col]), end = "")
        print("")