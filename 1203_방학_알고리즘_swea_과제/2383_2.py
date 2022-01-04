def on_stair(time_list, stair_num):
    time = 0
    wait = 0
    now = []
    while time_list or wait or now:
        while wait:
            if len(now) >= 3:
                break
            now.append(stair_num[2])
            wait -= 1

        for i in range(len(time_list) - 1, -1, -1):
            time_list[i] -= 1
            if time_list[i] <= 0:
                time_list.pop(i)
                wait += 1

        for i in range(len(now) - 1, -1, -1):
            now[i] -= 1
            if now[i] <= 0:
                now.pop(i)

        time += 1
    return time


def move(idx):
    global result
    if idx == M:
        stair1, stair2 = [], []
        for i in range(M):
            if choices[i] == 1:
                stair1.append(dist_stair1[i])
            else:
                stair2.append(dist_stair2[i])

        result = min(result, max(on_stair(stair1, stairs[0]), on_stair(stair2, stairs[1])) + 1)
        return

    choices[idx] = 1
    move(idx + 1)
    choices[idx] = 2
    move(idx + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = list(list(map(int, input().split())) for _ in range(N))

    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] >= 2:
                stairs.append((i, j, board[i][j]))

    M = len(people)
    dist_stair1 = [0] * M
    dist_stair2 = [0] * M
    for i in range(M):
        px, py = people[i]
        dist_stair1[i] = abs(stairs[0][0] - px) + abs(stairs[0][1] - py)
        dist_stair2[i] = abs(stairs[1][0] - px) + abs(stairs[1][1] - py)

    result = 2134567890
    choices = [0] * M
    move(0)

    print(f'#{tc} {result}')