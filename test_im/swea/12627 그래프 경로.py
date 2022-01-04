'''

이걸 왜 안풀었엇지?!

dfs 문제

'''



def dfs(now):  # now : 나의 현재 위치
    # 2. 기저조건(옵션)
    # 1. now에서 갈 수 있는 next찾기
    for to in range(V + 1):
        if adj[now][to] == 1 and visited[to] == 0:
            # adj[now][to] == 1 : now에서 to로 갈 수 있는 길이 있는가?
            visited[to] = 1  # to에 간다!라고 기록
            dfs(to)  # 길이 있으면 가라!

    # 3. 문제가 생길 수 있는 경우


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)  # 들렸던 점인가?
    # adj[from][to]
    for i in range(E):
        f, t = map(int, input().split())
        # f : 어디에서
        # t : 어디로
        adj[f][t] = 1
    start, end = map(int, input().split())
    visited[start] = 1
    dfs(start)  # start에서부터 갈 수 있는 모든 곳으로 전부 가보게 된다.
    print("#{} {}".format(tc + 1, visited[end]))  # <- 갔던 점인가?


def dfs(now): #now : 나의 현재 위치

    #2. 기저조건 (옵션)
    #1. now에서 갈 수 있는 next 찾기

    for to in range(V + 1): #노드의 수만큼 갈 수 있는 경우의 수가 존재
        if adj[now][to] == 1 and visited[to] == 0: #인접 행렬의 경우는 갈 수 있는 점인지도 체크해야 한다!
            visited[to] = 1
            dfs(to) #길이 있어 가!
            #굳이 다시 돌아올 필요가 없자나! 일단 가서 경로가 있는지 없는지만 체크 하는 거니깐!

T = int(input())
#인접 행렬로 풀엇구나?
for tc in range(1, T + 1):

    V, E = map(int, input().split())
    #인접 행렬 풀이!
    adj = [[0] * (V + 1) for _ in range(V + 1)] # V + 1의 이유?! 노드는 1번 부터 다루니깐!
    visited = [0] * (V + 1) #당연히 1차원 배열 노드로 체크 하는 거니깐!

    for i in range(E):
        frm, to = map(int, input().split())
        adj[frm][to] = 1

    start, end = map(int, input().split())
    visited[start] = 1 #처음에 시작하는 곳은 일단은 가게 되니깐!
    dfs(start)  # start에서부터 갈 수 있는 모든 곳으로 전부 가보게 된다.
    print("#{} {}".format(tc, visited[end]))  # <- 갔던 점인가?




