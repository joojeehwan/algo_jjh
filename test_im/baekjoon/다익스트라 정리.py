"""
1 2 4
1 3 11
1 4 7
2 5 25
3 7 46
4 5 18
4 6 1
5 8 13
6 7 50
6 8 4
7 9 1000
8 9 77
"""

# 교수님 방식 다익스트라


# 힙 다익스트라


# 근데 여기서 visied배열을 사용하면 속도를 올릴 수 있음! => 분기 조건을 추가함으로서!

# import heapq
#
# # 1. 그래프 구성
# V, E = 9, 12  # 노드와 간선의 개수
# Graph = [[] for _ in range(V + 1)]  # 입력받을 그래프를 미리 만듬!
#
# dist = [123456789] * (V + 1)  # 시작점부터의 거리
#
# for _ in range(E):
#     frm, to, cost = map(int, input().split())
#     Graph[frm].append((cost, to))
#     Graph[to].append((cost, frm))
#
# # 2. 힙 생성
# q = []
#
# # 3. 시작점 세팅
# heapq.heappush(q, (0, 1))  # 시작 노드의 번호와 시작노드니깐 cost 0
# dist[1] = 0  # 시작노드에서 시작노드까지 가는 드는 최소비용은 언제나 0
#
# while q:
#     # 가장 최단 거리가 짤븡 노드에 대한 정보 꺼내기(최소힙을 사용하기 때문에 그냥 꺼내기만 해도 가능)
#     now = heapq.heappop(q)
#     now_cost = now[0]
#     now_node_num = now[1]
#     # 4. now를 꺼냄 (now : 지금 확정할 수 있는 점)
#
#     # 5. next를 찾기
#
#     for cost, to in Graph[now_node_num]:  # 현재 노드번호에 연결되어 있는 녀석들을 체크!
#         if dist[now_node_num] + cost >= dist[to]:
#             continue  # now를 거쳐 가는 방법이 전에 찾아놨던 방법보다 더 멀다! 그럼 무시해!
#
#         dist[to] = dist[now_node_num] + cost  # 그게 아니라면! 현재 노드번호에 연결되어있는 다음 녀석을 가는 녀석은
#         # 현재 노드번호까지 온 거리 + 그 다음 노드 번호까지의 거리를 더한 녀석!
#         heapq.heappush(q, (dist[to], to))  # 이제 이 거리는 확정!

import sys


# visited배열 추가한 방식!

def dijkstra(f, t):
    # f라는 점에서 t라는 점까지 얼마나 걸리는가?
    # 1. 그래프 구성 <-
    dist = [2134567890] * (n + 1)
    q = []
    visited = [False] * (n + 1)
    # 3. 시작점 세팅
    dist[f] = 0
    heapq.heappush(q, (0, f))

    while q:
        # n번 반복해서 총 n개의 점들을 확정할 것이다.

        now = heapq.heappop(q)
        min_num = now[1]
        min_dist = now[0]
        if visited[min_num]:  # 이미 간곳은 가지 않게 처리하네?! 속도 향상!
            continue
        visited[min_num] = True

        # 아직 확정하지 않은 점들 중 가장 가까운 점(확정할 점 찾기)
        for cost, to in Graph[min_num]:
            if min_dist + cost >= dist[to]:
                continue
            dist[to] = min_dist + cost
            heapq.heappush(q, (dist[to], to))
    return dist[t]


n = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
Graph = [[] for _ in range(n + 1)]

for _ in range(e):
    f, t, cost = map(int, sys.stdin.readline().split())
    Graph[f].append((cost, t))
start, end = map(int, sys.stdin.readline().split())
print(dijkstra(start, end))

# 이코테 풀이 버젼

'''
입력 
노드개수, 간선개수
시작노드번호
a b c : a에서 b로 가는 비용이 c
6 11
1 
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

'''


import heapq
import sys
input = sys.stdin.readline



INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):

    frm, to, cost = map(int, input().split())
    graph[frm].append((cost,to))

def dijkstra_2(start):

    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        min_dist, min_now_node = heapq.heappop(q)

        #현재 노드가 이미 처리된 적이 있는 노드라면 무시 => visited배열 처리와 같은 기능
        if distance[min_now_node] < min_dist:
            continue

        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node_cost, next_node_to in graph[min_now_node]:
            cost = min_dist + next_node_cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_node_to]:
                distance[next_node_to] = cost
                heapq.heappush(q, (cost, next_node_to))

dijkstra_2(start)


for i in range(1, n+1):
    #도달할 수 없는 경우, 무한이라고 출력

    if distance[i] == INF:
        print("못가")
    else:
        print(distance[i])




