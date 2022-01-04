'''

3가지 풀이 다 보자! 

1. 가로 세로 모두 검사 해야함

2. 가로 먼저

2-1 ) cnt 변수를 만들어서 k개 만큼 진행할 수 있는 지 확인

2-2) 로직 => 반복을 돌면서 검은색 부분을 만났는데 그전까지 cnt개수가 k개이면 total를 증가 시키고
            그게 아니라면 cnt를 초기화 시켜서 그 다음 반복을 준비




'''



T = int(input())

for tc in range(1, T+1):

    #가로 세로의 길이 N, 단어의 길이 K
    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]


    #검은색 0 갈수 없음, 흰색 1 갈수 있음

    total = 0

    #가로 검사
    for i in range(len(MAP)):
        cnt = 0

        for j in range(len(MAP[i])):

            if MAP[i][j] == 0: #검은색인 부분에 도달 했을 때:

                if cnt == K: #벽에 닿기 전에 k가 다 적혀있다면
                    total += 1 #글자가 적힌 것이니, total의 값을 증가

                cnt = 0 #cnt 초기화

            else:
                cnt += 1 #흰곳이니 cnt 증가

        if cnt == K: #벽을 만나서 끝이 아니라 맵의 끝까지 갓으니 종료
            total += 1

    #세로 검사
    for i in range(len(MAP)):

        cnt = 0

        for j in range(len(MAP[i])):

            if MAP[j][i] == 0 :

                if cnt == K:
                    total += 1

                cnt = 0

            else:
                cnt += 1

        if cnt == K:
            total += 1

    print(f"#{tc} {total}")



def garo_check(r, c, k):
    # 양옆 체크하기

    #범위안에 있고 왼쪽이 근데 왼쪽에 빈칸이 있으면 그 칸을 다 못채운거자나! 그래서 false 인것!
    if c - 1 >= 0 and MAP[r][c - 1] == 1: return False  # 범위 안쪽이고 MAP[r][c-1] 빈칸이다
    #오른쪽끝이 범위안에 있고, 근데 오른쪽 끝을 한간 못채우면 다 못채운거라 false
    if c + k < N and MAP[r][c + k] == 1: return False
    #적을 범위를 벗어난 것!
    if c + k - 1 >= N: return False

    # [r][c] ~ [r][c+k-1]  총 k 칸 검사하기
    for i in range(k):
        if MAP[r][c + i] == 0:  # 벽이 하나라도 있으면
            return False
    return True


def sero_check(r, c, k):
    if r - 1 >= 0 and MAP[r - 1][c] == 1: return False
    if r + k < N and MAP[r + k][c] == 1: return False
    if r + k - 1 >= N: return False
    # [r][c] ~ [r+k-1][c] 총 k 칸 검사하기
    for i in range(k):
        if MAP[r + i][c] == 0:
            return False
    return True

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for R in range(N):
        for C in range(N):
            if garo_check(R, C, K): cnt += 1
            if sero_check(R, C, K): cnt += 1

    print(f"#{tc} {cnt}")



T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    #가로

    for row in range(N):
        length = 0
        for col in range(N): #이거는 내 풀이와 반대로,,! 적을 수 있는 것 부터 생각!
            if MAP[row][col] == 1: #갈 수 있는 곳!
                length += 1
                if col + 1 == N or MAP[row][col +1] == 0: # 단어의 끝인가? / 뒤에가 벽인가?
                    if length == K:
                        ans += 1
            else:
                length = 0 #벽을 만났으면 길이를 다시 초기화 하고 다음 반복을 해야 하기 때문에!

        # 세로
    for col in range(N):
        length = 0
        for row in range(N):
            if MAP[row][col] == 1:
                length += 1
                if row + 1 == N or MAP[row + 1][col] == 0:
                    if length == K:
                        ans += 1
            else:
                length = 0
    print("#{} {}".format(tc + 1, ans))