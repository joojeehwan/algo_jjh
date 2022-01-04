# import sys
# sys.stdin = open("Ladder2_input.txt")



'''

ladder1이랑 기본 구조는 같으니! 답 보지 말고 내 손으로 해보자! 


모든 출발점을 검사하여 바닥까지 가장 짧은 이동 거리를 갖는 시작점 x를 반환하는,,! 
(복수개의 경우 가장 큰 x좌표)

x처음 부터 끝까지 검색하면서!  한칸 이동 하는 것을 cnt로 개수를 센다!

그중에 가장 짧은 것을 사용 !

'''

''''
1 0 0 0 1
1 1 0 0 1
0 1 0 0 1
0 1 1 0 1
0 0 1 0 1

'''



T = 1

for _ in range(1, T+1):


    tc = int(input())
    size = 5

    MAP = [list(map(int, input().split())) for _ in range(size)]

    for start in range(size): # 모든 출발점을 검사하기 위해서!

        visited = [[0] * size for _ in range(size)]
        # 한번 간곳은 저장하기 위한 "기억 배열 만들기"
        min_cnt = 100 * 100
        row = 0
        col = 0
        cnt = 0
        de = 1
        # 맨위에서 부터 시작 좌표 찾기! 숫자가 1인 곳!
        if MAP[row][col + start] == 1:
            col = col + start

        else:
            continue

        de = 1

        #좌 우 하
        dr = [0, 0, 1]
        dc = [-1, 1, 0]

        while  row <= size-1 :

            for i in range(3): #방향 정해서 한칸 내려가고!
                next_row = row + dr[i]
                next_col = col + dc[i]
                #next_row랑 next_col을 정했으면? 이제 안되는 조건들을 continue로 배제

                if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                    continue #맵을 벗어나는 좌표! size에 = 가 붙는 이유는 100칸이라서 0 ~ 99까지 있는데!
                            # size는 100이니깐! 100만 되어도 범위 초과니깐!


                if visited[next_row][next_col] == 1:
                    continue

                if MAP[next_row][next_col] == 1:
                    row = next_row #이제 가라!!!
                    col = next_col
                    visited[row][col] = 1 #아 이제 next_가 현재가 되었으니!
                    cnt += 1
                    break # 그 방향이 조건에 맞았으면 굳이 다른 방향을 볼 필요가 없어서!

        if min_cnt > cnt :
            min_cnt = cnt

    print("#{} {}".format(tc, min_cnt))







