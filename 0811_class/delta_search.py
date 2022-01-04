import sys

sys.stdin = open("delta_search_input.txt")


T = 10
for tc in range(1, T + 1):

    N = int(input())

    lili = [list(map(int, input().split())) for _ in range(N)] # 파이썬의 경우 한 줄씩 입력받아서
    #NxM의 2차원 배열을 받아도 N만 사용해도 된다.

    #print(lili)

    def my_abs(n1, n2):
        if n1 - n2 >= 0:
            return n1 - n2
        else:
            return -(n1 - n2)


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    sum = 0
    for i in range(len(lili)):
        for j in range(len(lili[i])):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N: # 범위를 한정 짖는 것! 벽쪽에 붙어 있는 애들!
                #범위를 넘어서는 경우(문제가 생기는 경우)라 생각해도 좋다! continue사용해서!
                #-> 이거에 좋은점! "인전합 좌표값이 0인 경우 계산하지 않는다" 요론거 풀때!
                # 문제가 되는 것을 한줄씩 추가! 디버깅 할때 좋아!
                # 문제 사황인걸을 사용! 
                    sum += my_abs(lili[ni][nj],lili[i][j])

    print(f"#{tc} {sum}")

T = 10
for tc in range(T):
    N = int(input())
    num = []
    """
    for i in range(N):
        num += [list(map(int, input().split()))]
        # num.append(list(map(int, input().split())))
    """
    num = [list(map(int, input().split())) for _ in range(N)]

    sum = 0
    for row in range(N):
        for col in range(N):
            num[row][col]
            #     상,하,좌,우
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                """
                if nr < 0 or nc < 0 or nr >= N or nc >= N :
                    continue
                """
                # 우리가 원하는 범위 내에 있는가?

                # nr, nc : 다음 좌표(인접한 좌표)
                diff = num[row][col] - num[nr][nc]
                if (diff < 0):  # 절대값
                    diff *= -1
                sum += diff
    print("#{} {}".format(tc + 1, sum))

    """
    제출 정답 runtime error <- 자료형(type), index 90%

    list 크기 부족
    index 계산 <- 범위 고려
    """



