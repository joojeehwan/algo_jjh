'''


swea

[S/W 문제해결 기본] 9일차 - 중위순회


'''

T = 10


def in_order(now):
    if now:
        in_order(left[now])
        print(char[now], end='')
        in_order(right[now])


for tc in range(T):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    nodes = [list(input().split()) for _ in range(N)]
    char = [0] * (N + 1)

    for node in nodes:
        char[int(node[0])] = node[1]
        if len(node) == 4:
            left[int(node[0])] = int(node[2])
            right[int(node[0])] = int(node[3])
        elif len(node) == 3:
            left[int(node[0])] = int(node[2])

    print('#{}'.format(tc + 1), end=' ')
    in_order(1)
    print()