


#순열! 해봐라

#1 ~ N 까지의 순열!


def dfs(n, level):


    if n == level:

        print(*ans)

    else:
        for i in range(n): #이렇게 해야 갓다가 다시 들어가고 하자나! N이 주어졌을 때, 1부터 N까지의 수로 이루어진,,! 그 부분
            if visited[i] == 0:
                visited[i] = 1
                ans[level] = lst[i] #이거 그냥 i 해도 되는 구나!
                dfs(n, level + 1)
                visited[i] = 0


N = int(input())

lst = [i for i in range(1,N+1)]
ans = [0] * N
visited = [0] * N

dfs(N,0)


def dfs(k):

    if k == N:
        for i in range(N):
            print(ans[i], end = " ")
        print("")
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            ans[k] = i
            dfs(k+1)
            visited[i] = 0 # 다른 곳에서 사용할 수 있게 넘겨줘야 한다


# 아 이걸 함수로 넘길 수가 없겟구나,,,!!

N = int(input())
ans = [0] * (N)
visited = [0] * (N + 1)

dfs(0)


#겨수님 풀이


#모든 순열
import sys

N = int(sys.stdin.readline())
arr = [-1] * N
check = [0] * (N + 1)
def dfs(k):
    # 이번에 k번째 수를 고르겠다.
    if k == N:
        for i in range(N):
            print(arr[i], end = " ")
        print("")
        return
    for i in range(1, N + 1):
        if check[i] == 1: continue # 이미 골랐던 수
        arr[k] = i
        check[i] = 1
        dfs(k + 1)
        check[i] = 0

dfs(0)





