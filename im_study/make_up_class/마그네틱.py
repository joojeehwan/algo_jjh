

#좋은 문제,,! 문제를 잘 정독하면 답이 보인다!

#코드가 그렇게 어렵지는 않아,,,! 문제를 푸는 요령이 있음! 빨간색들이 떨어지는 s극을 만들기!

#교수님 코드도 복붙해서 다시 보기!




import sys
sys.stdin = open("input (40).txt")

# T = 10
#
#
# for tc in range(1, T+1):
#
#     N = int(input())
#
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     arr.extend([[0] * 100]) # S극 만들기
#
#     cnt = 0
#     for row in range(100):
#         for col in range(100):
#             if arr[row][col] == 1:
#                 if arr[row+1][col] == 2:
#                     cnt += 1
#                 elif arr[row+1][col] == 0:
#                     arr[row+1][col] == arr[row][col]
#
#     print("#{} {}".format(tc, cnt))

T = 10

for tc in range(1, T + 1):

    N = int(input())

    # arr = [[0] * 101 for _ in range(101)]
    #
    # for i in range(100):
    #     arr[i] = (list(map(int, input().split())))

    arr = [list(map(int, input().split())) for _ in range(100)]
    arr.extend([[0] * 100])
    # print(arr)
    cnt = 0
    for row in range(100):
        for col in range(100):  # 한 행씩 보는거임
            # N극에서 시작할 때 (위)
            if arr[row][col] == 1:
                # 한 칸씩 내려 그래서 row +1 을 한것 
                if arr[row + 1][col] == 2:  # 2가 나오면 cnt
                    cnt += 1
                elif arr[row + 1][col] == 0:  # 0이면 이동
                    arr[row + 1][col] = arr[row][col]

    print('#{} {}'.format(tc, cnt))

