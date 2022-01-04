'''



dfs로 풀어보자,,



이차원 배열의 범위도 설정해줘야 할꺼 같은데? 그래야
'''

#아 교수님 풀이처럼 했어야 했는데,, 이상한 생각을,, 했네,, 썩이는 것을 내가 생각을 못했네,,!!ㄴ

'''
위의 풀이에서 잘못된 점 

dfs 오른쪽으로만 아래족으로만,, 생각,,! 델타 배열 머릿속으로 생각하고 잇었는데 

그 외에는 내 아주 휼륭하였다.

그걸 안 사용! 사진에 다른 풀이도 있으니 그것도 적을 것!


'''



def dfs(row, col, sum):

    global ans

    if row == N-1 and col == N-1:
        ans = min(ans, sum + MAP[row][col])
        return

    dr = [1, 0]
    dc = [0, 1]
    for i in range(2):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if not (0 <= next_row < N and 0 <= next_col < N):
            continue

        dfs(next_row, next_col, sum + MAP[row][col])


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    ans = 24215781878

    MAP = [list(map(int, input().split())) for _ in range(N)]

    dfs(0,0,0)

    print(ans)

###


# 최소 합

# dp를 추가해서 속도를 높일 수 있다.

def dfs(row, col):

    if row == n-1 and col == n-1:
        return MAP[row][col]# 오른쪽 아래(끝)이면 멈춤

    if DP[row][col] != -1:
        return DP[row][col]
    ret = 2134567890
    dr = [1,0]
    dc = [0,1]
    for i in range(2):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if not ( 0 <= next_row < n and 0 <= next_col < n):
            continue # 맵을 벗어나면 무시
        ret = min(ret, dfs(next_row, next_col) + MAP[row][col])
        # row, col에서 n-1,n-1까지 갈 때의 비용
    DP[row][col] = ret
    return ret


t = int(input())
for tc in range(t):
    n = int(input())
    MAP = [ list(map(int, input().split())) for _ in range(n)]
    DP = [[-1] * (n) for _ in range(n)]
    print(dfs(0,0))
    for dp in DP:
        print(dp)