'''


이건 다익스트라 처럼 보인다!


서로 다른 가중치,, 심지어 양의 가중치,, 그래프,,,


단방향 간선, 노드는 1번 부터 시작


2번 다익스트라 해서,,!

1번 다익스트라) 주어진 노드에서 x번의 집까지 가는 가장 적은 비용의 경로

2번 다익스트라) x번 집에서 주어진 노드까지 가는 가장 적은 비용의 경로



이렇게 전체 노드들 중에서 x번으로 오고 가는 시간이 가장 많이 걸리는 노드가 몇번인지 구하라!


다익스트라를 2번 사용하니깐 함수로 빼는게 훨씬 효율적이다.





진출 진입을 바꿔도 완전 굿이네,, 저런 풀이가 있다니,,히!



'''
import heapq

INF = int(1e9)


def dijkstra(adj_list, distance):
    # 큐 생성
    q = []

    # 시작점 세탕
    heapq.heappush(q, (0, X))

    # 큐 반복
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 받기.
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in adj_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


T = int(input())

for tc in range(1, T + 1):

    # N : 노드의 개수
    # M : 간선의 갯수
    # X : 가야하는 목적 노드 번호

    N, M, X = map(int, input().split())

    adj_list_ft = [[] for _ in range(N + 1)]
    adj_list_tf = [[] for _ in range(N + 1)]

    distance_frm_to = [INF] * (N + 1)
    distance_to_frm = [INF] * (N + 1)

    for _ in range(M):
        frm, to, cost = map(int, input().split())
        adj_list_ft[frm].append((to, cost))
        adj_list_tf[to].append((frm, cost))

    distance_frm_to[X] = 0
    distance_to_frm[X] = 0

    dijkstra(adj_list_ft, distance_frm_to)
    dijkstra(adj_list_tf, distance_to_frm)



    max_distance = 0
    for i in range(1,N + 1):
        max_distance = max(max_distance, distance_frm_to[i] + distance_to_frm[i])


    print(f"#{tc} {max_distance}")


