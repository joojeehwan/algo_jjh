
from collections import deque



T = int(input())


for tc in range(1, T+1):

    V, E = map(int, input().split())
    
    
    #1. 연결 구조를 구성

    graph = [[] for _ in range(V + 1)] #빈 이차원 배열 만들어 놓기!

    for _ in range(E) : #거디가 값을 넣는다.
        FROM, TO = map(int, input().split())
        graph[FROM].append(TO)
        graph[TO].append(FROM)


    #2. 큐 생성
    q = deque()
    visited = [0] * (V+1)
    
    #3. 시작점 세팅

    s, g = map(int, input().split())

    visited[s] = 1
    q.append(s)


    while len(q) > 0: # 즉 큐에 값이 있는 동안 진행함!

        #4. q에서 맨 앞점을 꺼냄(now)

        now = q.popleft()

        #5. now에서 갈 수 있는 모든 곳 찾기!
        for next in graph[now]:
            if visited[next] != 0: #이미 한번 가본 곳이면 가지 않는다!
                continue
    
            #6 next를 q에 넣기
            visited[next] = visited[now] + 1 #몇 번쨰에 갓나를 알기 우ㅟ해서! 비지트 배열을 이렇게,,
            q.append(next)

    if visited[g] == 0:
        print("#{} {}".format(tc , 0))
    else:
        print("#{} {}".format(tc , visited[g] - 1))
