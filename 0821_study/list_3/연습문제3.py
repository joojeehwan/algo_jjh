
curR = 0
curC = -1
value = 1 #값이 기록되는,,!


ARR = [[0] * 5 for _ in range(5)]

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]
mode = 0

while value <= 25:

    next_row, next_col = curR + drow[mode], curC + dcol[mode]

    if 0<= next_row < 5 and 0 <= next_col < 5 and ARR[next_row][next_col] == 0:
        ARR[next_row][next_col] = value
        value += 1
        #다음 좌표 이동,,!
        curR, curC = next_row, next_col

    else:
        mode = (mode + 1) % 4

    #1.현재의 좌표에다가 value를 입력한다 => 이거는 시작이 00일떄!
    #2.다음데이터 입력을 좌표를 갱신한다
    #2-1.갱신을 위한 새로운 좌표를 만든다.
    #2-2. 새로운 좌푝 유요한지 확인한다.
    #2-3. 유효하지 않은 경우 mode(방향)을 변경한다.
    #2-4. 좌표를 갱신한다.
    # value를 증가한다

for i in range(5):
    print(ARR[i])