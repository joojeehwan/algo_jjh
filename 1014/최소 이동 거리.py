
import heapq

INF = int(1e9)

def dijkstra(start):

    q = []

    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 받기.
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


T = int(input())

for tc in range(1, T+1):


    vertex, edge = map(int, input().split())

    #1. 그래프 구성
    graph = [[] for _ in range(vertex + 1)]

    distance = [INF] * (vertex + 1)
    
    for _ in range(edge):
        frm, to, cost  = map(int, input().split())
        graph[frm].append( (to,cost))

    #2. 시작점 세팅 => 0번 노드에서 부터 시작함.
    start = 0

    dijkstra(start)

    print(f"#{tc} {distance[vertex]}")
        




#교수님 풀이
# 최소 이동 거리
import heapq

t = int(input())

for tc in range(t):
    N, E = map(int, input().split())
    Graph = [ [] for _ in range(N + 1)]
    dist = [2134567890] * (N + 1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        Graph[s].append( (w, e) )

    # graph 구성

    # 힙생성
    q = []

    # 시작점 세팅
    heapq.heappush(q, (0, 0))
    dist[0] = 0

    while q:
        now = heapq.heappop(q)
        now_cost = now[0]
        now_num = now[1]

        for cost, to in Graph[now_num]:
            if dist[now_num] + cost >= dist[to]:
                continue
            dist[to] = dist[now_num] + cost
            heapq.heappush(q, (dist[to], to) )
    print(f"#{tc + 1} {dist[N]}")

