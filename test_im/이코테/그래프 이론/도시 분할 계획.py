

def find_parent(parent, x):
    
    # 루트 노드가 아니라면 , 루트 노드를 찾을 때 까지 재귀적으로 호출

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


#두 원소가 속한 집합을 합치기

def union(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b



v, e = map(int, input().split())
parent = [0] * (v + 1) #부모 테이블 초기화

edges = []
result = 0

de = 1

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화

for i in range( 1, v+1):
    parent[i] = i


#모든 간선에 대한 정보 받기

for _ in range(e):
    a, b, cost = map(int, input().split())

    edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에서 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:

    cost, a, b = edge
    #사이클이 발생 x 경우에만!

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost
        last = cost

print(result - last)