# subtree


#N을 루트로 갖는 서브트르의 개수 = N을 시작으로 탐색을 진행하여 발견한 node의 개수
#일반적인 그래프 풀듯이 입력을 받는다.





# T = int(input())
#
#
#
# def dfs(now):
#     global ans
#     ans += 1
#
#     #현재 now 노드에 있음
#
#     for next in graph[now]:
#         dfs(next)
#
#     #함수가 끝까지 내려갔다가 반환되는 것도 알아야 해! 자꾸!
#
#
#
#
# for tc in range(1, T+1):
#
#     #노드번호는 1번 부터 존재한다.
#     #E는 간선의 개수
#     #노드 = 간선 + 1
#     #N은 start가 되는 노드
#
#     E, N = map(int, input().split())
#     data = list(map(int, input().split())) #일단 필요한 데이터들을 입력받고!
#     graph = [[] for _ in range(E + 2)] # 왜 E + 2 인거지?! 0을 사용하지 않음! 노드 번호는 1번 부터 시작
#     # 필요한 노드의 개수 만큼 리스트 만들기
#
#     #입력받은 데이터들을 부모 자식의 형태로 그래프화
#     for i in range(E):
#         par = data[i*2]
#         chi = data[i*2 + 1]
#         graph[par].append(chi)
#
#     # print(graph)
#
#     ans = 0
#     dfs(N)
#     print(f"#{tc} {ans}")


####################################################


#백준 5639 이진 검색 트리

#교수님 풀이

# import sys
#
# sys.setrecursionlimit(100000)
#
# data = list(map(int, sys.stdin.read().split()))
#
#
#
# def dfs(s, e):
#     if s > e:
#         return
#
#     now = data[s]
#     mid = e
#     while now < data[mid]:
#         mid -= 1
#
#     dfs(s+1, mid)
#     dfs(mid+1, e)
#
#     print(now)
#
#
# dfs(0, len(data) - 1)
#이때의 미드 값!
# e = 5
# now = 4
#
# data = [2,3,4,6,7,8]
# mid = e  # 구간이 나뉘는 지점
# while now < data[mid]:
#     mid -= 1
#
# print(mid)  #2가 출력


########################

#노드의 합


#교수님 풀이가 뭔가 더 쌈박!!



# T = int(input())
# for tc in range(1, T+1):
#
#     N, M, L = map(int, input().split())
#     node = [0] * (N + 1) #N번까지 있도록,,! 1차원 배열 구성 0번을 사용하지 않음!
#
#     for i in range(M):
#         num, value = map(int, input().split())
#         while num != 0:
#             node[num] += value
#             num // 2 #조상으로 가보자아!
#
#     print(f"#{tc} {node[L]}")


#DFS 반환 풀이!


# def postorder(now):
#     global N
#
#     if now > N:
#         return 0
#
#     if node[now] != 0:
#         return node[now]
#
#     left = postorder(now * 2)
#     right = postorder(now * 2 + 1)
#     node[now] = left + right
#
#     return node[now]
#
#
#
#
#
#
# T = int(input())
# for tc in range(T):
#     N, M, L = map(int, input().split())
#     node = [0] * (N + 1) # N번까지 있도록 1차원 배열 구성
#     for i in range(M):
#         num, value = map(int, input().split())
#         node[num] = value # leaf node setting
#     postorder(1) # 1번 node부터 시작해서 아래로 계산해와라!
#     print(f"#{tc + 1} {node[L]}")


################################

## 이진힙


#힙큐 사용 풀이

#
# import heapq
#
#
# T = int(input())
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     data = list(map(int, input().split()))
#
#
#     node = [] #힙큐를 사용하기 위해서! 빈 리스트를 만든다!
#
#     for i in data:
#         heapq.heappush(node, i)
#
#     ans = 0
#     now = N // 2 #마지막 node의 부모
#
#     while now != 0:
#         ans += node[now - 1] #여기서 이렇게 하는건 0을 생각하고!
#         now // 2 #부모 따라가자!
#



#직접 완전 이진 트리 구현

def insert(value):
    node.append(value)
    pos = len(node) - 1 #맨뒤에 추가된 녀석
    while pos != 0 and node[pos // 2] > node[pos]: #올바른위치가 될때까지! 부모가 더 작은!
        node[pos//2],node[pos] = node[pos], node[pos//2]
        pos //= 2 #부모 위치로 바뀌엇다고 갱신!


T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    node = [0] # 완전 2진트리 N + 1
    for i in data:
        insert(i)
    ans = 0
    now = (len(node) - 1) // 2
    while now != 0:
        ans += node[now]
        now //= 2
    print(ans)


#이진 탐색


# def inorder(now):
#     if now >= len(graph):
#         return
#
#     global cnt
#     inorder(now * 2) #왼쪽
#
#     graph[now] = cnt #프린트 대신에 값을 넣는다고 생각!
#     cnt += 1
#
#     inorder(now * 2 + 1)
#
#
#
# T = int(input())
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     graph = [0] * (N + 1)
#     cnt = 1
#     inorder(1)
#     print(f"#{tc} {graph[1]} {graph[N // 2]}")