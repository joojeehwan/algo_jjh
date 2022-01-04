#플래튼

'''
카운트배열 만들어 놓고 센다?! 각 값들이 몇 개씩 있는가?!
어차피 숫자는 0-10개자나! 인덱스가 숫자이고 거기에 숫자가 몇개씩 있는지 확인!
-> 데이터를 사전에 처리! 어떻게 좀더 효울적으로,,!

실제 문제로 나왔으면,,, 내 풀이는 시간초과여,,, !


counts 크기를 101개로 만들서 1 ~ 100까지 인덱스를 사용할 수 있게끔! 왜냐면 우린느 1~100을 쓰거든!
0은 사용하지 않거든!

'''



T = 10
for tc in range(T):
    dumps = int(input())
    boxes = list(map(int, input().split()))

    # counts 리스트 만들기
    # 어떤 높이가 몇 개 있는지 세어둔 리스트
    counts = [0] * 101
    # index : 높이, value : 해당 높이가 몇 개 있는가?
    max_height = 0 # 최대 높이
    min_height = 101 # 최소 높이
    for box in boxes:
        counts[box] += 1
        if max_height < box :
            max_height = box
        if min_height > box :
            min_height = box

    for i in range(dumps):
        counts[max_height] -= 1
        counts[max_height - 1] += 1 #아 가장 큰값이 하나 줄어들면서 그 값이 그 다음 큰 값과 같아 져서!
        counts[min_height] -= 1
        counts[min_height + 1] += 1 # 가장 작은 값이 하나 늘어나면서 그 값이 그 다음 작은 값과 같아져서!
        if counts[max_height] == 0:
            max_height -= 1
        if counts[min_height] == 0:
            min_height += 1

    ans = max_height - min_height





#sum


'''

가로 , 세로 같이 할 수 있음1 

이차원배열 => 대각선의 위치 정보로 이 대각선이 어디에 있는 대각선인지 알 수 있다! 

k = row - col (좌상 우하)

k = row + col (좌하 우상)


ex)체스판 퀸 두기! ... 기록을 보고 판단이 간으해져! 

=> 아하! 가로 세로 대각선에 이미 존재 하고 있음을! 미리 저장판에 저장해두고!
있는지 없는지만 판단! 그때 대각선을 확인할때 위와 같은 것을 활용! 

입력의 size를 줄여서 좀더 쉽게 생각! =>size라는 변수 사용!  

'''

T = 10
for tc in range(T):
    size = 100
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(size)]

    ans = -1
    sum_lu_rd = 0
    sum_ru_ld = 0
    for row in range(size):
        sum_row = 0
        sum_col = 0
        for col in range(size):
            sum_row += MAP[row][col]  # 줄 단위로 계산(가로방향)
            sum_col += MAP[col][row]  # 칸 단위로 계산(세로방향)
        if ans < sum_row:
            ans = sum_row
        if ans < sum_col:
            ans = sum_col
        sum_lu_rd += MAP[row][row]
        sum_ru_ld += MAP[row][(size - 1) - row]
    if ans < sum_lu_rd:
        ans = sum_lu_rd
    if ans < sum_ru_ld:
        ans = sum_ru_ld
    print("#{} {}".format(tc + 1, ans))


