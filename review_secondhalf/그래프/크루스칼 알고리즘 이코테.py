'''

크루 스칼 알고리즘 이코테


7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25



'''


def find_parent(parent, x):
    
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출

    if parent[x] == x:
        return x

    px = find_parent(parent,parent[x])
    parent[x] = px

    return px


def union(x, y):
    a = find_parent(parent,x)
    b = find_parent(parent,y)

    #더 작은 수의 값을 조상으로,,!
    if a < b:
        parent[b] = a

    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [i for i in range(v + 1)]


edges = []
result = 0

#단반향
for _ in range(e):
    frm, to, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정

    edges.append((cost, frm, to))


edges.sort()

for edge in edges:
    cost, a, b = edge # 오 이렇게 가능!

    # 사이클이 발생하지 않을 경우에만 집합에 포함

    if find_parent(parent,a) != find_parent(parent,b):
        union(a, b)
        result += cost


print(result)



