from collections import deque



# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

#각 노드에 연결된 간성 정보를 담기 위한 연결 리스트(그래프) 초기화 // 1번 노드 부터 탐색이 시작되니깐 v + 1을 한것
graph = [[] for _ in range(v + 1)]

# 단방향 그래프의 모든 간선 정보를 입력받기

for _ in range(e):
    frm, to = map(int, input().split())
    #frm 노드에서 to 노드로 이동이 가능
    graph[frm].append(to)
    #진입 차수를 1 증가
    indegree[to] += 1
    
#위상 정렬 함수

def topology_sort():
    result = [] #알고ㅈ리즘 수행 결과를 담을 리스트
    q = deque()
    
    #처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for node in range(1, v+1):
        if indegree[node] == 0:
            q.append(node)
            
        
    #큐가 빌때까지 반복

    while q:

        now = q.popleft()
        #여기서 결과를 담는군!
        result.append(now)
        
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for next in graph[now]:
            indegree[next] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[next] == 0:
                q.append(next)
                
    #위상 정렬를 수행한 결과 출력

    for node in result:
        print(node, end=" ")

topology_sort()

            
    
