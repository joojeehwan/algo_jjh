

#크루스칼 알고리즘

def Find(x):
    
    #루트 노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
    if parents[x] != x:
        parents[x] = Find(parents[x])
    return parents[x]


def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


v, e = map(int, input().split())

#부모 테이블 초기화
parents = [0] * (v + 1)

#부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parents[i] = i

#parent = [i for i in ragnge(v+1)]

#모든 간선에 대한 정보 받기
edges = []

for _ in range(e):
    n1, n2, cost = map(int, input().split())
    edges.append((cost, n1, n2))


edges.sort()
total_cost = 0
for cost, n1, n2 in edges:
    if Find(n1) == Find(n2):
        continue
    Union(n1, n2)
    total_cost += cost




#프림 알고리즘

import heapq

T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]


    totla_cost = 0

    # 인접리스트의 형태로 입력받음

    for i in range(E):
        frm, to, cost = map(int, input().split())

        graph[frm].append((cost, to))
        graph[to].append((cost, frm))

    # 1. 그래프 구성
    hq = []
    visited = [False] * (V + 1)

    # 2. 큐 선언 -> heap

    for cost, t in graph[0]:
        heapq.heappush(hq, (cost, t))

    visited[0] = True

    while hq:

        now = heapq.heappop(hq)
        now_cost = now[0]
        now_t = now[1]

        # 5. 이 선이 새로운 점을 연결하는 선인가?! <- next 찾기(판별)
        if visited[now_t]:
            continue

        totla_cost += now_cost

        visited[now_t] = True
        for cost, t in graph[now_t]:
            heapq.heappush(hq, (cost, t))

    print(f"#{tc} {totla_cost}")
