'''



완전이진 트리 기반으로 힙을 만듬!!


추가
1. 완전 이진 트리에 맞게 노드 1개 추가
2. 이번엔 추가한 노드가 알맞는 위치로 가도록 부모와 스왑
시간 복잡도 : 로그N

삭제
1. 맨 끝 노드와 루트 노드 스왑
2. 루트 노드에 있는 값을 알맞는 위치가 되도록 자식들과 스왑!
시간 복잡도: 로그 N


힙Q를 사용해서,,,!!



'''

# import heapq
#
# data = []
# # heap으로 사용할 list생성
# heapq.heappush(data, 1)
# heapq.heappush(data, 3)
# heapq.heappush(data, 4)
# heapq.heappush(data, 2)
# heapq.heappush(data, 7)
# heapq.heappush(data, 6)
# print(data)
#
# while data:
#     print(data[0])
#     heapq.heappop(data) # 우선순위가 가장 높은 data 삭제



import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = []
    data = list(map(int, input().split()))
    for number in data:
        heapq.heappush(numbers, number)
    numbers.insert(0,0) #0번 인덱스를 사용하지 않기 위해서!
    print(numbers)

    ans = 0
    while N > 0:
        N //= 2 #부모 노드를 찾아가는 것,,!
        ans += numbers[N]

    print(f"#{tc} {ans}")



##교수님 풀이 힙큐 사용


import heapq

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    node = []

    for i in data:
        heapq.heappush(node, i)
    # node라는 곳에 heap구조로 data 추가
    ans = 0
    now = N // 2 # 마지막 node의 부모(node번호)
    while now != 0:
        ans += node[now - 1]
        now //= 2

    print(f"#{tc + 1} {ans}")



## 직접 완전 이진 트리 구현


import heapq

def insert(value): # heap구조로 node에 value를 추가
    # 1. 일단 맨 뒤에 data(value)를 추가
    node.append(value)
    pos = len(node) - 1 #위치,,! position을 pos로,,!
    # 2. 이번에 추가한 얘가 올바른 위치가 될 때까지 부모랑 swap
    while pos != 0 and node[pos // 2] > node[pos]:
        node[pos//2], node[pos] = node[pos], node[pos//2] # 부모랑 swap
        pos //= 2 # 부모 위치로 이동했다고 갱신

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    node = [0] # 완전 2진트리 N + 1
    for i in data:
        insert(i)
    ans = 0
    now = (len(node) - 1) // 2
    while now != 0:
        ans += node[now]
        now //= 2
    print(ans)




