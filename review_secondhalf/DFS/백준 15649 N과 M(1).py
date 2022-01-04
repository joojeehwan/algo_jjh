'''


순열 구하는 거구나,,!


'''


def dfs(level):

    #레벨이 내가 원하는 갯수 만큼 뽑았다.
    if level == M: 
        for i in range(M): #그 M개의 갯수 만큼
            print(arr[i], end = " ")
        print("")
        return

    for i in range(1, N+1): #1 ~ N+1 의 범위에서! 
        if visited[i] == 0: #방문하지 않은 곳만!

            visited[i] = 1 #기록용
            arr[level] = i #이건 정말 값이 들어가는!
            dfs(level + 1)
            visited[i] = 0

N, M  = map(int, input().split())

arr = [-1] * N

visited = [0] * (N + 1)

dfs(0)




