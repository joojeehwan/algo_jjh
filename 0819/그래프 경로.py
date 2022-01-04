

def dfs(now): # now : 나의 현재 위치
    # 2. 기저조건(옵션)
    # 1. now에서 갈 수 있는 next찾기
    for to in range(V + 1):
        if adj[now][to] == 1 and visited[to] == 0:
            # adj[now][to] == 1 : now에서 to로 갈 수 있는 길이 있는가?
            visited[to] = 1 # to에 간다!라고 기록
            dfs(to) # 길이 있으면 가라!

    # 3. 문제가 생길 수 있는 경우

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1) # 들렸던 점인가?
    # adj[from][to]
    for i in range(E):
        f, t = map(int, input().split())
        # f : 어디에서
        # t : 어디로
        adj[f][t] = 1
    start, end = map(int, input().split())
    visited[start] = 1
    dfs(start) # start에서부터 갈 수 있는 모든 곳으로 전부 가보게 된다.
    print("#{} {}".format(tc + 1, visited[end])) # <- 갔던 점인가?

V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    f, t = map(int, input().split())
    adj[f][t] = 1

start, end = map(int, input().split())
visited[start] = 1
dfs(start)

