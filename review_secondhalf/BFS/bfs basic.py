from collections import deque




def bfs():

    start = 1 #1번 노드 부터

    queue = deque([start])

  # 탐색 시작 노드를 방문처리
    visited[start] = True

    while queue:

      start = queue.popleft()
      #어떤 활동이 여기서 일어남!
      print(start, end = " ")

      #꺼낸 원소와 인접 노드 확인
      for i in graph[start]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True

# 2차원 맵정보 입력받기
graph=[
  [], # 0번 노드 비우기
  [2,3,8], #1번 노드와 연결된 2,3,8노드
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

N = len(graph)

visited = [False] * (N + 1)

bfs()


