


#ladder1풀이



'''


도착지에서 거꾸로 올라가는 방향으로,,!

while을 쓰기 좋은 경우! 도착지가 정해지고 거기까지 가는 ,,,! for보다는 while!

조건을 만족하면서 목표까지는 가는 것!
'''

import sys


sys.stdin = open("ladder1_input.txt")

def search(start): #도착지에서 위로 올라가는 함수
    i = 99 #행
    j = start #열
    while i>0: #맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1 #위로 한 칸 이동
        if j > 0 and ladder[i][j-1] == 1:#왼쪽 칸이 1이면
            while j > 0 and ladder[i][j-1] == 1: #왼쪽칸이 있고 1이면 ..! 0을 만날 때까지 이동
                j -= 1
        #오른쪽 같이 1이면
        elif j < 99 and ladder[i][j+1] == 1:  #오른쪽 칸이 있고 1이면!
            while j < 99 and ladder[i][j+1] == 1:
                j += 1
        #좌우가 0이면 위로... 이건 while문 바로 아래서 하는구나!! 굳이 else가 필요치 않아!
    return j #0번 행에 도착했을 때의 열(출발지) 리턴


T = 10
for tc in range(1, T+1):
    n = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착지 검색

    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print(f"#{tc} {ans}")



#0817
'''

테스트 케이스가 너무 크다!
size 관련된 것들을 다 변수로 바군다! 맵 크기와 관련된 것으로! 

그리고 디버깅하기! 
'''

T = 10
for tc in range(T):
    N = int(input())
    size = 100
    MAP = [list(map(int, input().split())) for _ in range(size)]
    visited = [[0] * size for _ in range(size)] # 들렸던 점인지 기록
    # 0 ~ 99

    row = size - 1
    col = 0
    for i in range(size):
        if MAP[row][i] == 2:
            col = i
    # 시작점 찾기

    # 사다리 타고 올라가기
    # 우선순위 : '기본 : 위' 왼쪽 or 오른쪽 <- 우선
    dr = [ 0, 0,-1]
    dc = [-1, 1, 0]
    while row > 0:
        de = 1
        for i in range(3):
            next_row = row + dr[i]
            next_col = col + dc[i]
            if next_row < 0 or next_col < 0 or \
                next_row >= size or next_col >= size:
                continue # 맵을 벗어나는 좌표면 무시
            if visited[next_row][next_col] == 1:
                continue
            if MAP[next_row][next_col] == 1:
                row = next_row
                col = next_col
                visited[row][col] = 1 # row, col을 들려봤다.
                break
    # 2차원 맵, 델타 배열로 다음 좌표를 계산해서 움직이는 경우
    # 좌표 계산시 맵을 벗어나는 좌표가 찾아지는 경우

    # 갔던 곳을 다시 가는 경우

    print("#{} {}".format(tc + 1, col))



#파리퇴치




