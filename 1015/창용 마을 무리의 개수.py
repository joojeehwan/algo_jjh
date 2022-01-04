'''

유니온 파인트 문제 같이 보이는데,,!

'''




#경로 압축 버젼
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    answer = set()

    for i in parent:
        answer.add(find_parent(parent,i))

    print(f"#{tc} {len(answer) - 1}")


#rank 사용 기법


