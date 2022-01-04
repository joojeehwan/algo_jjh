



T = int(input())

for tc in range(1, T+1):

    N, M, L = map(int, input().split())

    tree = [0] * (N+1)

    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    for i in range(N, L - 1, -1):
        tree[i // 2] += tree[i]

    print("#{} {}".format(tc, tree[L]))


#교수님 풀이,,!!
T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1) # N번까지 있도록 1차원 배열 구성
    for i in range(M):
        num, value = map(int, input().split())
        while num != 0: # node인지 확인
            node[num] += value # leaf node의 value를 넣어줌
            num //= 2
        # 부모로 타고 올라가면서 모든 조상node들에게 value씩 누적
    print(f"#{tc + 1} {node[L]}")
    # 완전 이진 트리



#### DFS 풀이 반환

def postorder(now):
    # 현재 now번째
    global N
    if now > N:
        return 0
    if node[now] != 0:
        return node[now]
        # 계산하거나 알고 있는 값이면 그냥 가져와라(다시 계산하지 말라)
        # Dynamic Programming <- 가면서 계산하기 보다는 뒤에껄 계산해와서 내껄 계산하는 방식
    left = postorder(now * 2) # 왼쪽
    right = postorder(now * 2 + 1) # 오른쪽
    node[now] = left + right
    return node[now]

T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1) # N번까지 있도록 1차원 배열 구성
    for i in range(M):
        num, value = map(int, input().split())
        node[num] = value # leaf node setting
    postorder(1) # 1번 node부터 시작해서 아래로 계산해와라!
    print(f"#{tc + 1} {node[L]}")
    # 완전 이진 트리














