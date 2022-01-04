'''


상어초등학교

딕셔너리로 받으면 좋을거 같긴하네,,,! 학생번호 : 선호하는 학생들


1. 인접한 곳에 학생을 배치해야함.(상하좌우, 대각선은 있을 수 없음)

2. 대전제 좋아하는 학생에게 인접하도록 배치

    2-1) 배치를 할때 그 배치하는 곳 주위에 비어있는 칸이 많은 곳으로 (다음번 을 대비)

    2-2) 행의 번호가 작은 순으로, 열의 번호가 작은 순으로
'''

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def seat_1(k, val, MAP):

    seat = dict()
    max_num = 0

    for row in range(N):
        for col in range(N):
            #빈자리에 앉을 수 있는 자리
            if class_MAP[row][col] == 0:
                count = 0

                for k in range(4):
                    next_row = row + dr[k]

                    next_col = col + dc[k]

                    if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                        continue

                    if MAP[next_row][next_col] in val:
                        count += 1

                seat[count] = seat.setdefault(count, []) + [[row, col]]


                if max_num<count:
                    max_num = count

    return seat[max_num]


def seat_2(k, seat, MAP):

    new_seat = dict()
    max_num = 0

    for row, col in seat:
        count = 0
        for k in range(4):
            next_row = row + dr[k]
            next_col = col + dc[k]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue

            if MAP[next_row][next_col] == 0:
                count += 1

        #민우님 함수  그find_seat? 부분을 setdeafult 함수로 구현
        new_seat[count] = new_seat.setdefault(count, []) + [[row, col]]

        if max_num<count:
            max_num = count

    return new_seat[max_num]
N = int(input())


student_info = {}

for i in range(N * N):
    info = list(map(int, input().split()))
    student_info[info[0]] = set(info[1:])

class_MAP = [[0] * N for _ in range(N)]


for idx, val in student_info.items():

    seat = seat_1(idx, val, class_MAP)
    seat = seat_2(idx, seat, class_MAP)
    seat = sorted(seat)

    class_MAP[seat[0][0]][seat[0][1]] = idx



result = 0

satisfafcion = [0,1,10,100,1000]

for row in range(N):

    for col in range(N):

        s = class_MAP[row][col]

        count = 0
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if 0<= next_row < N and 0 <= next_col < N:
                if class_MAP[next_row][next_col] in student_info[s]:
                    count += 1


        result += satisfafcion[count]



print(result)







