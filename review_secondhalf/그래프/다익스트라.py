import heapq

V, E = 9, 12
Graph = [ [] for _ in range(V + 1) ]
visited = [False] * (V + 1)
dist = [2134567890] * (V + 1) # 시작점부터의 거리
for _ in range(E):
    f, t, cost = map(int, input().split())
    Graph[f].append( (cost, t) )
    Graph[t].append( (cost, f) )
# 1. 그래프 구성

q = []
# 2. 힙 생성

heapq.heappush(q, (0, 1))
dist[1] = 0
# 3. 시작점 세팅
while q:
    now = heapq.heappop(q)
    now_cost = now[0]
    now_num = now[1]
    # 4. now를 꺼냄 (now : 지금 확정할 수 있는 점)

    # 5. next 찾기
    for cost, to in Graph[now_num]:
        if dist[now_num] + cost >= dist[to]:
            continue # now를 거쳐 가는 방법이 전에 찾아놨던 방법보다 멀다.
        dist[to] = dist[now_num] + cost # now를 거쳐가는 방법이 더 이득이면 갱신
        heapq.heappush(q, (dist[to], to) )

INF = int(1e9)


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 받기.
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


T = int(input())

for tc in range(1, T + 1):

    vertex, edge = map(int, input().split())

    # 1. 그래프 구성
    graph = [[] for _ in range(vertex + 1)]

    distance = [INF] * (vertex + 1)

    for _ in range(edge):
        frm, to, cost = map(int, input().split())
        graph[frm].append((to, cost))

    # 2. 시작점 세팅 => 0번 노드에서 부터 시작함.
    start = 0

    dijkstra(start)

    print(f"#{tc} {distance[vertex]}")