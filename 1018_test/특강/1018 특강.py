'''

BFS 일정한 틀이 있음

'''

#큐 임포트
from collections import deque

#델타 배열
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# row = 2
# col = 2
#
# MAP = [
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]
#        ]
# for i in range(4):
#     next_row = row + dr[i]
#     next_col = col + dc[i]
#
#     MAP[next_row][next_col] = 1
#
# for i in range(4):
#     print(MAP[i])

#BFS
'''
이차원 배열을 그래프의 연결이라 생각하고,,! 

1. MAP 그래프 구성

2. QUEUE 튜플을 만들어 놓는다.

3. 델타 배열

규칙
1) 다음  갈 수 있는 곳 예약
2) 탐색

'''
'''
문제1) bloom
꽃이 3개 있는데 동시에 핀다! 
map을 언제 다 채울 수 있나?!

약간 토마토 같은 문제!  

'''


# #1. 그래프 구성
# MAP = [
#     [0,0,1,0],
#     [0,0,0,1],
#     [0,0,0,0],
#     [0,1,0,0]
# ]
#
# #2. 큐 생성
# q = deque()
#
# #3. 시작 값 세팅
# q.append((3,1))
# q.append((0,2))
# q.append((1,3))
#
# #큐가 비워질떄까지,,! 4 ~ 6번 실행
# ans = 0 #정답을 담을 변수 만들기
# while q:
#
#     #4. 큐의 맨앞 꺼내기
#     start = q.popleft()
#     now_row = start[0]
#     now_col = start[1]
#     #5.next값 찾기
#     for i in range(4):
#         next_row = now_row + dr[i]
#         next_col = now_col + dc[i]
#
#         if next_row < 0 or next_col < 0 or next_row >= 4 or next_col >=4:
#             continue
#         #지금 이 풀이는 맵자체를 visited 배열로 만들어서 사용하는 것
#         if MAP[next_row][next_col] != 0: #이미 간곳이면 가지 않는다!
#             continue
#
#         MAP[next_row][next_col] = MAP[now_row][now_col] + 1
#         q.append((next_row, next_col))
#         ans = MAP[next_row][next_col]
#
#
# print(ans)


'''

문제 2) 미로 찾기

이차원 배열에 미로가 있음,, 벽(1)도 있고! 갈수 있는 길(0) 

0,0에서 출발해서 4,0까지 가야되는데

최소한의 거리로 가면 몇번 이냐?! => 전형적인 BFS문제



1)
point! 싸이클을 막기! 
used 배열, visted 배열


2) 최소 몇번에 가는지 level도 추가! 


SO) 내가 찾고자 하는 값을 찾으면 BREAK로 멈춰야 하는데,,! 이중 반복에서 하나만 나가니깐!
함수로 만들어서 나가버리자!


여러가지 경로를 찾는건 dfs(백트래킹)으로하는게,,! 여러가지 다 가볼 수 있음!
bfs는 최소경로를 구할때!

내가 온 경로를 적는 건 path를 만들면돼! 

'''


# MAP = [
#     [0,1,1,1,0],
#     [0,0,0,1,0],
#     [0,1,1,1,0],
#     [0,0,0,0,0]
# ]
#
# Q = deque()
# visited = [[0] * 5 for _ in range(4)]
#
# def bfs():
#
#     Q.append((0,0))
#     visited[0][0] = 1
#
#     while Q:
#
#         now = Q.popleft()
#         now_row = now[0]
#         now_col = now[1]
#
#         if now_row == 0 and now_col == 4:
#             return visited[now_row][now_col]
#
#         for i in range(4):
#             next_row = now_row + dr[i]
#             next_col = now_col + dc[i]
#
#             if next_row < 0 or next_col < 0 or next_row >=4 or next_col >= 5:
#                 continue
#
#             if MAP[next_row][next_col] == 1:
#                 continue
#
#             if visited[next_row][next_col] != 0:
#                 continue
#
#             visited[next_row][next_col] = visited[now_row][now_col] + 1
#             Q.append((next_row, next_col))
#
#     return -1
#
# ans = bfs()
# print(ans - 1)


'''
사진 확인

문제 3
한 지점에서 b지점들까지의 최소거리
(하나의 좌표에서, 여러개의 좌표들간의 최소거리)




문제4
섬A과 섬B사이의 최단 거리를 구해라!
(즉 하나의 좌표가 아니라 여러개의 좌표들간의 최소 거리,,!)

sol)

1) 이중포문을 돌려서 섬B의 좌표를 구한다1

2) 찾은 섬B의 좌표를 활용해서 섬의 좌표들을 Q에 전부 등록한다.(BFS1회)

3) Q에 섬B의 좌표들을 등록한 상태에서 BFS를 돌리면 된다!(BFS1회)
(이러면)

BFS를 2번 돌리면 된다.

문제5

섬 SIZE구하기



<섬의 개수>
1) 이중 포문돌려서 한 지점 구하고 BFS를 돌린다!

2) 그리고는 섬을 MAP에서 지워준다! 침몰시켜준다= 바다와 같게 만들어 (다음 검색을 위해서)

3) 최종적으로 BFS의 횟수가 섬의 갯수(칸의 갯수가 아니라 이어진 섬들의 갯수가)


<섬의 크기>

위와 같은 방식,,! 그런데 섬의 크기는 Q에 몇개가 차는지가 바로 SIZE(칸수)

'''

#섬의 개수 예시,, 이렇게 있으면 섬의 개수는 2개

MAP = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [1,0,0,0,0]
]

Q = deque()

def bfs(start_row, start_col):


    MAP[start_row][start_col] = 0
    Q.append((start_row,start_col))

    while Q:

        now = Q.popleft()
        now_row = now[0]
        now_col = now[1]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >=4 or next_col >= 5:
                continue

            if MAP[next_row][next_col] == 0:
                continue

            MAP[next_row][next_col] = 0
            Q.append((next_row, next_col))

    return -1
ans = 0
for row in range(4):
    for col in range(5):
        if MAP[row][col] == 1:
            bfs(row, col)
            ans += 1

print(ans)



'''

과수원,,

가까운 사과를 찾아가서 수확

총 12회 만에 도착,,! 


1) 시작점에서 bfs를 돌림

2) 가장 가까운 사과 하나 발견하면 -> 그 곳에서 다시 이제 bfs를 돌려서! 다음 가장 가까윤 사과를 찾음

3) 그렇게 최소 이동거기를 구함

'''


'''

탱크 문제

앞으로 한칸 전진, 방향 전화 왼쪽 90도, 방향 전화 오른쪾 90도

bfs돌리면 되는데!

델타 배열을 포문으로 안돌리고! 하나하나 따로처리!

사진 확인

visited 배열이 3차원,,! 탱크가 어느 방향을 보고 있는거에 따라서
같은 지점에 가더라도 다른 것이라서,,!

'''


'''

A, B가 있음,, ! 애네 둘다 사방향으로 동시에 움직임

A랑 B랑 서로 만나는데 최소횟수!

SOL) A, B묶어서,,! 가능 방향을 생각 16가지의 델타 배열이 있겠네! 

큐에 (AY, AX) , (BY, BX), LEV
VISTED는 4차원 배열을 사용해야함 A와 B의 좌표를 row, col의 2개의 좌표니간!


아 이건 좀 어려워보인다,,! 

'''


'''

플러드 필 설계 방법


1. 큐에 무엇을 넣을지 설정! 

EX) row, col만 들어갈지,, 레벨도 들어가늕,,, 오작교 사용유무

2. used vs best배열

best 배열?! [오작교 사용여부][row][col]에 몇번만에 도착했는지! 







'''

# # include <iostream>
# # include <queue>
# using
# namespace
# std;
# int
# N, M;
# int
# map[11][11];
# int
# best[2][11][11];
# int
# direct[4][2] = {-1, 0, 1, 0, 0, 1, 0, -1};
# struct
# Node
# {
#     int
# y, x;
# int
# isUsedM;
# int
# lev;
# };
# queue < Node > q;
# int
# getNextLev(int
# nowLev, int
# ny, int
# nx, int
# T)
# {
# if (T == 1)
# return nowLev + 1;
# if (T == 0) T = M;
# return ((nowLev / T) + 1) * T;
# }
# int
# run()
# {
# q.push({0, 0, 0, 0});
# while (!q.empty()) {
# Node now = q.front();
# q.pop();
# for (int t = 0; t < 4; t++) {
# int ny = now.y + direct[t][0];
# int nx = now.x + direct[t][1];
# if (ny < 0 | | nx < 0 | | ny >= N | | nx >= N)
# continue;
# if (now.isUsedM == 1 & & map[ny][nx] == 0) continue;
# // 새로운
# 다리를
# 사용할지
# 결정
# int
# nextUsedM = now.isUsedM;
# if (now.isUsedM == 0 & & map[ny][nx] == 0) nextUsedM = 1;
# // 절벽
# 연속
# 2
# 개
# 방지
# if (map[now.y][now.x] != 1 & & map[ny][nx] != 1) continue;
#
# // 시간
# 계산하기
# int
# nextLev = getNextLev(now.lev, ny, nx, map[ny][nx]);
#
# // 최적인지
# 확인
# if (best[nextUsedM][ny][nx] <= nextLev) continue;
# best[nextUsedM][ny][nx] = nextLev;
# q.push({ny, nx, nextUsedM, nextLev});
# }
# }
# int
# mini = best[0][N - 1][N - 1];
# if (mini > best[1][N - 1][N - 1])
# mini = best[1][N - 1][N - 1];
# return mini;
# }
# int
# main()
# {
# ios::sync_with_stdio(0);
# // freopen("text.txt", "r", stdin);
# int
# tc;
# cin >> tc;
# for (int i = 1; i <= tc; i++) {
#     cin >> N >> M;
# for (int y = 0; y < N; y++) {
# for (int x = 0; x < N; x++) {
# cin >> map[y][x];
# }
# }
# while (!q.empty()) q.pop();
#
# for (int y = 0; y < 11; y++) {
# for (int x = 0; x < 11; x++) {
# best[0][y][x] = 21e8;
# best[1][y][x] = 21e8;
# }
# }
# int
# ret = run();
# cout << "#" << i << " " << ret << endl;
# }
# return 0;
# }
#
#
#
# #######################
#
#
# # include <iostream>
# using
# namespace
# std;
# int
# N, O, M;
# int
# nums[11];
# char
# opers[5];
# int
# targetNum;
# int
# best[1000];
# int
# used[1000];
# int
# johap[1000];
# int
# joCnt;
# int
# johapNumCnt[1000];
# int
# johapUsed[1000];
# void
# init()
# {
# for (int i = 0; i < 1000; i++) {
#     best[i] = 99;
# used[i] = 0;
# }
# for (int i = 0; i < joCnt; i++) {
#     int num = johap[i];
# best[num] = johapNumCnt[i];
# }
# }
# int
# getCalResult(int
# a, char
# oper, int
# b)
# {
# if (oper == '*') return a * b;
# if (oper == '-') return a - b;
# if (oper == '/') return a / b;
# return a + b;
# }
# void
# getMinTouchCnt(int
# touchCnt, int
# now)
# {
# for (int x = 0; x < O; x++) {
# for (int i = 0; i < joCnt; i++) {
# int num = johap[i];
# int nextCnt = touchCnt + johapNumCnt[i] + 1;
# if (nextCnt > M - 1)
# break;
# if (opers[x] == '/' & & num == 0) continue;
# int
# next = getCalResult(now, opers[x], num);
#
# if (opers[x] == '+' & & next > 999) break;
# if (opers[x] == '-' & & next < 0) break;
# if (opers[x] == '*' & & next > 999) break;
# if (used[next] == 1) continue;
# if (best[next] <= nextCnt) continue;
#
# best[next] = nextCnt;
# used[next] = 1;
# getMinTouchCnt(nextCnt, next);
# used[next] = 0;
# }
# }
# }
# void
# getJoHapDFS(int
# lev, int
# sum)
# {
# for (int i = 0; i < N; i++) {
#     int next = sum * 10 + nums[i];
# if (next > 999)
# continue;
# if (johapUsed[next] == 1) continue;
# johapUsed[next] = 1;
# getJoHapDFS(lev + 1, next);
# }
# }
# void
# getJohap()
# {
# for (int i = 0; i < 1000; i++) {
#     johap[i] = 0;
#     johapUsed[i] = 0;
#     johapNumCnt[i] = 0;
# }
# joCnt = 0;
# getJoHapDFS(0, 0);
# for (int i = 0; i < 1000; i++)
# {
# if (johapUsed[i] == 0) continue;
# johap[joCnt] = i;
# if (i < 10) johapNumCnt[joCnt] = 1;
# else if (i < 100) johapNumCnt[joCnt] = 2;
# else if (i < 1000) johapNumCnt[joCnt] = 3;
# joCnt + +;
# }
# }
# int
# main()
# {
# // freopen("text.txt", "r", stdin);
#
# int
# tcCnt;
# cin >> tcCnt;
# for (int tc = 1; tc <= tcCnt; tc++)
# {
# cin >> N >> O >> M;
#
# for (int i = 0; i < N; i++) cin >> nums[i];
# for (int i = 0; i < O; i++) {
#     int t;
# cin >> t;
# if (t == 1) opers[i] = '+';
# if (t == 2) opers[i] = '-';
# if (t == 3) opers[i] = '*';
# if (t == 4) opers[i] = '/';
# }
# cin >> targetNum;
# getJohap();
# init();
# int
# ret = 0;
# if (best[targetNum] != 99) ret = best[targetNum];
# else {
# for (int i = 0; i < joCnt; i++) {
# getMinTouchCnt(johapNumCnt[i], johap[i]);
# }
# ret = best[targetNum] + 1;
# }
#
# if (best[targetNum] == 99) ret = -1;
# cout << "#" << tc << " " << ret << "\n";
# }
# return 0;
# }