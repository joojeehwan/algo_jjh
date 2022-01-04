'''


유니온 파인드 문제구나,,!!



하나의 그룹엔 하나의 조상만이!!

그룹의 개수를 알려면! 조상의 개수를 세어도 된다'
그룹스 사용하는 풀이!



새로운 방법?! => 조상에게 몰어 넣는다! 방2
=> 합쳐지는 유니온에서 커스텀!!

'''


def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for t in range(int(input())):

    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]

    votes = list(map(int, input().split()))

    for i in range(0, M * 2, 2):
        union_parent(votes[i], votes[i + 1])

    answer = set()
    for i in parent:
        answer.add(get_parent(i))

    print('#{} {}'.format(t + 1, len(answer) - 1))






# 그룹 나누기
def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    if px == py:
        return
    parents[py] = px
    global group_cnt
    group_cnt -= 1

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    parents = [i for i in range(n + 1)]
    group = [1] * (n + 1) # 여기에 그룹이 있다.
    group_cnt = n # 총 그룹수
    for i in range(0, len(data), 2):
        Union(data[i], data[i + 1])
    """
    cnt = 0
    for i in range(1, n + 1):
        if i == parents[i]:
            cnt += 1
    """
    print(f"#{tc + 1} {group_cnt}")