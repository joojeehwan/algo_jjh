''''


p.8

완전 그래프 에서

간선들의 수

(5 * (4)) / 2 => /2 를 하는 건 중복을 제거! 




그래프의 표현 2가지

노드의 개수가 1000 이하며 인접행렬을 해도 돼! 

1. 인접 행렬 -> n*n 행렬 / 이차원 리스트 활용

방향이 있는 경우 없는 경우의 모습이 다름!





2. 인접 리스트 -> 이코테 방식


'''


'''
"이러한 입력이 있다고 가정"
마지막정점번호, 간선수
6 8
0 1 0 2 0 5 0 6 4 3 5 3 5 4 6 4

'''



#1.인접행렬 부분

V, E = map(int, input().split())
edge = list(map(int, input().split()))

adjM = [[0] * (V+1) for _ in range(V + 1)]
for i in range(E): #간선의 수만큼!
    n1, n2 = edge[2*i], edge[2*i + 1]
    adjM[n1][n2] = 1 #유향그래프이면(방향성o)이면 여기서 그냥 끝
    adjM[n2][n1] = 1 #무향 그래프이면 여기까지 적어야 해!




adjL = [[] for _ in range(V + 1)]

for i in range(E): #간선의 수만큼!
    n1, n2 = edge[2*i], edge[2*i + 1]
    adjL[n1].append(n2)
    adjL[n2].append(n1) #무향 그래프인 경우! 

