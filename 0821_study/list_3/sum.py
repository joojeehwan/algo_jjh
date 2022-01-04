


T = 10



for tc in range(T):
    size = 100
    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(size)]


    abs = -1
    sum_lu_rd = 0
    sum_ru_ld = 0

    for row in range(size):
        sum_row = 0
        sum_col = 0

        for col in range(size):
            sum_row += MAP[row][col]
            sum_col += MAP[col][row]

        #한 개의 반복문 안에서 가로, 세로의 합중에 최대값을 구한다.
        if ans < sum_row:
            ans = sum_row
        if ans < sum_col:
            ans = sum_col

        sum_lu_rd += MAP[row][row]
        sum_ru_ld += MAP[row][(size-1) - row] #인덱스라서 size-1이 들어감!

    if ans < sum_ru_ld:
        ans = sum_ru_ld
    if ans < sum_lu_rd:
        ans = sum_lu_rd

    print("#{} {}".format(tc, ans))


#원래 내 풀이보다 훨씬 효율적인듯,,!

'''
T = 10

for tc in range(1, T+1):

    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]

    res = []

    #행 합
    for i in range(len(lst)):
        sum_row = 0
        for j in range(len(lst[i])):
            sum_row += lst[i][j]
        res.append(sum_row)

    # 열 합
    for j in range(len(lst[0])):
        sum_col = 0
        for i in range(len(lst)):
            sum_col += lst[i][j]
        res.append(sum_col)
    # 대각선 합
    sum_dia = 0
    for i in range(len(lst)):
        sum_dia += lst[i][i]
    res.append(sum_dia)
    # 역 대각선 합

    sum_revesr_dia = 0

    for i in range(len(lst)):
        sum_revesr_dia += lst[i][99-i]

    res.append(sum_revesr_dia)

    max_val = 0
    for i in range(len(res)):
        if max_val < res[i]:
            max_val = res[i]

    print(f"{tc} {max_val}")


'''