

import sys

sys.stdin = open("농작물 수확_input.txt")
'''

 N = 7 // 2 ?

행 별로

시작과 끝의 인덱스를 보자!


쓰면서 패턴을 본다,,!


0 - (3,3)

1- (2,4)

2 - (1,5)

3 - (0, 6)

4  - (1, 5)

5 - (2, 4)

6 - (3,3)


이걸 깊이로 한다고 넓이로,,> 아까 도 비슷한거 본거 같은디,,!


'''









# for tc in range(1, T+1):
#
#     N = int(input())
#
#     lst = [list(map(int, input())) for _ in range(N)]
#
#     N // 2
#
#     sum = 0
#     for row in range(N // 2 + 1):
#         for col in range(N // 2 - row,  N // 2 + row + 1):
#                 sum += lst[row][col]
#
#     for row in range(N // 2 + 1, N + 1):
#         for col in range(N // 2 - row + 2, N // 2 + row -2):
#                 sum += lst[]
#


T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    t_N = N//2
    change = -1 #이게 신의 한수,,, 
    answer = 0
    for i in range(N):
        if i >= N//2:
            change = 1 #체인지 변수를 사용해서,,! 기점 기준으로 더 할 수 있게,,!
        for j in range(abs(i-N//2), abs(N-t_N)):
            answer += map_list[i][j]
        t_N += change
    print('#{} {}'.format(t, answer))




