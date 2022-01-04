'''



큐 구현


1, frontm rear (index)

2. append, pop

pop(-1) : 스택

pop(0) : 큐,,, 라고 전통적으로 사용!


3. deque



'''


def ADD(value):
    global end
    q[end] = value
    end += 1
    end %= len(q)


def POP():
    global front
    global end
    if front == end:  # 비어있으면 못 꺼냄
        return "error"
    temp = q[front]
    front += 1
    front %= len(q)
    return temp


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split())) + [0]
    # queue의 크기는 항상 최대 넣을 데이터보다 1개 이상 더 커야합니다.
    # 꽉차있는 것과 비어있는 것을 구분하기 위해

    front = 0
    end = len(q) - 1

    for _ in range(M):
        temp = POP()
        ADD(temp)
    print("#{} {}".format(tc + 1, POP()))





