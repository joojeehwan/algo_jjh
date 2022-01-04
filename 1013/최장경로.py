'''



dfs로 풀어보자




N개의 정점, M개의 간선 -> 가중치 없는 무방향 그래프 => 최장 경로 길이를 계산

정점의 번호 1 ~ N까지(0번을 사용하지 않음), 같은 번호의 정점 2번이상 x (vistied배열을 사용해서 막자) => 그러나 다른 경로를 확인할때 또 써야하기 때문에 풀어주자!


경로의 길이? => 경로 상에 등장하는 정점의 개수



다른 경로의 경우 중복을 허용하기 위해서!! vistied를 풀어주는 것!

=> 경로가 하나만 있는 것이 아니고 여러개가 있을텐데, 현재 경로에서 체크를 하고 안 풀면!
    다음 경로에서 사용할 수 없으니깐 !

단순 경로 하나 자체 안에서는 중복이 있으면 안되지만!

'''

def dfs(now, distance):

    global ans

    ans = max(ans, distance)

    #next 찾기
    for next in adjL[now]: #인접행렬과 다르게 값이 있는지 없는지 할 필요x 어차피 값이 필요한 녀석들만 가져왔으니깐!
        if visited[next] == False: #안가 본놈

            visited[next] = True
            dfs(next, distance + 1)
            visited[next] = False




T = int(input())


for tc in range(1, T+1):


    V, E = map(int, input().split())

    adjL = [[] for _ in range(V+1)]

    visited = [False] * (V+1)

    ans = 1

    for _ in range(E):
        frm, to = map(int, input().split())
        adjL[frm].append(to)
        adjL[to].append(frm)

    #좌표의 시작점이 고정 x
    for i in range(1, V+1):
        visited[i] = 1
        dfs(i,1)
        visited[i] = 0

    print(f"#{tc} {ans}")


t = int(input())

def dfs(now, cnt):
    global ans
    ans = max(cnt, ans)
    # now : 현재 몇 번 점에 있는가?
    for next in Graph[now]:
        if visited[next]:
            continue
        visited[next] = True
        dfs(next, cnt + 1)
        visited[next] = False

for tc in range(t):
    n, m = map(int, input().split())
    Graph = [[] for  _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        Graph[x].append(y)
        Graph[y].append(x)
    visited = [False] * (n + 1)
    ans = 0
    for i in range(n + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(f"#{tc + 1} {ans}")
