'''


색종이

덧칠 한다는 개념으로 가자!

'''



N = int(input())


MAP = [[0] * 100 for _ in range(100)]


for i in range(N):

    row_ld ,col_ld, width, height = map(int, input().split())
    cnt = 0
    for row in range(row_ld, row_ld + width):
        for col in range(col_ld, col_ld + height):
            MAP[row][col] = i + 1

    de = 1
    #이중 포문 돌리지말자! 일중 포문으로 끝낼 수 있다,, for - count 함수를 사용해서!
    #row 하나씩 뽑아서 count로 갯수 구하기!
for i in range(N):
    cnt = 0
    for row in MAP:
        cnt += row.count(i+1)
    # for row in range(row_ld, row_ld + height):
    #     for col in range(col_ld, col_ld + width):
    #         if MAP[row][col] == i + 1:
    #             cnt += 1

    print(cnt)





