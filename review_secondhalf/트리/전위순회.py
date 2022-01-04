
'''

swea 이진 트리 전위 순회

'''

def pre_order(now):
    print(now, end=' ')
    if tree[now * 2] != 0:
        pre_order(tree[now * 2])
    if tree[now * 2 + 1] != 0:
        pre_order(tree[now * 2 + 1])


T = int(input())

for tc in range(T):
    V = int(input())
    E = V - 1
    tree = [0] * ((V + 1) * 2)
    for i in range(E):
        parent, child = map(int, input().split())
        if tree[parent * 2] == 0:
            tree[parent * 2] = child
        else:
            tree[parent * 2 + 1] = child

    print('#{}'.format(tc + 1), end=' ')
    pre_order(1)
    print()