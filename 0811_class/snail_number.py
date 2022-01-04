





T = int(input())
for tc in range(T):
    N = int(input())
    MAP = [[-1] * (N + 2) for _ in range(N + 2)]
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            MAP[row][col] = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    # 방향 순서 : 우 하 좌 상

    row = 1
    col = 0
    # 현재 좌표
    dir = 0 # 현재 진행중인 방향

    cnt = 1 # 기록할 숫자
    while cnt <= N*N :
        next_row = row + dr[dir]
        next_col = col + dc[dir]
        #   다음 좌표
        if MAP[next_row][next_col] != 0:
            #가면 안되는 곳인지?
            dir = (dir + 1) % 4 # 4가되면 0으로 돌아가게
        else:
            row = next_row
            col = next_col # 가도 괜찮은 좌표면 직접 가도록 만들어 준다.
            MAP[row][col] = cnt # 가서 cnt로 기록
            cnt += 1 # 다음 번호를 준비
    print("#{}".format(tc + 1))
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            print("{} ".format(MAP[row][col]), end = "")
        print("")
