#dfs


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









T = 10
for tc in range(T):
    N= int(input())
    size = 100
    str_list = [input() for _ in range(size)]

    for i in range(size):
        # i : 가로 기준점
        temp = ""
        for j in range(size):
            # j : 세로 줄 번호
            temp += str_list[j][i]
        str_list.append(temp)

    ans = 0
    flag = 0 # 찾았는가?
    for M in range(size, 1, -1):
        for str_temp in str_list:
            for i in range(size - M + 1):
                temp = str_temp[i:i + M] # i~i+M-1 <- M개의 길이 문자열
                #회문 : 앞에서 부터 읽은 문자열 == 뒤에서 부터 읽은 문자열
                cnt = 0
                for j in range(len(temp)):
                    if temp[j] == temp[len(temp) -1 -j]:
                        cnt += 1
                if cnt == len(temp):
                    ans = M
                    flag = 1

    print("#{} {}".format(tc + 1, ans))