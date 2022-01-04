'''


요리사,,!



1) 2개씩 경우의수를 확인해야 함! => 어떤 쌍으로 음식을 고를지 선택! nC2 를 해야함! 조합!

dfs로 경우의 수 찾기!

만약에 12면 다른 음식은 34

12 => 34
13 => 24
14 => 23


2) 그 다음에 반복문으로 시너지를 구한다!



조합을 만드는 방법 2가지

1. 비트를 사용해서

2. dfs

'''

def dfs(level, idx, beginwith):

    if level == find_num:
        calc(0)
        return

    else:
        for i in range(beginwith, N):
            food_a[idx] = i
            dfs(level +1, idx + 1, i + 1)
    return

def calc(food2_cnt):

    global res_min
    customer1 = 0
    customer2 = 0

    for num in range(N):
        if num not in food_a:
            food_b[food2_cnt] = num
            food2_cnt += 1

    for i in range(N // 2):
        for j in range(N // 2):
            if i != j:
                customer1 += board[food_a[i]][food_a[j]]
                customer2 += board[food_b[i]][food_b[j]]

    if abs(customer1 - customer2) < res_min:
        res_min = abs(customer1 - customer2)

    return


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    res_min = 20000

    food_a = [0] * (N // 2)
    food_b = [0] * (N // 2)

    find_num = N // 2

    dfs(0,0,0)

    print(f"#{tc} {res_min}")


#####################

# 요리사
def make_path(now = 0, path = []):
    if len(path) == n // 2:
        # A쪽 식재료를 모두 뽑았다.
        path_set.add(tuple(path))
        return
    if now >= n:
        return
    # now : 식재료 번호
    make_path(now + 1, path + [now]) # A쪽에 포함
    make_path(now + 1, path) # B쪽에 포함

def calc():
    ret = 2134567890
    for path in path_set:
        food1 = 0 # A의 맛
        food2 = 0 # B의 맛
        for i in path:
            for j in path:
                food1 += MAP[i][j]
        other_path = [] # B 식재료 조합
        for i in range(n): # 모든 식재료 중
            if not i in path: # path에 없으면
                other_path.append(i)
        for i in other_path:
            for j in other_path:
                food2 += MAP[i][j]
        ret = min(ret, abs(food1 - food2))
    return ret

def proceed():
    global path_set
    path_set = set()
    make_path()
    return calc()

t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc + 1} {proceed()}")



