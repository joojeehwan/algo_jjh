


T = int(input())


for tc in range(1, T+1):


    N = int(input())

    MAP = [list(input().rstrip()) for _ in range(N)] # 리스트를 사용해서 해당 값을 변경 할 수 있게!


    # 찾아서 지운다! 기지국 주위의 집들을 찾아서 지우러간다! 범위 조심!

    for row in range(N):
        for col in range(N): #지우러 출발해보자아아아!!

    #기지국이 아니라면! 무시
            if MAP[row][col] == 'H' or MAP[row][col] == 'X':
                continue

        #기지국 별로 거리가 다르기 때문에,,,! 일종의 "표시"를 준다!
        # 기지국 마다 다른 거리를 주기 위해서!

            if MAP[row][col] == 'A':
                flag = 1

            elif MAP[row][col] == "B":
                flag = 2

            elif MAP[row][col] == "C":
                flag = 3

            #이제 여기서부터 다른 기지국 마다 표시를 할 수 있게 됨!
            for dir in range(1, flag+1): #실제로 1부터 이동을 하니깐! flag 레이지의 범위만큼 반복하니깐! => 거리 설정!
                if 0 <= row - dir: MAP[row-dir][col] = "X"
                if row + dir < N: MAP[row + dir][col] = "X" #인덱스로 하면 N이니깐 이렇게 하는 것!
                if 0 <= col - dir: MAP[row][col-dir] = "X"
                if col + dir < N : MAP[row][col + dir] = "X"


    cnt = 0

    for row in range(N):
        for col in range(N):
            if MAP[row][col] == "H":
                cnt += 1

    print("#{} {}".format(tc, cnt))
