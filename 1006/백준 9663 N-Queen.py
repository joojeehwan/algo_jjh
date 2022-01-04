'''


백트래킹을 해보자!


'''


# N Queen
def dfs(now):
    # now번째 줄에 말을 배치한다.
    if now >= N:
        # 맨 끝줄까지 말을 배치했다.
        # 가지치기를 모두 통과하여 '정상적인'상태이다.
        global ans
        ans += 1

    for col in range(N):
        if check_col[col]:  # 이 열은 앞에서 사용 중이다.
            continue  # 가지치기
        if check_ru_ld[now + col]:  # 이 대각선은 앞에서 사용 중이다.
            continue  # 가지치기
        if check_lu_rd[now - col]:  # 이 대각선은 앞에서 사용 중이다.
            continue  # 가지치기

        check_col[col] = True
        check_ru_ld[now + col] = True  # 오른쪽위->왼쪽아래 대각선은 row+col으로 계산하여 번호를 매겨줄 수 있다.
        check_lu_rd[now - col] = True  # 왼쪽위->오른쪽아래 대각선은 row-col으로 계산하여 번호를 매겨줄 수 있다.
        MAP[now][col] = 1
        dfs(now + 1)
        # 다음줄로 넘어가라
        MAP[now][col] = 0
        # col위치에 두는 방법은 다 해봤으니 기록을 삭제
        check_col[col] = False  # 기록 복구
        check_ru_ld[now + col] = False
        check_lu_rd[now - col] = False


N = int(input())
check_col = [False] * N  # 어떤 열을 사용했는가?
check_ru_ld = [False] * (2 * N + 1)  # 어떤 대각선(오른쪽위 -> 왼쪽아래)을 사용했는가?
#대각선의 갯수가 왜 (2*n+1)인지 몰겠씁니다 ㅠㅠ 왜죠???
#이거 교수님 풀이입니다!!
check_lu_rd = [False] * (2 * N + 1)  # 어떤 대각선(왼쪽위 -> 오른쪽아래)을 사용했는가?
ans = 0
MAP = [[0] * (N) for _ in range(N)]
dfs(0)