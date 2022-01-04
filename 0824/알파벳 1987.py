

#알파벳 풀이! 백ㅈ준


'''


dfs 구조

1) dr, dc => 한번씩 간다

- 안되는 조건은 continue로 무시!(ex 맵안에 있어야한다,,,!)

2) 그리고 간다! 재귀로! dfs(next_row, next_cl)




'''


'''


패스를 이용해서, 내가 지나온 알파벳을 알아버리네,,,? -> 근데 시간초과! 

(사진 확인)
그럼 어떻게?! DAT를 사용함! 

CHECK배열의 인덱스에 의미를 부여!  => 중복 알파벳을 피할 수 있다.



'''

'''

<백트래킹>

다른 경로를 보고 싶을때,,!!

갓을떄는 기록을 해두지만, 갓다가 돌아올때는 기록을 지워줘야해! 

그래서 DFS(NEXT_ROW, NEXT_COL) 다음에 CHECK[ASC] = 0인것!

사진확인! E에서 D로 갈떄 다시 기록된걸 지워야 해! 

"와와.. 기록을 지우기만 해도 다양한 경로(모든 경로)를 확인할 수 있음"

'''

'''



문제에서 원하는 건 최대 길이!!


1. DFS(R, C, CNT)
글로벌 ans
ans = max(ans, cnt)
다음점 갈떄 DFS(R, C, CNT+1)

'''

#교수님 풀이

import sys


r, c = map(int, sys.stdin.readline().split())

MAP = [ sys.stdin.readline().rstrip() for _ in range(r) ]

path = []
# DAT <- Direct Access Table
check = [0] * 256
# check[index] -> index: 아스키코드값, value : 해당 아스키코드를 들린적 있는가?
ans = 0
def dfs(row, col, cnt):
    global ans
    ans = max(ans, cnt)
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if 0 <= next_row < r and 0 <= next_col < c:
            # 맵 안에 있어야 한다.
            asc = ord(MAP[next_row][next_col]) # 아스키코드값 추출
            if check[asc] == 1:
                continue
                # 이번에 들릴 문자는 기록하기도 전에 기록이 되어 있다.
                # 이미 들린 문자다.
            check[asc] = 1 # 이 아스키코드값은 들렸다.
            dfs(next_row, next_col, cnt + 1)
            check[asc] = 0 # 갔다가 돌아와서는 기록 삭제

check[ ord(MAP[0][0]) ] = 1
dfs(0, 0, 1) # 1 넣는것은 스타트 지점을 예의주시 한것!
print(ans)