'''


전력난

MST 정리,,,

크루스칼 정리

프림 정리

불이 켜진 길로만,,!


노드의 수 m

간선의 수 n

그래프의 형태? 어떤 두집을 골라도 서로 왕래 할 수 있는 경로가 항상 있다.

x, y , z : x번 집과 y번 집이 양방향으로 연결되어 있고 그 아동에 드는 비용이 z라는 뜻

도시상의 모든 길의 거리의 합은 2의 31 미터보다 작다.

입력의 끝에서는 첫 줄에 0이 2개 주어진다. 0 0 을 만나면 입력이 종료!


불이 켜진 길로만 간다는 게 무슨 소리징?!

"길의 가로등을 켜 두면 하루에 길의 미터 수만큼 돈이 들어가는데, 일부를 소등하여 그만큼의 돈을 아낄 수 있따."

집 기준이 아니라 길 기준이네?!

불이 켜진 길만으로 서로를 왕래? => 즉, 한번 간 길을 가지 않곳! 모든 길을 갈 수 있는 방법!


즉 "

약간 한붓 그리기 해서 가장 큰 값을 구하는 건가?!


아니 최소 신장인데? 최대 값을? 뭐지?


아 문제의 출력이 절약할 수 있는 최대 비용이네!

절약한 금액을 요구했으므로 전체 비용에서 크루스칼 알고리즘으로 구한 최소 비용을 뺀 값을 출력하면 됩니다.
why?
'''
import sys

import heapq


input = sys.stdin.readline


while True :
    V, E = map(int, input().split())

    if V == 0 and E == 0 :
        break

    graph = [[] for _ in range(V+1)] #idx : 노드번호 value: (비용, 갈 수 있는 점)

    total_cost = 0

    graph_cost = 0

    #그래프 구성 => 양방향
    for _ in range(E):

        frm, to, cost = map(int, input().split())
        graph[frm].append((cost, to))
        graph[to].append((cost, frm))
        graph_cost += cost


    #큐와 비짓배열,,! 한 번 간 길은 다시 안감!
    hq = []

    visted = [False] * (V + 1)



    #시작점 세팅 0번 노드에서 부터 시작 왜 for문을 사용해서!? 노드가 여러개 연결되어 있을 수도 있음!

    for cost, to in graph[0]:
        heapq.heappush(hq, (cost, to))


    visted[0] = True

    while hq:

        #힙 큐를 사용해서 가장 최소의 값이 도출 됨!
        now = heapq.heappop(hq)
        now_cost = now[0]
        now_to = now[1]

        #새로운 점을 연결하는 선만! 한번 한 곳에
        if visted[now_to]:
            continue

        #갈 수 있는 점에 대해서 처리
        total_cost += now_cost

        visted[now_to] = True

        #다음 번 갈 수 있는 곳 찾기
        for cost, to in graph[now_to]:
            heapq.heappush(hq, (cost, to))


    print(graph_cost - total_cost)




