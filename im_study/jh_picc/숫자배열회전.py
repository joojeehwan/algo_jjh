import sys
sys.stdin = open('숫자 배열 회전_input.txt')

# T = int(input())
#
# for tc in range(1, T + 1):
#
#     N = int(input())
#
#     lst = [input().split() for _ in range(N)]
#
#     res = []
#
#     # print(lst)
#
#     # 90도
#     for j in range(len(lst)):
#         print()
#         for i in range(len(lst) - 1, -1, -1):
#             print(lst[i][j], end="")
#
#     # 180도
#     for i in range(len(lst) - 1, -1, -1):
#         print()
#         for j in range(len(lst) - 1, -1, -1):
#             print(lst[i][j], end="")
#
#     # 270도
#
#     for i in range(len(lst) - 1, -1, -1):
#         print()
#         for j in range(len(lst)):
#             print(lst[j][i], end="")





'''

원래 문제를 빠르게 풀기 위해서는 90도 회전 한것을 가지고 와서
계속 그것을 90도 회전 한다고 생각하고 풀면 쉬워짐! 

'''
T = int(input())

for tc in range(1, T+1):

    N = int(input())

    mat = []

    for _ in range(N): #2차원 행렬 만들기
        mat.append(list(map(int, input().split())))

    # mat = [list(map(int, input().split())) for _ in range(N)]

        
    #90도

    # mat_90 = [[0] * N for _ in range(N)]
    mat_90 = [[0 for _ in range(N)]  for _ in range(N)]

    #이렇게 하는게 수업 스타일! 해보자! => 직접 그려보고 해보면 쉽다!
    for row in range(N):
        for col in range(N):
            mat_90[row][col] = mat[N - 1 - col][row]


    #180도 회전

    mat_180 = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            mat_180[row][col] =mat[N - 1 - row][N -1-col]

    mat_270 = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            mat_270[row][col] = mat[col][N-1-row]

    # 최종 결과 출력 이게 진짜 어려워,,!!!
    # print('#{}'.format(tc))
    # for i in range(N):
    #     result = ''.join(map(str, mat_90[i])) + ' '
    #     result += ''.join(map(str, mat_180[i])) + ' '
    #     result += ''.join(map(str, mat_270[i]))
    #     print(result)
    print('#{}'.format(tc))
    for i in range(N):
        for a in range(N):
            print(mat_90[i][a], end='')
        print(end=' ')
        for b in range(N):
            print(mat_180[i][b], end='')
        print(end=' ')
        for c in range(N):
            print(mat_270[i][c], end='')
        print()