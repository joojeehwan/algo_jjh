#정사각형 방




# def dfs(row, col):
#
#     if dp[row][col] != -1:
#         return dp[row][col]
# 
#
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#
#     ret = 1
#     for i in range(4):
#
#         next_row = row + dr[i]
#         next_col = col + dc[i]
#
#         if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
#             continue
#
#         if MAP[next_row][next_col]  != MAP[row][col] + 1 :
#             continue
#
#         ret = max(ret, dfs(next_row, next_col) + 1)
#
#     dp[row][col] = ret
#
#     return ret
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#
#     N = int(input())
#
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#
#     dp = [[-1] * N for _ in range(N)]
#
#     ans_cnt = 0
#     ans_num = -1
#
#
#     for i in range(N):
#         for j in range(N):
#
#             cnt = dfs(i, j)
#             if ans_cnt < cnt:
#                 ans_cnt = cnt
#                 ans_num = MAP[i][j] #네모안의 값을 만들어 줌으로써 비교를 가능케 할려고!
#
#             elif ans_cnt == cnt and ans_num > MAP[i][j]: #같으면! 네모안의 값이 작은 것을!
#                 ans_num = MAP[i][j]
#
#     print(f"#{tc} {ans_num} {ans_cnt}")
#
#
#



#장훈이의 높은 선반

#점원을 뽑고 안뽑고의 dfs방식,,!



#now는 사람의 인덱스
#sum은 뽑힌 사람의 몸무게의 합
# def dfs(now, sum):
#
#     global ans
#
#     if B <= sum:
#         ans = min(ans, sum) #최솟값 기록
#         return
#
#     if now >= N:
#         #모든 사람에 대해서 확인이 끝,,!
#         return
#
#     #1. 뽑는다.
#     dfs(now + 1, sum + height[now])
#
#     #2. 뽑지 않는다.
#     dfs(now + 1, sum)
#
#
# T = int(input())
#
#
# for tc in range(1, T+1):
#
#     N, B = map(int, input().split())
#
#     height = list(map(int, input().split()))
#
#     ans = 987654321
#
#     dfs(0, 0)
#
#
#     #만들 수 있는 높이 가 B이상인 탑 중에서,,!
#     print(f"#{tc} {ans - B}")

#격자판의 숫자 이어 붙이기




def dfs(row, col, line):


    if len(line) == 7:

        ans.add(line)
        return

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):

        next_row = row + dr[i]
        next_col = col + dc[i]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N :
            continue

        dfs(next_row, next_col, line + MAP[next_row][next_col])



T = int(input())


for tc in range(1,T+1):

    N = 4

    #문자열로 입력받는다
    MAP = [input().split() for _ in range(N)]

    ans = set()


    for i in range(N):
        for j in range(N):
            dfs(i, j, MAP[i][j])


    print("#{} {}".format(tc, len(ans)))



























