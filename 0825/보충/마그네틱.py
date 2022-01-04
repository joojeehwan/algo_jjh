import sys
sys.stdin = open("마그네틱_input.txt")


T = 10

for tc in range(1, T+1):

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
        for col in range(100):  #한 행씩 보는거임
            #N극에서 시작할 때 (위)
            if arr[row][col] == 1:
                # 한 칸씩 내려
                if arr[row+1][col] == 2:  #2가 나오면 cnt
                    cnt += 1
                elif arr[row+1][col] == 0:  #0이면 이동
                    arr[row+1][col] = arr[row][col]


    
    print('#{} {}'.format(tc, cnt))



    #
    # ans = 0
    # #열우선 순회
    # for col in range(100):
    #     # 상태, 값, 0 = 1을 만나기전 상태, 1 = 1을 만난 상태
    #     state = 0
    #     for row in range(100):
    #         if state == 0 and arr[row][col] == 1:
    #             state = 1
    #
    #         elif state == 1 and arr[row][col] == 2:
    #             ans +=1
    #             state = 0
    #
    # print(ans)
    #




# arr = [[1,2,3], [1,2,3]]
#
# arr.extend([[1,2,3]])
#
# print(arr)

