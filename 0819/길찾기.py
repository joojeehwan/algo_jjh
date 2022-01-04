



'''


입력 받는 2가지 case

1. 홀짝

i % 2 == 0

2.(0, ren(load),2)

3. 2 * ?

=> 2 * i
=> 2 * i + 1

어떻게 저장할 것인가!?




'''



import sys

sys.stdin = open("길찾기_input.txt")

for _ in range(10):

    tc, N = map(int, input().split())
    road = list(map(int,input().split()))
    # #1 홀짝
    # #2 2step
    # #3 2*?
    #
    for i in range(N):
        st = road[2*i]
        ed = road[2*i+1]



    #어떻게 저장할 것인가? 1.ch1, ch2
    ch1 = [0] * 100
    ch2 = [0] * 100
     #두갈래의 길이니깐! 시작점과 도착점으로 이루어져 있으니,,,!!
    for i in range(N):
        if ch1[road[2*i]] == 0:
            ch1[road[2*i]] = road[2*i + 1]
        else:
            ch2[road[2*i]] = road[2*i + 1]


    # 2. 인접행렬
    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1


    # 3. 인접리스트

    adj_lst = [[] for _ in range(100)]

    for i in range(N):
        adj_lst[road[2*i]].append(road[2*i+1])


    visited = [0] * 100
    ans = 0
    stack = [0]

    while stack :
        curr = stack.pop()

        if curr == 99:
            ans = 1
            break

        #방문하지 않았으면

        #방문을 했으면 건너가~

        if visited[curr]: continue

        visited[curr] = 1

        for w in adj_lst[curr]:
            if not visited[w]:
                stack.append(w)

    print("#{} {}".format(tc, ans))


#######################################################

def DFS_2(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = 1

    for w in range(100):
        if not visited[w] and adj_arr[v][w]:
            DFS_2(w)

for _ in range(10):

    tc, N = map(int, input().split())
    road = list(map(int,input().split()))

    # 2. 인접행렬
    adj_arr = [[0] * 100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1


    visited = [0] * 100
    ans  = 0
    DFS_2(0)

    print("#{} {}".format(tc, ans))








#
# def dfs(now): # now : 나의 현재 위치
#     # 2. 기저조건(옵션)
#     # 1. now에서 갈 수 있는 next찾기
#     for to in range(V + 1):
#         if adj[now][to] == 1 and visited[to] == 0:
#             # adj[now][to] == 1 : now에서 to로 갈 수 있는 길이 있는가?
#             visited[to] = 1 # to에 간다!라고 기록
#             dfs(to) # 길이 있으면 가라!
#
#     # 3. 문제가 생길 수 있는 경우
#
# T = int(input())
# for tc in range(T):
#     V, E = map(int, input().split())
#     adj = [[0] * (V + 1) for _ in range(V + 1)]
#     visited = [0] * (V + 1) # 들렸던 점인가?
#     # adj[from][to]
#     for i in range(E):
#         f, t = map(int, input().split())
#         # f : 어디에서
#         # t : 어디로
#         adj[f][t] = 1
#     start, end = map(int, input().split())
#     visited[start] = 1
#     dfs(start) # start에서부터 갈 수 있는 모든 곳으로 전부 가보게 된다.
#     print("#{} {}".format(tc + 1, visited[end])) # <- 갔던 점인가?
#
# V, E = map(int, input().split())
# adj = [[0] * (V+1) for _ in range(V+1)]
#
# for i in range(E):
#     f, t = map(int, input().split())
#     adj[f][t] = 1
#
# start, end = map(int, input().split())
# visited[start] = 1
# dfs(start)