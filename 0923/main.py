'''

트리

- 순환되지 않는 그래프

- A라는 점과 B라는 점 사이의 경로가 유일한 그래프!

노드개수 : N
간선개수 : N - 1


- 트리의 구조로 데이터를 저장하는 방법은 4가지

1. 그래프 - 인접행렬 (arr[from][to]의 구조, 이차원 배열) / 메모리 소비가 크다

2. 그래프 - 인접리스트(arr[from].append(to)의 구조)

------------------------------------------------기본 그래프!

k진 트리 : 자식이 k개 까지만 있는 트리

3. 트리 - 2차원 배열로 저장

4. 트리 - 1차원 배열로 저장(2가지)
(1) 부모를 저장 (1차원 배열에 해당 노드의 부모 노드의 번호를 배열로 저장)

Union-Find 알고리즘(a형) 에서 사용이 됨,,(같은 그룹인지를 최종 조상만 보고 확인)

(2) 자식 번호를 계산
일반적인 방법은 아님,,특별한 상황(완전 k진 트리)에서 사용

현재 노드 : n
왼쪽 자식 : n * k
오른쪽 자식 : n * k + a(단, 0 <= a < k)
부모노드 : n // k

힙, 세그먼트 트리(b형), 인덱스 트리(b형)


------------------------------------

- <트리의 존재 이유?!>

탐색할려고!!  <- 연결정보를 활용하여 다른 node찾기

탐색의 2가지 방법 -> dfs(재귀, 스택), bfs(큐)

ex) 2진 트리

def dfs(now):
    기저 조건 : 끝인지 확인

    #now 현재 노드 번호

    요기서 처리(전위순회)

    dfs(now의 왼쪽 자식)

    요기서 처리(중위순회)

    dfs(now의 오른쪽 자식)

    요기서 처리 (후위순회)


'''

