

import heapq


T = int(input())


for tc in range(1, T+1):


    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    total_cost = 0

    #인접 리스트 방식으로 입력받기 => 1. 그래프 구성
    for i in range(E):

        frm, to, cost = map(int, input().split())
        graph[frm].append((cost, to))
        graph[to].append((cost, frm))


    hq = []
    visited = [False] * (V + 1)

    #2. 큐 선언 -> heap 선언
    
    
    #3. 시작점(1번점 세팅) -> 시작점에 연결된 선 모두 heap에 추가

    for cost, t in graph[1]:
        heapq.heappush(hq, (cost, t))

    visited[1] = True

    while hq:

        #4. now점 꺼내기 -> now 선 (가장 짧은 선)
        now = heapq.heappop(hq)
        now_cost = now[0]
        now_t = now[1]

        #5. 이 선이 새로운 점을 연결하는 선인가?! <-next 찾기 (판별)

        if visited[now_t]:
            continue

        total_cost += now_cost
        
        #6. 새로운 점 열결 <- next를 큐에 추가

        visited[now_t] = True
        for cost, t in graph[now_t]:
            heapq.heappush(hq, (cost, t))

    print(f"#{tc} {total_cost}")

