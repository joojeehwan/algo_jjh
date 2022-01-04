

def find(x):

    if x == parents[x]:
        return x

    px = find(parents[x])
    parents[x] = px

    return px




def union(x, y):

    px = find(x)
    py = find(y)

    if px < py:
        parents[py] = px

    else:
        parents[px] = py


v, e = map(int, input().split())
parents = [i for i in range( v + 1)]

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    #사이클이 발생한 경우 종료!
    
    if find(a) == find(b):
        cycle = True
        break
    #사이클이 발생하지 않았다면 합집합 수행
    else:
        union(a, b)
    
if cycle:
    print("사이클이 발생")

else:
    print("사이클이 발생x")






