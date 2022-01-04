'''


트리와 쿼리

정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.


힌트에 답이 있구나

dfs를 하라는 이야기 구나,!

재귀 구조로!

무방향


visted 배열 쓰늬깐,,! 메모리 초과뜨네,,

굳이 할 필요가 없었구나,, 흠흠,,!

'''


'''
def countSubtreeNodes(currentNode) :
    size[currentNode] = 1 // 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
    for Node in currentNode’s child:
        countSubtreeNode(Node)
        size[currentNode] += size[Node]

'''

import sys
sys.setrecursionlimit(10**9)

def dfs(root) :

    sub_tree[root] = 1 #자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.

    # visited[root] = True

    for node in adj_list[root]:

        # if visited[node] == False:  #안가본 곳
        #     dfs(node)
        #     sub_tree[root] += sub_tree[node]

        if sub_tree[node] == 0:  # 안가본 곳
            dfs(node)
            sub_tree[root] += sub_tree[node]

    return

N, R, Q = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
sub_tree = [0] * (N + 1) #인덱스 : 루트 번호 , value : 서브트리의 정점의 갯수를 담을 배열
# visited = [False] * (N + 1) #방문 여부를 담을 리스트!

for _ in range(N - 1):

    frm, to = map(int, sys.stdin.readline().split())
    #무방향 그래프 니깐!
    adj_list[frm].append(to)
    adj_list[to].append(frm)


dfs(R) #루트노드를 설정하고 DFS 실행

for _ in range(Q):

    temp = int(sys.stdin.readline())

    print(sub_tree[temp])




