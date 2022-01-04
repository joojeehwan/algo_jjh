'''


방법 2가지 

프림 or 크루스칼 알고리즘

프림으로 다시 해보자!

'''



import heapq



T = int(input())


for tc in range(1, T+1):

    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    
    totla_cost = 0
    
    #인접리스트의 형태로 입력받음

    for i in range(E):

        frm, to, cost = map(int, input().split())

        graph[frm].append( (cost,to))
        graph[to].append((cost,frm))

    #1. 그래프 구성
    hq = []
    visited = [False] * (V+1)

    #2. 큐 선언 -> heap


    for cost, t in graph[0]:
        heapq.heappush(hq, (cost, t))

    visited[0] = True

    while hq:

        now = heapq.heappop(hq)
        now_cost = now[0]
        now_t = now[1]

        #5. 이 선이 새로운 점을 연결하는 선인가?! <- next 찾기(판별)

        if visited[now_t]:
            continue

        totla_cost += now_cost

        visited[now_t] = True
        for cost, t  in graph[now_t]:
            heapq.heappush(hq, (cost, t))

    print(f"#{tc} {totla_cost}")




# 최소 신장 트리(Kruskal)
import heapq

def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px

t = int(input())
for tc in range(t):
    V, E = map(int, input().split())
    parents = [ i for i in range(V + 1)]
    edges = []
    for _ in range(E):
        n1, n2, cost = map(int, input().split())
        edges.append( (cost, n1, n2) )
    edges.sort() #코스트 기준 가장 작은 값부터 순서대로 할려고!
    total_cost = 0
    for cost, n1, n2 in edges:
        if Find(n1) == Find(n2):
            continue
        Union(n1, n2)
        total_cost += cost


    print(f"#{tc + 1} {total_cost}")
