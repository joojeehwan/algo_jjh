

# 배열 최소의 합
# def dfs(row, sum):
# 
#     # row번째까지 고른 수들의 합 : sum
# 
#     global ans
# 
#     if row == n :
#         #둘 수 없는 경우는 가지치기를 했으니 여기까지 오면 가능한 방법이다.
# 
#         ans = min(ans, sum)
#         return
# 
#     for i in range(n):
#         if check_col[i] == 1:
#             continue #기록하기도 전에 이미 기록이 있다!
#             #앞에서 둔적이 있다! 그러면 무시(가지치기)
# 
#         check_col[i] = 1
#         dfs(row+1, sum + data[row][i])
#         #이번에 i번 위치에다가 말을 두는 방법으로 다 해보기
#         #이번에 row번째 줄 i번째 칸의 값을 고른 것이므로 해당 값만큼 sum에 누적
# 
#         check_col[i]  = 0 #i번에 대해선 끝났으니 기록을 삭제
# 
# 
# 
# T = int(input())
# 
# for tc in range(T):
# 
#     n = int(input())
# 
# 
#     #그래서 어디에 두었니?
#     check_col = [0] * n #col[index] -> index: 칸 번호, value : 해당 칸을 사용하고 있는가?
#     ans = 2134567890
# 
# 
#     data = [list(map(int, input().split())) for _ in range(n)]
#     dfs(0,0)
#     print("#{} {}".format(tc + 1, ans))


#토너먼트 카드 게임


# def dfs(start, end):
# 
#     if start == end :
#         return start
#         #기저 조건(최대한 쪼개서 1개만 남았는가?)
# 
#     mid = (start + end) // 2
#     left = dfs(start, mid)
#     right = dfs(mid + 1, end)
# 
#     if data[left] < data[right]:
#         if data[left] == 1 and data[right] == 3:
#             return left
#         else:
#             return right
# 
#     elif data[left] > data[right]:
#         if data[left] == 3 and data[right] == 1:
#             return right
#         else:
#             return left
# 
# 
# T = int(input())
# 
# 
# for tc in range(1, T+1):
#     size = int(input())
#     data = list(map(int, input().split()))
#     winner = dfs(0, size-1)
#     print("#{} {}".format(tc + 1, winner+1))
#     
#     


#미로


# import sys
#
#
# sys.stdin = open("미로_input.txt")
#
#
#
# def dfs(row, col):
#     #반환값 <- 도착지를 발견하면 1, 아니면 0
#
#
#
#     #상 하 좌 우
#     dr = [-1,1,0, 0]
#     dc = [0,0,-1,1]
#
#     for i in range(4):
#         global ans
#         if MAP[row][col] == 3 and visited[row][col] == 1:
#             ans = 1
#         next_row = row + dr[i]
#         next_col = col + dc[i]
#
#         if 0 <= next_row < N and 0 <= next_col < N :
#             #맵 안에 있을 때만 진행
#
#             if MAP[next_row][next_col] == 1:
#                 continue #가려는 좌표에 벽이 있다면 무시
#
#             if visited[next_row][next_col] == 1:
#                 continue #기록을 하기 전에 이미 기록이 있다? 무시
#
#             visited[next_row][next_col] = 1 #갔으니깐 기록
#             dfs(next_row, next_col)
#
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     ans = 0
#     N = int(input())
#     MAP = [list(map(int, input().rstrip())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)] # 해당 좌표를 들렀는지 기록!
#
#
#     for row in range(N):
#         for col in range(N):
#             if MAP[row][col] == 2:
#                 dfs(row, col)
#
#     print("#{} {}".format(tc, ans))


#알파벳


import sys

r, c = map(int, sys.stdin.readline().split())

MAP = [sys.stdin.readline().rstrip() for _ in range(r)]


check = [0] * 256

ans = 0

def dfs(row, col, cnt):
    global ans
    
    ans = max(ans, cnt)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if 0 <= next_row < r and 0 <= next_col < c :
            # 맵 안에 있어야 한다
    
        asc = ord(MAP[next_row][next_col]) #아스키코드 값 추출

        if check[asc] == 1:
            continue

        check[asc] = 1
        dfs(next_row, next_col, cnt + 1)
        check[asc] = 0

check[ ord(MAP[0][0]) ] = 1
dfs(0, 0, 1) # 1 넣는것은 스타트 지점을 예의주시 한것!
print(ans)







