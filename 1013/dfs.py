'''

깊이 우선 탐색


가장 마지막에 만났던 갈림길의 정점으로 되돌아가서! 다시 깊이 우선 탐색을 반복해야 하므로!

후입선출 구조의 스택 사용! , 함수 반환(재귀)와 같은 !


dfs와 bfs의 차이가 스택 사용 / 큐 사용은 아님! => 재귀 구조는 어떻게 설명한거데! dfs의!
둘을 설명할떄는 탐색방법을 두고 사용해야해! 



스택

'''


#스택 구현


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()

        return pop_object

    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]

        return top_object

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True

        return is_empty




'''

p.28의 dfs는

경로를 저장 x , 선택하지 않은 나머지 들을 저장한,,! 

'''


def dfs(graph, n, visited):
    # 현재 노드를 방문처리
    visited[n] = True
    print(n, end='')

    # 현재 노드와 인접한 노드를 확인
    for i in graph[n]:
        # 방문하지 않은 노드라면
        if not visited[n]:
            # 재귀호출
            dfs(graph, i, visited)


######## dfs 사용
# 각 노드에 연결된 정보를 2차원 리스트로 표현
graph = [
    [],  # 노드번호가 1부터 시작하기 때문에 인덱스 0은 비워둔다
    [2, 3, 8],  # 1번 노드와 인접한 노드 2,3,8
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보
visited = [False] * (8 + 1)  # 전체 노드갯수 8개+인덱스0
# dfs 호출
dfs(graph, 1, visited)




