def bfs(idx, answer=100):
    global max_value


    #가지 치기
    if answer <= max_value:
        return

    if idx >= N:
        max_value = answer
        return
    for i in range(N):
        if use_check[i]:

            use_check[i] = False
            bfs(idx + 1, answer * (success_list[idx][i]))
            use_check[i] = True


T = int(input())
for t in range(1, T + 1):
    N = int(input())

    success_list = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    use_check = [True for _ in range(N)]
    max_value = 0
    bfs(0)
    print('#{} {:6f}'.format(t, max_value))