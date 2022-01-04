
def dfs(idx):
    global count
    # 순회를 할때마다 카운트
    count += 1
    # 자식노드를 순회한다.
    for i in Tree[idx]:
        dfs(i)

for t in range(int(input())):
    # 노드의 개수와 출력할 노드
    E, N = map(int, input().split())
    temp_list = input().split()
    # 노드의 개수만큼 리스트 만들기
    Tree = [[] for _ in range(E+2)]
    for idx, i in enumerate(range(0, E*2, 2)):
        a = int(temp_list[i])
        b = int(temp_list[i + 1])
        # 부모노드를 찾아서 자식노드 표현
        Tree[a].append(b)
    count = 0
    dfs(N)
    # 결과값 출력
    print('#{} {}'.format(t + 1, count))

####

# # 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree D2
# 구현3
def inorder(node):
    global cnt
    if node == 0:
        return
    # 전위
    cnt += 1
    inorder(left[node])
    # 중위
    inorder(right[node])
    # 후위


for test_case in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    # 구현1
    left = [0] * (E + 2)  # 첫번째 자식
    right = [0] * (E + 2)  # 두번째 자식
    # 구현2
    for i in range(0, len(arr), 2): #arr의 값이 한줄로 들어오니깐!
        papa, baby = arr[i], arr[i + 1]  # 부모 - 자식
        if left[papa]:  # 0이 아니고 첫번째에 값이 있으면
            right[papa] = baby  # 두번째에 보관
        else:  # 0이면
            left[papa] = baby  # 첫번째에 보관

    cnt = 0
    inorder(N)
    print('#{} {}'.format(test_case, cnt))
    
    
    
## 교수님 풀이! 

## N을 루트로 갖는 서브트리의 node개수 = N을 시작으로 탐색을 진행하여 발견한 node의 개수

##dfs로 구현

T = int(input())

def dfs(now):
    global ans
    ans += 1
    # 현재 now node에 있음

    for next in graph[now]:
        dfs(next)
    #for문이 끝나면 자연스레 return을 하니깐!

for tc in range(T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [ [] for _ in range(E + 2) ]
    for i in range(E):
        parents = data[i * 2]
        child = data[i * 2 + 1]
        graph[parents].append(child)
    # N을 root로 갖는 subtree의 node개수
    # N을 시작으로 탐색을 진행하여 발견한 node의 개수
    # bfs, dfs <-
    ans = 0
    dfs(N)
    print(f"#{tc + 1} {ans}")