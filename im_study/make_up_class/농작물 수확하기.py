



T = int(input())



for tc in range(1, T+1):

    N = int(input())
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]
    mid = N // 2
    flag = -1
    ans = 0

    for row in range(N):
        if row >= N//2:
            flag = 1
        for col in range(abs(row-N//2), abs(N - mid)): #앞에 abs안 괄호는 바뀌면 안되니깐!
            ans += MAP[row][col]
        mid += flag

    print('#{} {}'.format(tc, ans))

T = int(input())

for tc in range(1, T + 1):
    # 농장의 한 변의 길이
    N = int(input())
    # 농장 만들기
    board = [list(map(int, (' '.join(input().rstrip())).split())) for _ in range(N)]

    # 얻을 수 있는 수익
    result = 0

    # 계산하는 칸의 변동성을 위한 변수
    k = 0

    # 맨 위부터 중간 바로 직전까지
    for i in range(N // 2):
        for j in range(N // 2 - k, N // 2 + k + 1):
            result += board[i][j]
        k += 1

    # 중앙부터 맨 아래까지
    for i in range(N // 2, N):
        for j in range(N // 2 - k, N // 2 + k + 1):
            result += board[i][j]
        k -= 1

    # 결과 출력
    print('#{} {}'.format(tc, result))



