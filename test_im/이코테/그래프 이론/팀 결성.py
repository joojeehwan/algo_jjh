


def find_parent(parent, x):


    if parent[x] == x:
        return x
    px = find_parent(parent, parent[x])
    parent[x] = px

    return px



def union(x, y):

    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b




n, m = map(int, input().split())

#부모 테이블 초기화
parent = [i for i in range(n + 1)]



for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union(a, b)

    else:
        if find_parent(parent, a)== find_parent(parent, b):
            print("YES")

        else:
            print("NO")