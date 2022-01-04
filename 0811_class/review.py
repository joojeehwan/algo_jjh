


#2차원 배열


#lst = [2,3,4]



# lst = [list(map(int, input().split())) for _ in range(5)]

#얕은 복사 주의!!!



#위에랑 같애!
# lst2 = []
# for _ in range(5):
#     lst2.append(list(map(int, input().split())))
#
# print(lst2)

# 행우선!


# lst = [[2,3,5], [4,5,6], [4,8,9], [1,4,9]]
#
# for i in range(len(lst)):
#     print()
#     for j in range(len(lst[i])):
#         print(lst[i][j], end =" ")
#
# #열우선
#
# for j in range(len(lst[0])):
#     print()
#     for i in range(len(lst)):
#         print(lst[i][j], end = " ")



#지그재그

#홀짝 풀이


#m은 가로 사이즈

#rows = ren(lst)
#cols = len(lst[0])





#연습 문제 3번

curR = 0
curC = -1
value = 1

ARR = [[0] * 5 for _ in range(5)]
#우 하 좌 상
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]
mode = 0

while value <= 25:
    ni, nj = curR + drow[mode], curC + dcol[mode]
    if 0<= ni<5 and 0<= nj <5 and ARR[ni][nj] == 0 :
        ARR[ni][nj] = value
        value += 1
        curR, curC = ni, nj

    else:
        mode = (mode+1) % 4


    #1.현재의 좌표에다가 value를 입력한다 => 이거는 시작이 00일떄!
    #2.다음데이터 입력을 좌표를 갱신한다
    #2-1.갱신을 위한 새로운 좌표를 만든다.
    #2-2. 새로운 좌푝 유요한지 확인한다.
    #2-3. 유효하지 않은 경우 mode(방향)을 변경한다.
    #2-4. 좌표를 갱신한다.
    # value를 증가한다

for i in range(5):
    print(ARR[i])



# 셀렉션 소트와 연관해서??? 25에 딱맞게 하는게 아니라 더 큰 수를 넣으면 셀렉션이 된다!
