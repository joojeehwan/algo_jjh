'''



최소 몇번의 연산?! => BFS의 냄새가 난다



'''

from collections import deque


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().splti())
    
    ans = 0
    
    visited = set()

    visited.add(N)
    
    #큐 생성
    q = deque()

    #시작점 세팅
    q.append((N,0))

    while q:

        val,check = q.popleft()

        if N == M :
            break

        if val+1 not in visited and val + 1 <= 1000000:
            pass