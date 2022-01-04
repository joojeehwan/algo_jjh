

'''


파리 퇴치

이건 다시 풀어보기로 했자나!

4중 포문을 이용해서 4개의 칸씩 확인 하면서 검색!

'''


T = int(input())

for tc in range(1, T+1):


    N, M = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for row in range(N-M+1):
        for col in range(N-M+1):
            temp_sum = 0
            for i in range(row, row + M):
                for j in range(col, col + M):
                    temp_sum +=  MAP[i][j]
            total = max(total, temp_sum)

    print(f"#{tc} {total}")






