#오목 함수를 사용하여 구현!


MAP = [list(map(int,input().split())) for _ in range(19)]


who = 0 #누가 이겼는지,,!?


for row in range(19):
    
    #row : 기준점의 줄 번호

    for col in range(19):
    # col : 기준점의 칸 번호

    #오른족, 아래, 우하향, 우상향
    dr = [0, 1, 1,-1]
    dc = [1, 0, 1, 1]

    #안되는 조건들 나열! 후 continue처리!
    if MAP[row][col] == 0 :
        continue
        
    for dir in range(4):
        #dir : 방향 번호
        cnt = 0 # 연속한 말이 몇개 있는가?
        for i in range(5):
            # i : dir 방향대로 얼마나 갈 것인가?
            next_row = row + dr[dir] * i
            next_col = col + dc[dir] * i
            if next_row < 0 or next_col < 0 or next_row >= 19 or next_col >= 19:
                continue
            if MAP[next_row][next_col] == MAP[row][col]: #처음 시작값과 비교!
                cnt += 1





