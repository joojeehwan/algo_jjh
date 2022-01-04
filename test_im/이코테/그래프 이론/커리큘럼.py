from collections import deque
import copy

#노드의 개수 입력받기

v = int(input())

indegree = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]

time = [0] * (v + 1)

#방향 그래프의 모든 간선정보 받기

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]: #-1을 입력에 넣을려고! 
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) #배열 복사시에는! 조심!
    q = deque()

    #처음 시작할때는 진입차수가 0인 노드를 큐에 삽입
    for node in range(1, v+1):
        if indegree[node] == 0:
            q.append(node)
            
        
    #큐가 빌떄까지 반복

    while q:
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1배기

        for i in graph[now]:
            #인접한 노드에 대해서 현재보다 강의 시간이 더 긴경우를 찾는다면, 더 오랜시간이 걸리는 경우의 시간값을 저장하는 방식으로 결과 테이블 갱신
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)


    for i in range(1, v+ 1):
        print(result[i])

topology_sort()


#
# arr = [1,2,3,4,5]
#
# print(arr[1:-1])
