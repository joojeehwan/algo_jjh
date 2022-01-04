''''

n-queen으로 백트래킹은 마무리 하자!


N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
'''

#N_Queen

def dfs(now):

    #now번쨰 줄에 말을 배치한다.

    if now >= N:
        #맨 끝줄까지 말을 배치 했다.
        #가지치기를 모두 통과하여 "정상적인 상태이다"
        global ans
        ans += 1
        return

    for col in range(N):
        if check_col[col]: # 이 열은 앞에서 사용 중이다.
            continue

        if check_ru_ld[now + col]: # 이 대각선은 앞에서 사용 중이다.
            continue

        if check_lu_rd[now - col]: # 이 대각선은 앞에서 사용중이다! 어차피 - 들어가도 행 열마다 같게 동작하니깐 !
            continue

        check_col[col] = True
        check_ru_ld[now + col] = True
        check_lu_rd[now - col] = True

        MAP[now][col] = 1
        dfs(now + 1)
        # 다음 줄로 넘어가라!

        MAP[now][col] = 0
        #col위치에 두는 방법은 다 해봣으니 기록을 삭제

        check_col[col] = False
        check_ru_ld[now + col] = False
        check_lu_rd[now - col] = False



N = int(input())

check_col = [False] * N

check_ru_ld = [False] * (2 * N -1) # 어떤 대각선(오른쪽 위 ->왼쪽 아래)를 사용했는가?

check_lu_rd = [False] * (2 * N - 1)

ans = 0

MAP = [[0] * N for _ in range(N)]

dfs(0)

print(ans)
