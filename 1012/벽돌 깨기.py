'''

SWEA 벽돌 깨기



1) 구슬은 좌우로만 움직일 수 있어서 항상 맨위에 있는 벽돌만 깨뜨릴 수 있다.

2) 벽돌을 숫자 1 ~ 9로 표현되며, 구술이 명중한 벽돌은 상하좌우로
(벽돌에 적힌 숫자 -1 )칸 만큼 같이 제거 된다.

    EX)
    벽돌에 1이 적혀 있으면 자기 자신만 제거

    만약에 3이 적혀 있으면 자기자신 포함해서 상하좌우 2칸 씩 이동(5X5 짜리 십자가)


3) 제거되는 범위 내에 있는 벽돌은 동시에 제거 된다. 


4) 빈공간이 있을 경우 벽돌을 밑으로 떨어짐


"N개의 벽돌을 떨어뜨려서 최대한 많은 벽돌을 제거"


구슬을 쏘는 횟수 : N
가로 길이 : W
세로 길이 :H




가장 먼저 해야 하는 작업


1. 벽돌 고르기 <= 재귀(dfs)

path
순열 사용

'''


#구슬을 쏘는 위치를 탐색 -> DFS

#구슬을 쏘는 위치(행, 열)을 구하게 되면 그 자리에서부터 연쇄 폭팔을 하게 되는 부분을 BFS를 활용

#유의 할점 DFS후 다시 백트래킹을 할 때, 이미 게임판은 연쇄폭팔로 부쉬진 상태이기 때문에,

# 폭발이 일어나기 전의 게임판으로 복구를 해줘야 함.

# 그러므로 BFS로 연쇄폭팔을 하기 전에 미리 현재 상태의 게임판을 복사를 해놓고 백트래킹 후에 그 복사된

# 게임판으로 복구를 하면 된다.



dr = [-1,1,0,0]
dc = [0,0,-1,1]



#이차원 리스트 복사
def deepcopy(lst):

    new_lst = []
    #행 별로 새로운 리스트에 삽입
    for row in range(len(lst)):
        temp = [] #임시 저장되는 배열을 만듬.
        for col in range(len(lst[row])):
            temp.append(lst[row][col])

        new_lst.append(temp)

    return new_lst


def bomb(row, col, now_bricks):

    q = [(row, col, now_bricks[row][col])]
    now_bricks[row][col] = 0

    
    #터져나가는 형태 => bfs로 구현
    earsed_bricks = 1
    while q:
        now_row, now_col, now_power = q.pop(0)

        for pow in range(1, now_power):
            for dis in range(4):
                next_row = now_row + pow * dr[dis]
                next_col = now_col + pow * dc[dis]

                if next_row < 0  or next_col < 0 or next_row >= N or next_col >= N:
                    continue

                if now_bricks[next_row][next_col] == 0:
                    continue

                if now_bricks[next_row][next_col] != 1:
                    q.append((next_row, next_col, now_bricks[next_row][next_col]))
                earsed_bricks += 1
                now_bricks[next_row][next_col] = 0




                    
                

'''

구슬을 쏘는 횟수 : N
가로 길이 : W (넓이) col
세로 길이 :H (높이) row



사이사이 빈칸을 모어서 위에 채워 넣는다. 

'''



def dfs(result, k, bricks):
    global max_result

    #구슬을 주어진 수 만큼 발사 했네
    if k == N: 
        if max_result < result:
            max_result = result
        return

    for w in range(W):
        now_bricks = deepcopy(bricks)
        now_height = 0

        while now_height < H and not now_bricks[now_height][w]:
            now_height += 1






    
    

T = int(input())


for tc in range(1, T+1):

    N, W, H = map(int, input().split())

    ori_bricks = [list(map(int, input().split())) for _ in range(H)]

    ans = 0
    for row in range(H):
        for col in range(W):
            if ori_bricks[row][col] != 0:
                ans += 1

    max_result = 0

###############################################################


#구글링한 코드


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def deepcopy(lst):
    new_lst = []
    for y in range(len(lst)):
        temp = []
        for x in range(len(lst[y])):
            temp.append(lst[y][x])
        new_lst.append(temp)
    return new_lst


def erase_bricks(y, x, cur_bricks):
    Q = [(y, x, cur_bricks[y][x])]
    cur_bricks[y][x] = 0

    erased_bricks = 1
    while Q:
        cur_y, cur_x, cur_power = Q.pop(0)

        for p in range(1, cur_power):
            for d in range(4):
                new_y, new_x = cur_y + p * dy[d], cur_x + p * dx[d]
                if -1 < new_y < H and -1 < new_x < W and cur_bricks[new_y][new_x] != 0:
                    if cur_bricks[new_y][new_x] != 1:
                        Q.append((new_y, new_x, cur_bricks[new_y][new_x]))
                    erased_bricks += 1
                    cur_bricks[new_y][new_x] = 0

    return erased_bricks


def sort_bricks(cur_bricks):
    for x in range(W):
        cur_w_bricks = []
        for y in range(H - 1, -1, -1):
            if cur_bricks[y][x] != 0:
                cur_w_bricks.append(cur_bricks[y][x])
                cur_bricks[y][x] = 0

        for h in range(len(cur_w_bricks)):
            cur_bricks[H - 1 - h][x] = cur_w_bricks[h]


def dfs(result, k, bricks):
    global max_result
    if k == N:
        if max_result < result:
            max_result = result
        return

    for w in range(W):
        cur_bricks = deepcopy(bricks)
        cur_h = 0

        while cur_h < H and not cur_bricks[cur_h][w]:
            cur_h += 1

        num_erase = 0
        if cur_h < H:
            num_erase = erase_bricks(cur_h, w, cur_bricks)
            sort_bricks(cur_bricks)
        dfs(result + num_erase, k + 1, cur_bricks)


for tc in range(int(input())):
    N, W, H = map(int, input().split())

    origin_bricks = [list(map(int, input().split())) for _ in range(H)]
    num_all_bricks = 0
    for y in range(H):
        for x in range(W):
            if origin_bricks[y][x] != 0:
                num_all_bricks += 1

    max_result = 0
    dfs(0, 0, origin_bricks)

    print('#{} {}'.format(tc + 1, num_all_bricks - max_result))


################################################################


#교수님 풀이
# 벽돌 깨기 sample
# import copy
# from collections import deque
#
#
# def make_path(now=0, path=[]):
#     if now == N:
#         path_set.add(tuple(path))
#         path_list.append(path)
#         return
#     for i in range(W):
#         # 구슬을 떨어뜨릴 위치 0 ~ w - 1
#         make_path(now + 1, path + [i])
#
#
# def copy_map():
#     temp_MAP = [[0] * W for _ in range(W)]
#     for row in range(H):
#         for col in range(W):
#             temp_MAP[row][col] = MAP[row][col]
#     return temp_MAP
#
#
# def break_block(temp_map, col):
#     # 이번에 터질 부분 터트리기
#     # temp_map의 col번째 열을 터트린다.
#     # bfs
#
#     # 1. 그래프 구성 <- temp_map
#
#     # 2. queue생성 [0] : row, [1] : col, [2] : size
#     q = deque()
#
#     # 3. 시작점 세팅
#     for row in range(H):
#         if temp_map[row][col] != 0:
#             q.append((row, col, temp_map[row][col]))
#             temp_map[row][col] = 0  # 이 블록은 터졌다.
#             break
#     while q:
#         # 4. now꺼내기
#         now = q.popleft()
#         now_row = now[0]
#         now_col = now[1]
#         now_size = now[2]
#
#         dr = [-1, 1, 0, 0]
#         dc = [0, 0, -1, 1]
#         # 5. next찾기 : now로 인해 터질 벽돌 찾기
#         for i in range(4):
#             for pow in range(now_size):
#                 next_row = now_row + pow * dr[i] # ------
#                 next_col = now_col + pow * dc[i] # ------
#
#                 #범위 밖에 있는 것은 제외
#                 if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
#                     continue
#                 #벽돌이 비어있는 것도 제외
#                 if temp_map[next_row][next_col] == 0:
#                     continue
#
#                 # 6. 찾은 next를 추가하기
#                 q.append((next_row, next_col, temp_map[next_row][next_col]))
#                 temp_map[next_row][next_col] = 0  # 터트리기
#
#
# def drop_block(temp_map):
#     # temp_map을 확인하면서 벽돌 떨어트리기
#     for col in range(W):
#         for row in range(H - 1, -1, -1):
#             de = 1
#     # 아래서 위 방향으로 확인함
#     # 빈 공간의 개수 counting
#     # 빈 공간이 아니면 빈 공간의 개수만큼 아래로 떨어트림
#
#
# def proceed():
#     # 순서대로 처리
#     make_path()  # 구슬을 떨어뜨릴 순열 만들기
#     de = 1
#     # temp_map = copy_map()
#     for path in path_set:
#         temp_map = copy.deepcopy(MAP)
#         for now in path:
#             break_block(temp_map, now)  # 터트리기만 함
#             # 터트려서 빈 공간이 생기면 빈 공간만큼 벽돌들이 떨어져야함
#
#
# t = int(input())
# for tc in range(t):
#     N, W, H = map(int, input().split())
#     MAP = [list(map(int, input().split())) for _ in range(H)]
#     path_set = set()
#     path_list = []
#     proceed()



#####################################


# 미완성 코드 => 학습을 위해서
# 벽돌 깨기
import copy
from collections import deque

def make_path(now = 0, path = []):
    if now == N:
        path_set.add(tuple(path))
        path_list.append(path)
        return
    for i in range(W):
        # 구슬을 떨어뜨릴 위치 0 ~ w - 1
        make_path(now + 1, path + [i])

def copy_map():
    temp_MAP = [[0]*W for _ in range(W)]
    for row in range(H):
        for col in range(W):
            temp_MAP[row][col] = MAP[row][col]
    return temp_MAP

def break_block(temp_map, col):
    # 이번에 터질 부분 터트리기
    # temp_map의 col번째 열을 터트린다.
    # bfs

    # 1. 그래프 구성 <- temp_map

    # 2. queue생성 [0] : row, [1] : col, [2] : size
    q = deque()

    # 3. 시작점 세팅
    for row in range(H):
        if temp_map[row][col] != 0:
            q.append( (row, col, temp_map[row][col]) )
            temp_map[row][col] = 0 # 이 블록은 터졌다.
            break
    while q:
        #4. now꺼내기
        now = q.popleft()
        now_row = now[0]
        now_col = now[1]
        now_size = now[2]

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        # 5. next찾기 : now로 인해 터질 벽돌 찾기
        for i in range(4):
            for size in range(now_size):
                next_row = now_row + dr[i] * size # ------
                next_col = now_col + dc[i] * size # ------

                if not( 0 <= next_row < H and 0<= next_col < W):
                    continue
                if temp_map[next_row][next_col] == 0:
                    continue

        # 6. 찾은 next를 추가하기
                q.append((next_row, next_col, temp_map[next_row][next_col]))
                temp_map[next_row][next_col] = 0 # 터트리기

def drop_block(temp_map):
    # temp_map을 확인하면서 벽돌 떨어트리기
    for col in range(W):
        cnt = 0
        for row in range(H-1, -1, -1):
            if temp_map[row][col] == 0:
                cnt += 1
            else :
                temp_map[row + cnt][col] = temp_map[row][col]
            # 아래서 위 방향으로 확인함
            # 빈 공간의 개수 counting
            # 빈 공간이 아니면 빈 공간의 개수만큼 아래로 떨어트림
        for row in range(cnt):
            temp_map[row][col] = 0
            # 빈칸 세팅

def count_block(temp_map): # 맵의 벽돌 개수 counting
    cnt = 0
    for rowMAP in temp_map:
        for block in rowMAP:
            if block != 0:
                cnt += 1
    return cnt

def pro():
    ans = count_block(MAP)
    # 순서대로 처리
    make_path() # 구슬을 떨어뜨릴 순열 만들기
    #temp_map = copy_map()
    for path in path_set:
        temp_map = copy.deepcopy(MAP)
        for now in path:
            break_block(temp_map, now) # 터트리기만 함
            # 터트려서 빈 공간이 생기면 빈 공간만큼 벽돌들이 떨어져야함
            if path == (2, 2, 6):
                de = 1
            drop_block(temp_map)
        ans = min(ans, count_block(temp_map))
    return ans


t = int(input())
for tc in range(t):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    path_set = set()
    path_list = []
    print(f"#{tc + 1} {pro()}")

