import os
import time

'''

앤 캐슬 힌트!


현재 말이 있는 row에서 다음 row+1로 가는것을 생각! 

col[3]의 값이 1이면 거기에 있구나 판단! 두고 안두고를 알 수 있ㄷ,,! 이거 저번에 알려준거 같은데?!
=> 그 col라인 쭉 쓰면 안되니깐! 한 점이 아니라!! 



보이게 하는 것(프로그램같이 돌리는 것은 ㄴ)은 콘솔로 해라! 


'''



def print_MAP():
    for i in range(N):
        for j in range(N):
            if path[i] == j:
                print("0", end = "")
            else :
                print(".", end = "")
        print("")
    time.sleep(0.5)
    os.system("cls")



N = 8

path = [-1] * N

col = [0] * N

def dfs(row):
    if row == N:
        return
    for i in range(N):
        path[row] = i
        print_MAP()
        if col[i] == 1:
            continue # i번에 두고 싶은데 이미 사용중이면 넘어가라

        col[i] = 1 # i번 col에 두겠다.
        dfs(row + 1)
        col[i] = 0 # i번 col에 두는 작업 끝이 나서 원상복구

        path[row] = -1

dfs(0)

'''
"""
backtracking = DFS + 조건
 
"""
T = 10
 
 
def dfs(row,col):
    global answer
    if row == N:
        answer += 1
        return
 
    for i in range(N):
        if column[i] == 1:
            continue
        column[i] = 1
        dfs(row+1,i)
        column[i] = 0
 
for tc in range(T):
    N = int(input())
    column = [0]*N
    answer = 0
    dfs(0,0)
    print('#{} {}'.format(tc + 1, answer))



'''

'''


def dfs(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for i in range(N):
        path[row] = i
        #print_MAP()
        if col[i] == 1:
            continue # i번에 두고 싶은데 이미 사용중이면 넘어가라
 
        col[i] = 1 # i번 col에 두겠다.
        dfs(row + 1)
        col[i] = 0 # i번 col에 두는 작업 끝이 나서 원상복구
 
for tc in range(1,11):
    N = int(input())
    path = [-1] * N
    col = [0] * N
    cnt = 0
    dfs(0)
 
    print(f'#{tc} {cnt}')


'''
