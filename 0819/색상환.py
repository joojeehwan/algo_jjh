'''


다이나믹

1. 리스트 구조(배열 구조)
EX) DP[?][?]

2. 변인요인이 바뀔 때 계산이 어떻게 되어갈지
(현재 상태 <- 바로 직전 상태들 찾기)



=> dp의 내용을 정의 하는게 중요! 문제의 정의를 생각! 
dp[색의갯수][몇개의 색을 골랐는가] <- 경우의 수





'''



n = int(input())
k = int(input())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003

answer = (dp[n-3][k-1] + dp[n-1][k]) % 1000000003
print(answer)

