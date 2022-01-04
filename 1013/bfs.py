from collections import deque

# BFS
def bfs(graph, start, visited):
  # 큐 구현을 위해 deque라이브러리 사용
  queue = deque([start])

  # 탐색 시작 노드를 방문 처리
  visited[start] = True



  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 꺼내서 출력
    n = queue.popleft()
    print(n, end='')
    #어떤 활동이 여기서 이루어짐!

    # 꺼낸 원소와 인접노드 확인
    for i in graph[n]:
      # 아직 방문하지 않은 노드라면
      if not visited[i]:
        queue.append(i)
        visited[i]=True

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

# 방문 정보
visited = [False]*(8+1) #(총 노드의 갯수)+인덱스 0
# bfs호출
bfs(graph, 1, visited)


'''
최단,, 에 어울린다. 


'''


class Queue():
  def __init__(self):
    self.queue = []


def enqueue(self, data):
  self.queue.append(data)


def dequeue(self):
  dequeue_object = None
  if self.isEmpty():
    print("Queue is Empty")
  else:
    dequeue_object = self.queue[0]
    self.queue = self.queue[1:]

  return dequeue_object


def peek(self):
  peek_object = None

  if self.isEmpty():
    print("Queue is Empty")
  else:
    peek_object = self.queue[0]

  return peek_object


def isEmpty(self):
  is_empty = False
  if len(self.queue) == 0:
    is_empty = True
  return is_empty

