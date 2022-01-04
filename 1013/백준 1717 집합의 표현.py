



# 집합의 표현
import sys

def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px

n, m = map(int, sys.stdin.readline().split())

parents = [i for i in range(n + 1)] # make-set

for _ in range(m):
    order, a, b = map(int, sys.stdin.readline().split())
    if order == 0:
        Union(a, b)
    else:
        if Find(a) == Find(b):
            print("YES")
        else:
            print("NO")