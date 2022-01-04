'''

다익스트라를 반복문으로도 가능 방법 1

heap으로 다익스트라 반복문 가능 방법 2


'''



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

        #시간을 줄여준다!
        if visited[min_num]:
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