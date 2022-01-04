


#벽돌 깨기

import copy
from collections import deque




#dfs
#재귀를 이용한 조합의 방법! dfs
def make_path(now = 0, path = []):

    #구슬을 N개 다 쏘았다.
    if now == N:
        path_list.append(path)
        return

    for i in range(W):

        make_path(now + 1, path + [i])


#BFS로 연쇄폭팔을 하기 전에 미리 현재 상태의 게임판을 복사를 해놓아야 하기 때문에!
def copy_map():

    #이중 포문을 해서 MAP을 그대로 복사하기
    temp_MAP = [[0] * W for _ in range(H)]

    for row in range(H):
        for col in range(W):
            temp_MAP[row][col] = MAP[row][col]

    return temp_MAP


#bfs
def bomb_block(temp_map, col):
    # 터질 부분을 터트리기,,
    # temp_map의 col번째 열을 터트린다.
    
    #1. 그래프 구성,, 이미 했음 temp_map

    #2. queue 생성 => [0] : row, [1] : col, [2] : size

    q = deque()
    
    
    #3. 시작점 세팅

    #열을 터뜨려야 하니깐! 열을 고정하고, 행을 위에서 아래로 내려가면서! 시작점 찾기!
    for row in range(H):
        if temp_map[row][col] != 0:
            q.append((row, col, temp_map[row][col]))
            temp_map[row][col] = 0 # 이 블록은 터졌다.
            break
    #q에 값이 있는 동안 반복한다.
    while q:
        
        #4. now 꺼내기

        now = q.popleft()
        now_row = now[0]
        now_col = now[1]
        now_size = now[2]

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        #5. next찾기 => now로 인해 터질 벽돌 찾기

        for i in range(4):
            for pow in range(now_size):
                next_row = now_row + pow * dr[i]
                next_col = now_col + pow * dc[i]

                #범위 밖에 있는 것은 제외
                if next_row < 0 or next_col < 0 or next_row >= N:
                    continue

                if temp_map[next_row][next_col] == 0:
                    continue

                q.append((next_row, next_col, temp_map[next_row]))
                temp_map[next_row][next_col] = 0 #공 터트리기



#이 부분이 im같은 문제
def drop_block(temp_map):
    #temp_map을 확인하면서 벽돌 떨어트리기

    for col in range(W):
        #하나의 컬럼마다!  아래 2개의 for문을 실행 시키는 것! 순서대로!
        cnt = 0 #다른 열로 가면 다시 초기화 해야 하니깐!
        for row in range(H-1, -1, -1):
            if temp_map[row][col] == 0:
                cnt += 1
            else:
                #지금까지 빈칸 개숫를 이용해서 그 만큼 아래칸으로 내려간다
                #swap이 아니다! 그래서 마지막에 cnt만큼 위에서 아래 칸 채워야 한다
                temp_map[row+cnt][col] = temp_map[row][col]
                
        for row in range(cnt):
            temp_map[row][col] = 0
            #빈칸 세팅



def count_block(temp_map): #맵의 벽돌 개수 counting

    cnt = 0
    #이차원 배열에서 하나 빼면 그건 일차원 긴줄 row니깐!
    for rowMAP in temp_map:
        #그 일차원 row에서 하나씩 조회 하면! 블록 하나를 조회하는것!
        for block in rowMAP:
            if block != 0:
                cnt += 1

    return cnt



def pro():
    ans = count_block(MAP) #원래 처음 입력 배열에서 갯수 세기
    
    #순서대로 처리

    make_path()

    for path in path_list:
        #주어진 경우의 수 하나마다 최소값을 구하기 위해서!
        temp_map = copy.deepcopy(MAP)
        for now in path: #패스의 하나의 col 번호
            bomb_block(temp_map, now) #터트림! 
            # 터트려서 빈공간이 생기면 빈 공간만큼 벽돌들이 떨어져야 함
            drop_block(temp_map)
        #내부의 포문을 돌리고(구슬 3번 다쏘고!) 그 다음 경우의 수로 간다!
        #다 쏘고 이제 이전 ans와 비교하면서 남은 벽돌의 갯수가 최소값 갱신
        ans = min(ans, count_block(temp_map))

    return ans
    



T = int(input())

for tc in range(1, T+1):

    N, W, H = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(H)]

    #공을 쏘는 경우의 수를 담을 리스트
    path_list = []

    print(f"#{tc + 1} {pro()}")


#요리사


# 이 문제는 이것만 이해하면 끝나는 것!
def make_path(now = 0, path = []):

    if len(path) == n // 2:
        #set엔 튜플로 해서 넣어야 한다.
        path_set.add(tuple(path))
        return

        if now >= n:
            return

    make_path(now + 1, path +[now]) # A쪽에 포함!
    make_path(now + 1, path)

def calc():
    ret = 2134567890

    #전체 PATH의 수만큼!
    for path in path_set:
        food1 = 0 # A의 맛
        food2 = 0 # B의 맛
        #A에 해당하는 패스만큼,,!
        for i in path:
            for j in path:
                food1 += MAP[i][j]

        #패스에는 A의 식재료만 들어가 있으니!
        #B의 식재료를 만들기 위해서!
        other_path = [] # B 식재료 조합
        for i in range(n): # 모든 식재료 중
            if not i in path: # path에 없으면 => 그건 바로 B의식재료 겟구나!
                other_path.append(i)
        #이중포문으로 구하기!
        for i in other_path:
            for j in other_path:
                food2 += MAP[i][j]
        #패스마다 ret을 값을 갱신!
        ret = min(ret, abs(food1 - food2))
    return ret

def proceed():
    global path_set
    path_set = set()
    make_path()
    return calc()

t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc + 1} {proceed()}")