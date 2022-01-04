

T = 10




def dfs(row):

    global count

    if row == N :
        count += 1
        return


    for i in range(N):
        if check_col[i] == 1:
            continue

        check_col[i] = 1
        dfs(row+1)
        check_col[i] = 0



for tc in range(1, T+1):

    N = int(input())
    check_col = [0] * N
    count = 0
    dfs(0)

    print("#{} {}".format(tc, count))
