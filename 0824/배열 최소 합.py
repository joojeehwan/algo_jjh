

import sys

sys.stdin = open("배열 최소 합_input.txt")


# #단 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다,,!
#
# #N캐슬에서 모티브를 얻어라,,!
#
#
# T = int(input())
#
#
#
#
# #완전 틀리게 했구마잉,,!!!
# for tc in range(1, T + 1):
#
#     N = int(input())
#     col_check = [0] * N
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     total = 0
#     for row in range(len(lst)):
#         min_value = 11
#         min_idx = 0
#         for col in range(len(lst[row])):
#             if min_value > lst[row][col] and col_check[col] == 0:
#                 min_value = lst[row][col]
#                 min_idx = col
#
#         col_check[min_idx] = 1
#
#         total += min_value
#
#     print("#{} {}".format(tc, total))
#
#

'''

앤캐슬 하는 방법,,,!!

check를 복구해야! 다른 방법을 찾아볼 수 있어,,,! 다른 방법으로도 찾아 보게 해야지! 




1. 전역변수 방법

1) 하나씩 골라서 맨 밑의 값까지 고르기
2) 1)을 다양한 방식으로 가볼 수 있게 만들기,,! (check한거 없애기)
3) 값을 계산하는 구조로 만들기! (ex) sum + data[row][i])

그 방법들 중에서도 최소가 되는 것을 원해! 





'''

#최교수님 풀이


def dfs(row, sum):
    # row번째까지 고른 수들의 합 : sum
    global ans
    if row == n:
        # 둘 수 없는 경우는 가지치기를 했으니 여기까지 오면 가능한 방법이다!

        #만약에 카운트 세는거였으면 여기다가 cnt조건을 주었을 것!
        ans = min(ans, sum) #보통 기저 조건에 문제와 직접적인 연결고리가 있는 것을,,!
        return
    for i in range(n):
        # i 0~n-1(칸 번호)
        if col[i] == 1:
            continue  # 기록하기도 전에 이미 기록이 있다!
            # 앞에서 둔적이 있다! 그러면 무시(가지치기)
        col[i] = 1

        dfs(row + 1, sum + data[row][i])
        # 이번에 i번 위치에다가 말을 두는 방법으로 다 해보기
        # 이번에 row번째 줄 i번째 칸의 값을 고른 것이므로 해당 값만큼 sum에 누적

        col[i] = 0  # i번에 대해선 끝났으니 기록을 삭제


T = int(input())
for tc in range(T):
    n = int(input())

    # 그래서 어디뒀는데!!!!!
    col = [0] * n  # col[index] -> index: 칸 번호, value : 해당 칸을 사용하고 있는가?
    ans = 2134567890

    data = [list(map(int, input().split())) for _ in range(n)]
    dfs(0, 0)
    print("#{} {}".format(tc + 1, ans))

    # 1. 하나씩 골라서 맨 밑의 값까지 고르기
    # 2. 1.을 다양한 방식으로 가볼 수 있게 만들기
    # 3. 값을 계산하는 구조 <- 합, 경우의 수 : 그냥 앤캐슬이랑 이거 같은 구조 외우자!


