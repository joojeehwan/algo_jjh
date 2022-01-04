
T = int(input())

for tc in range(1, T+1):


    N = int(input().rstrip())

    MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]

    new_MAP = [[0] * N*2 for _ in range(N * 2)]

    for i in range(len(new_MAP) // 2):

        for j in range(0, N):
            new_MAP[i][j] = MAP[i][j]

    for i in range(len(new_MAP)//2):

        for j in range(N, 2*N):
            new_MAP[i][j] = MAP[i][2*N -1 - j]

    for i in range(len(new_MAP) // 2, len(new_MAP)):

        for j in range(0, N):

            new_MAP[i][j] = MAP[2*N -1 -i][j]

    for i in range(len(new_MAP) // 2, len(new_MAP)):

        for j in range(N, 2*N):

            new_MAP[i][j] = MAP[2*N-1-j][2*N-1-i]

    print(f"#{tc}")
    for row in new_MAP:
        print(*row)








