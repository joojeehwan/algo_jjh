'''

2xn 타일링 2




0번 비트만 확인하면 짝수 / 홀수 확인이 가능하구나,,!


swea 종이 붙이기 다시 풀고 풀어보자!!

점화식을 세워서 풀어보자!

'''





n = int(input())


dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for col in range(3, 1001):
    dp[col] = 2 * dp[col-2] + dp[col-1]

print(dp[n] % 10007)


