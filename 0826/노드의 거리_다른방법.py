

from collections import deque


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())


    #1. 연결 구조를 구성
    graph = [[] for _ in range(V + 1)] #빈 이차원 배열 만들어 놓고!

    for _ in range(E): #거기에다가 값을 넣는다!
        FROM, TO  = map(int, input().split())
        graph[FROM].append(TO) #양방향이 경우 한정! graph[Fr]
        graph[TO].append(FROM)
        

    #2. queue 생성

    q = deque()
    visited = [0] * (V+1)

    #3. 시작점 세팅
    s, g = map(int, input().split())
    visited[s] = 1
    q.append(s)

    #7. 4 ~ 6단계를 반복
    while len(q) > 0:
        # 4. q에서 맨 앞점을 꺼냄(now)
        now = q.popleft()
        for next in graph[now]:
            if visited[next]!= 0:
                continue
            #6 next를 q에 넣기
            visited[next] = visited[now] + 1
            q.append(next)



    if visited[g] == 0:
        print("#{} {}".format(tc , 0))
    else:
        print("#{} {}".format(tc , visited[g] - 1))

        

