#재귀도 함수가 쌓이는 모습! 스택이랑 같은 구조! 그래서,,! 스택을 안쓰고 재귀로 구현 가능!



#백준 문제 추천

#1.백준 2606 바이러스 < 기본 dfs 구현(스토리만 추가)
#2. 백준 섬의개수 4963





def dfs1(s, V):
    visited = [0]*(V+1)
    stack = []
    i = s  # 현재 방문한 정점 i
    #visited[i] = 1
    print(node[i])
    while i!=0: #True:
        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w]==0:
                stack.append(i) # 방문 경로 저장
                i = w           # 새 방문지 이동
                #visited[w] = 1
                print(node[i])
                break
        else:           # 다음 정점이 없으면
            if stack:
                i = stack.pop()   # 지나온 정점이 남아있는 경우
            else:
                i = 0             # 지나온 정점이 남아있지 않은 경우
                # break
    return


# dfs : 주로 모든 방법을 다 해봐야 하는 경우
#



visited = [0] * 8
prev = [0] * 8 # <- 누구를 통해서 왔는가?
counts = [0] * 8 # <- A로부터 얼마나 가야되는가?
# visited[index], index : 위치 번호, value : 들렸는가?
def dfs2(now): # now : 지금 위치한 점
    # 2. 옵션 (기저조건, 문제에 따라 특이한 끝날 조건)
    print(node[now])
    # 1. 현재 now에서 갈 수 있는 next를 찾아서 가라!
    for i in range(1, 8):
        if adj[now][i] == 1 and visited[i] == 0:
            next = i
            visited[next] = 1 # next로 간다고 기록
            counts[next] = counts[now] + 1
            prev[next] = now
            dfs2(next)

    #3. 문제가 생길 수 있는 부분(Error발생 가능한 부분들 수정)
    #4. 계산 및 추가 작업


#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
node = ['', 'A','B','C','D','E','F','G']
'''
7 8
1 2
1 3
...
'''
# V, E = map(int, input().split())
# ad = [[0]*(V+1) for _ in range(V+1)]
# for _ in range(E):
#    n1, n2 = map(int, input().split())
#    ad[n1][n2] = 1
#    ad[n2][n1] = 1

visited[1] = 1
dfs2(1)
de = 1