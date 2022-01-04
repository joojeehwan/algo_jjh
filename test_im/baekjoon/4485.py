'''

녹색 옷 입은 애가 젤다지?


누가 보아도 다익스트라 문제,,!

근데 다익스트라라는 그래프를  2차원 배열에 옮긴 형태!
다익스트라 적는 거 복습 하고 풀어보자!

'''


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


#델타 배열 만들기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():

    q = []
    heapq.heappush(q, (MAP[0][0],0,0))
    distance[0][0] = 0

    while q:
        #가장 비용이 적은 값 꺼내기(최소힙)
        min_dist, min_now_row, min_now_col = heapq.heappop(q)

        # #현재 노드가 이미 처리된 적이 있는 노드라면 무시 => visited배열 처리와 같은 기능
        # if distance[min_now_row][min_now_col] < min_dist:
        #     continue
        #이거 넣으면 다익스트라 안돈다!

        #현재 좌표와 연결된 다른 인접한 좌표들의 비용들을 확인(사방)
        for dir in range(4):

            next_row = min_now_row + dr[dir]
            next_col = min_now_col + dc[dir]
            
            #일단 범위 체크 => 이차원 배열
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue

            cost = min_dist + MAP[next_row][next_col]
            # 현재 좌표를 거쳐서, 다른 좌표로 이동하는 거리가 더 짧은 경우

            if cost < distance[next_row][next_col]:
                distance[next_row][next_col] = cost
                heapq.heappush(q, (cost, next_row, next_col))



tc = 1
while True:
    #와 이런 입력도 있구먼,,
    N = int(input())

    if N == 0:
        break

    MAP = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    de = 1
    dijkstra()

    print(f"Problem {tc}: {distance[N-1][N-1]}")

    tc += 1


