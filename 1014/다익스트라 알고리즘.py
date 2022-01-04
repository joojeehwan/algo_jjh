''''

<다익스트라 알고리즘>
거리가 짧은 점 부터 확정

확정지으면서 주변 점들 거리 갱신

거리가 음수일떄는 사용할 수 없음.. ex) 음수 사이클,, 무한히 값이 줄어든다!

'''


# dijkstra smaple code
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
import heapq

V, E = 9, 12
Graph = [ [] for _ in range(V + 1) ]


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
    for cost, to in Graph[now_num]: # 아 이게 왜 TO 인지 알았다! 그래프의 구성을 생각!
        if dist[now_num] + cost >= dist[to]:
            continue # now를 거쳐 가는 방법이 전에 찾아놨던 방법보다 멀다.
        dist[to] = dist[now_num] + cost # now를 거쳐가는 방법이 더 이득이면 갱신
        heapq.heappush(q, (dist[to], to) )
de = 1



#반복문으로 구현된 다익스트라
# 반복 dijkstra
import sys


def dijkstra(f, t):
    # f라는 점에서 t라는 점까지 얼마나 걸리는가?
    # 1. 그래프 구성 <-
    visited = [False] * (n + 1)# 확정 되었는가?
    dist = [2134567890] * (n + 1)

    # 3. 시작점 세팅
    dist[f] = 0

    for _ in range(n):
        # n번 반복해서 총 n개의 점들을 확정할 것이다.

        # 아직 확정하지 않은 점들 중 가장 가까운 점(확정할 점 찾기)
        min_dist = 2134567890
        min_num = 0
        for i in range(1, n + 1):
            if dist[i] < min_dist and not visited[i]:
                min_dist = dist[i]
                min_num = i

        visited[min_num] = True # 너 확정!

        for cost, to in Graph[min_num]:
            if min_dist + cost >= dist[to]:
                continue
            dist[to] = min_dist + cost
    return dist[t]


n = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
Graph = [ [] for _ in range(n + 1) ]

for _ in range(e):
    f, t, cost = map(int, sys.stdin.readline().split())
    Graph[f].append( (cost, t) )
start, end = map(int, sys.stdin.readline().split())
print(dijkstra(start, end))



#힙 다익스트라

# heap dijkstra
import sys
import heapq

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

        # 아직 확정하지 않은 점들 중 가장 가까운 점(확정할 점 찾기)
        now =  heapq.heappop(q)
        min_num = now[1]
        min_dist = now[0]
        if visited[min_num]: #이미 간곳은 가지 않게 처리하네?! 속도 향상!
            continue
        visited[min_num] = True
        for cost, to in Graph[min_num]:
            if min_dist + cost >= dist[to]:
                continue
            dist[to] = min_dist + cost
            heapq.heappush(q, (dist[to], to))
    return dist[t]
"""
    선의 개수 * log(선의 개수) <- 시간 복잡도
    선의 개수 : E, 점의 개수 V
    ElogE ->     E가 최대한 많은경우 E = n^2
    ElogV <- dijkstra의 시간 복잡도

    log(힙내부 데이터 수) <- 삽입과 삭제
"""
n = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
Graph = [ [] for _ in range(n + 1) ]

for _ in range(e):
    f, t, cost = map(int, sys.stdin.readline().split())
    Graph[f].append( (cost, t) )
start, end = map(int, sys.stdin.readline().split())
print(dijkstra(start, end))