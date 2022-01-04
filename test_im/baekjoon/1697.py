'''


숨바꼭질

bfs 기본형 공부하고 다시 풀어보자

#1차원 bfs 어렵구만?

'''


from collections import deque

def bfs():

    q = deque()
    q.append(N)
    visited[N] = 1
    while q:
        now = q.popleft()

        if now == K:
            print(visited[now] - 1)

        dr = [-1, 1, 2]
        for i in range(3):
            if i == 2:
                next = now * dr[i]
            else:
                next = now + dr[i]

            if next < 0 or next > 1000000:
                continue

            if visited[next] != 0:
                continue


            visited[next] = visited[now] + 1
            q.append(next)

N, K = map(int, input().split())
visited  = [0] * 1000001
bfs()







