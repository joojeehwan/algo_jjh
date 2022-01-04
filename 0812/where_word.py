
import sys

sys.stdin = open("where_word_input.txt")



#행우선, 열우선으로 각각 이중 포문을 싹돌면서, 연속된 1의 갯수를 세고 그 갯수가 단어의 길이와 맞는지만 체크
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    total = 0

    # 행우선
    for col in range(N):
        count = 0
        for row in range(N):
            if matrix[col][row] == 0: #검은색 부분
                if count == K:
                    total += 1
                count = 0
            else: #흰부분 이니깐 카운트를 세면서 글자 범위와 맞는지 확인!
                count += 1
        if count == K:
            total += 1

    # 열우선
    for row in range(N):
        count = 0
        for col in range(N):
            if matrix[col][row] == 0:
                if count == K:
                    total += 1
                count = 0
            else:
                count += 1
        if count == K:
            total += 1

    print("#{} {}".format(tc, total))

    T = int(input())
    for tc in range(T):
        N, K = map(int, input().split())
        MAP = [list(map(int, input().split())) for _ in range(N)]
        ans = 0
        # 가로
        for row in range(N):
            length = 0
            for col in range(N):
                if MAP[row][col] == 1:
                    length += 1
                    if col + 1 == N or MAP[row][col + 1] == 0:
                        # 뒤에가 벽인가? : 단어의 끝인가
                        if length == K:  # 단어의 길이가 K
                            ans += 1
                else:
                    length = 0

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