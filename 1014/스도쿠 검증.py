

'''
# 파리 퇴치!

# 스도쿠 검증! 은 im 필수 문제!


#im에서 중요하게 생각해야 할 것! 배열 완전 탐색!


#범위에 변수가 들어가는 것을 잘해야 한다!



'''



'''


counts 배열을 만들어야 한다! index가 숫자고, value가 사용횟수! 

한번씩 다 사용될려면 1 ~ 9까지 1을 사용했어야 해! 


이번엔 함수로 만들어보자! flag 대신 함수를 사용하면 return으로 끝낼 수 있으니깐! 


중복을 다루는 방법 => set(), counts 배열




'''



def check(arr_2nd):

    for row in range(len(arr_2nd)):
        counts_ver = [0] * 10
        for col in range(len(arr_2nd[row])):
            counts_ver[arr_2nd[row][col]] += 1
            if counts_ver[arr_2nd[row][col]] > 1: #값이 중복인지 확인
                return 0

    for row in range(len(arr_2nd)):
        counts_hor = [0] * 10
        for col in range(len(arr_2nd[row])):
            counts_hor[arr_2nd[col][row]] += 1
            if counts_hor[arr_2nd[col][row]] > 1: #값이 중복인지 확인
                return 0

    for row in range(9):
        for col in range(9):
            count_squ = [0] * 10
            if row % 3 == 0 and col % 3 == 0:
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        count_squ[arr_2nd[i][j]] += 1

                        if count_squ[arr_2nd[i][j]] > 1:
                             return 0

    return 1



T = int(input())


for tc in range(1, T+1):

    MAP = [list(map(int, input().split())) for _ in range(9)]

    if check(MAP) == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")



'''

교수님 추가 문제 어떻게 구할까?!

제일 넓은 가로, 제일 넓은 세로 구하기! 


1차원 배열 2개를 만들어서! 0으로된, 열 , 행 배열  2개 만들고


정렬 쓰면 다 된것! 

카운츠 배열
입력으로 들어오는 값이 있으면 1 로 표시 하고!  
연속 된 0의 갯수 중에 가장 긴 길이를 구해서! 


'''




# import sys
# sys.stdin = open('input.txt')

#스도쿠 검증하기 함수
# 파라미터? 매개변수의 역할?? : 함수를 실행하는데 필요한 데이터
def solve(arr):
    # 스도쿠 검증
    # 모든행마다 각각 1부터 9까지 숫자가 한 번씩만 들어야함
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            if check[arr[i][j]]:    #중복이 발생
                return 0
            else:
                check[arr[i][j]] = 1
    # 모든 열마다 각각 1부터 9까지 숫자가 한 번씩만 들어가야 한다.
    for j in range(9):
        check = [0] * 10
        for i in range(9):
            if check[arr[i][j]]:    #중복이 발생
                return 0
            else:
                check[arr[i][j]] = 1
    # 3*3으로 표현되는 부분행렬에 1부터 9까지 숫자가 한번씩만 들어가야 한다.
    #크게 3*3
    # for i in range(3):
    #     for j in range(3):
    #         check = [0] * 10    #작은 3*3 행렬에서 1~9까지가 한 번씩 나오는지 검사
    #         for a in range(i*3,i*3+3):
    #             for b in range(j*3,j*3+3):
    #                 if check[arr[a][b]]:  # 중복이 발생
    #                     return 0
    #                 else:
    #                     check[arr[a][b]] = 1
    #
    for i in range(0,9,3):
        for j in range(0,9,3):
            check = [0] * 10
            for a in range(i,i+3):
                for b in range(j,j+3):
                    if check[arr[a][b]]:  # 중복이 발생
                        return 0
                    else:
                        check[arr[a][b]] = 1

    return 1    #조건 세 개를 모두 통과 했으니 스도쿠 이다.


T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = solve(arr)
    print('#{} {}'.format(tc, result))







