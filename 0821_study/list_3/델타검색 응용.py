import sys

sys.stdin = open("3in.txt")


T = 10

for tc in range(1, T+1):

    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for row in range(N): #row자체도 인덱스임! 값이 아님!

        for col in range(N): #col로 마찬가지! 값이 아니라 인덱스임!
            dr = [-1, -2, -2, -1, 1, 2, 2, 1]
            dc = [-2, -1, 1, 2, -2, -1, 1, 2]
            sum = 0
            for i in range(8):

                next_row = row + dr[i]
                next_col = col + dc[i]

                if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                    continue

                diff = lst[row][col] - lst[next_row][next_col]
                if (diff < 0):  # 절대값
                    diff *= -1
                total += diff



    print("#{} {}".format(tc, total))




