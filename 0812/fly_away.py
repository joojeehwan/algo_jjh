

#연달아 m개의 행을 보면서 m개씩 묶어서 합을 구하고 가장 큰것을 찾는다...!

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    square = [list(map(int, input().split())) for _ in range(N)]

    maxi = 0 # 최종적인 최대합을 구하기 위해서!
    for i in range(N-M+1):00
        for j in range(N-M+1):
            current = 0 # 이중 포문을 통해서 사격형이 형성될때마다 합을 임시 저장!
            for k in range(M):
                for l in range(M):
                    current += square[j+l][i+k]
            if current > maxi: #여기에 If문 있는거!
                maxi = current
    print('#{} {}'.format(tc, maxi))


# 이차원 배열에서 포문 하나의 의미는 검색을 들어가기 위함이라고 생각하면 좋다!
'''
파리퇴치 방법2

프리픽스를 2차원으로 확장




'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    MAP = [[0 for _ in range(N + 1)]]
    for i in range(N):
        MAP += [[0] + list(map(int, input().split()))] #왜 입력을 이렇게 받지?! dp에서 -m 이런거 할때 음수 되서!
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + MAP[row][col]

    ans = 0
    for row in range(M, N + 1):
        for col in range(M, N + 1):
            sum = dp[row][col] - dp[row - M][col] - dp[row][col - M] + dp[row - M][col - M]
            if ans < sum:
                ans = sum

    print("#{} {}".format(tc + 1, ans))
N = 5
MAP = [[0 for _ in range(N + 1)]]

for i in range(N):
    MAP += [[0] + [1,23,4,5,6]]

dp = [[0] * (N+1) for _ in range(N + 1)]
print(dp)