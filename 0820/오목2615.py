


'''

검은바둑알 1
흰색 바둑알 2
아직 놓이지 않음 0

숫자

연속으로 놓일 수 있음을 어떻게 표현하지..?연속으로
=> 회문 공부하면서 했었다! 그걸 적용해보자!

=> 델타 배열을 사용해버리네,, 대단하구만,,, 오른쪽 , 아래 , 우하향, 좌하향을,,!

 o(기준 * -1)o(기즌) o o o o o(기준 * 5) (양 쪽 끝이 달라야지 6개가 안된다! )

map을 벗어나는 좌표는 항상 조심하자! 알았지?! 이런식의 좌표문제는,,! 이 자슥아!




디테일하게 과정을 적으면서 코드의 방향성을 적자!

델타가 생각이 안난거는 내가 skil을 정리 안해서야,,!

상황을 그려보면서 생각해보아라,,! 

디버깅의 문제라면! 아주 안될듯한 예외 케이스를 넣어보자,,! + 디버깅 모드 하는 연습



'''


MAP = [list(map(int, input().split())) for _ in range(3)]

count = 0

M = 2

for row in range(len(MAP)):

    for col in range(3 - M + 1):
        temp = MAP[row][col:col+M]
        sum = 0
        for i in temp:
            sum += i
        if sum == 5:
            print(1)
            break

print(MAP)




######################################


#for문 사용 구현
MAP = [ list(map(int, input().split())) for _ in range(19)]

who = 0

for row in range(19):
    # row : 기준점의 줄 번호
    for col in range(19):
        # col : 기준점의 칸 번호
        dr = [0, 1, 1, -1]
        dc = [1, 0, 1, 1]
        # row,col기준에서 나아갈 방향 4가지 선정(오른쪽, 아래, 우하향, 우상향)
        if MAP[row][col] == 0:
            continue # 말이 없으면 무시
        for dir in range(4):
            #dir : 방향 번호
            cnt = 0 # 연속한 말이 몇개 있는가?
            for i in range(5):
                # i : dir방향대로 얼마나 갈 것인가?
                next_row = row + dr[dir] * i
                next_col = col + dc[dir] * i
                if next_row < 0 or next_col < 0 or next_row >= 19 or next_col >= 19:
                    continue
                if MAP[next_row][next_col] == MAP[row][col]:
                    cnt += 1
             #위에까지 5개를 확인하는 코드


            #그 반댓방향으로 같은 돌이 1개라도 있으면 6개 이상이 되어 버리니,
            #항상 넥스트 들 다음에는 범위 조심,,!!
            next_row = row - dr[dir]
            next_col = col - dc[dir]
            if next_row >= 0 and next_col >= 0 and \
                    next_row < 19 and next_col < 19 and \
                    MAP[next_row][next_col] == MAP[row][col] :   #6목을 찾는 거니깐! 당연히 범위안에 있으야 하고!, 첫번쨰 기준 6개 되는 하나가 나랑 같아야 해!
                continue

            #그 이후 방향으로 하나라도 더 있으면 안되니깐!

            next_row = row + dr[dir] * 5
            next_col = col + dc[dir] * 5
            if next_row >= 0 and next_col >= 0 and \
                    next_row < 19 and next_col < 19 and \
                    MAP[next_row][next_col] == MAP[row][col]:
                continue
            if cnt == 5:
                # 정답을 찾았다.
                y = row
                x = col
                who = MAP[row][col]
print(who)
if who != 0:
    print(y + 1, x + 1)


#함수 사용구현


def check(row, col, dy, dx):
    if MAP[row][col] == MAP[row + 5 * dy][col + 5 * dx]:
        return # 5칸 앞에 같은 말이 있는지 보고 무시
    if MAP[row][col] == MAP[row - dy][col - dx]:
        return # 바로 뒷칸에 같은 말이 있는지 보고 무시
    for i in range(5):
        if MAP[row][col] != MAP[row + i * dy][col + i * dx] :
            return # 5개의 말 중에서 하나라도 다른게 있으면 무시
    # 앞의 for문을 통과하면 승자를 찾은 것이므로 기록
    global ans
    ans[0] = MAP[row][col]
    ans += [row, col]

M = [ list(map(int, input().split())) for _ in range(19)]
MAP = [[0] * 30 for _ in range(30)] # 30 x 30크기 맵
for i in range(6,25):
    for j in range(6, 25):
        MAP[i][j] = M[i - 6][j - 6] # (6,6)~(24,24)위치에 입력값 복사

ans = [0] # ans : 답, 0번 : who, 1번 : y, 2번 : x

for row in range(6,25):
    # row : 기준점의 줄 번호
    for col in range(6,25):
        # col : 기준점의 칸 번호
        if MAP[row][col] == 0:
            continue # 돌이 없으면 무시
        dr = [0, 1, 1, -1]
        dc = [1, 0, 1, 1]
        for dir in range(4):
            check(row, col, dr[dir], dc[dir])

print(ans[0])
if ans[0] != 0:
    print(ans[1]-5, ans[2]-5)