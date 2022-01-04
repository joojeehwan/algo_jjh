'''

이진탐색이라고 되어 있지만 이진탐색 트리를 몰라도 풀이가 가능하다



중위순회

1. 제일 왼쪽까지 이동
2. 숫자를 배치
3. 오른쪽으로 이동



'''


# D2 5176 이진탐색

def makeTree(n):
    global count
    # 배열이니까 배열크기 넘어가지 않도록
    if n <= N: # 이게 없으면 에러!
        # 왼쪽노드는 현재 인덱스 * 2
        makeTree(n * 2)
        # 더이상 못가면 값넣기
        tree[n] = count
        # 값 넣었으면 증가시키기
        count += 1
        # 우측 노드는 현재 인덱스 *2 + 1
        makeTree(n * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for i in range(N + 1)] #0번 노드는 사용하지 않으니!
    count = 1
    makeTree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))



#교수님 풀이가 좀 더 직관적!



T = int(input())

def inorder(now):
    if now >= len(graph):
        return
    global cnt
    inorder(now * 2)
    # 처리
    graph[now] = cnt # <- 1~N
    cnt += 1
    inorder(now * 2 + 1)

for tc in range(T):
    N = int(input())
    graph = [0] * (N + 1)
    # 0번은 사용하지 X <- 0에 아무리 곱해도 0 오오,,이거를 알았구만,,!!
    cnt = 1
    inorder(1)
    print(f"#{tc + 1} {graph[1]} {graph[ N//2 ]}")




###########

'''


<이진 탐색 트리(BST)> 

- 현재 노드 기준 왼쪽은 나보다 작음, 오른쪽은 나보다 큼(로그N) 

한쪽으로만 계속 가는 최악의 경우가 있음,, 이렇게 되면 탐색의 시간을 줄이기 위해서 하는건데! 의미가 없어지게 됨!(N) 
이것을 이진 탐색트리로 바꾸는 거 있는 데 AVL트리(나 배웠던거!)



'''