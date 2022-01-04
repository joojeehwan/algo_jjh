
import sys


sys.stdin = open("달팽이숫자_input.txt")



T = int(input())



for tc in range(1, T+1):

    N = int(input())

    #일단 큰 틀을 만든다! 값을 하나씩 넣은 이차원 배열을 만든다
    # 근데 주위를 -1를 둘러서! 나중에 맵 범위 벗어나는 것 확인할때 사용!

    MAP = [[-1] *(N+2) for _ in range(N+2)]



    #양 옆의 -1들을 제외하고 안에 사각형에만 값을 넣어야 해서 1 ~ N+1 인것!
    for row in range(1, N+1):
        for col in range(1, N+1):
            MAP[row][col] = 0

    #우 -> 하 -> 좌 -> 상 으로 인덱스가 이동해야 함!
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    #처음 시작좌표! -1이 있는 곳!
    row = 1
    col = 0
    
    #현재 진행 중인 방향
    dir = 0 
    
    #이게 왜 필요하징?! => 기록할 숫자!
    cnt = 1 # 하나씩 적어가면서 남은 숫자를 알아야 하니깐!

    while cnt <= N * N : # N * N인 이유는 가로 세로 곱한 만큼 숫자를 적게 되어서!
        # 딱 그 갯수까지 적여야 하니깐 "="까지 적은 것!

        #다음 좌표 가보자아!
        next_row = row + dr[dir]
        next_col = col + dc[dir]

        #똑같이 가면 안되는 좌표 확인! 범위를 넘어서는 그런 것들!
        if MAP[next_row][next_col] != 0 : # 아 이래서,, 주위를 -1로 둘럿음,,,!
            #벚어나는 것 예외를 쉽게 처리 할려고,,! 0이 아닌 곳, 즉 -1인 곳은 장외니깐!

            #아 그리고 방향 바꾸어야지!
            dir = (dir + 1) % 4 #쭉 증가만 하면 안되니깐,,! % 4한것! [4]번에서 다시 0이 되도록 하기 위함!

        else:
            #이제 한칸 가자!
            row = next_row
            col = next_col
            #가도 괜찮은 좌표면 현재좌표를 그 다음 좌표로 바꾸어준다!
            MAP[row][col] = cnt #번호를 적기!
            cnt += 1 #다음 번호를 준비

    print("#{}".format(tc))
    for row in range(1, N+1):
        for col in range(1, N+1):
            print("{}".format(MAP[row][col]), end = " ")
        print("")





