'''




'''
# BFS 경우의 수 커스텀
from collections import deque

def bfs(n, m):
    # 1. 그래프 구성 <- 연산으로 대체
    # 2. 큐 생성
    q = deque()
    visited = [2134567890] * (1000000 + 1)
    cnt = [0] * (1000000 + 1) # index : 어떤 수, value : 해당 수를 최소 횟수로 만드는 경우의 수
    # 3. 시작점 세팅
    q.append(n)
    visited[n] = 1
    cnt[n] = 1
    order = [1, -1, -10]

    while q:
        # 4. now 꺼내기
        now = q.popleft()
        if now == m:
            break
        # 5. next찾기
        for i in range(3):
            next = now + order[i]
            if next < 0 or next > 1000000:
                continue
            if visited[next] < visited[now] + 1:
                continue
            if visited[next] == visited[now] + 1:
                cnt[next] += cnt[now]
                continue
            visited[next] = visited[now] + 1
            cnt[next] += cnt[now]
            q.append(next)
        next = now * 2
        if next <= 1000000 :
            if visited[next] < visited[now] + 1:
                continue
            if visited[next] == visited[now] + 1:
                cnt[next] += cnt[now]
                continue
            visited[next] = visited[now] + 1
            cnt[next] += cnt[now]
            q.append(next)
    return visited[m] - 1

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    print(f"#{tc + 1} {bfs(n, m)}")



# 연산
from collections import deque

def bfs(n, m):
    # 1. 그래프 구성 <- 연산으로 대체
    # 2. 큐 생성
    q = deque()
    visited = [0] * (1000000 + 1)
    # 3. 시작점 세팅
    q.append(n)
    visited[n] = 1
    order = [1, -1, -10]

    while q:
        # 4. now 꺼내기
        now = q.popleft()
        if now == m:
            break
        # 5. next찾기
        for i in range(3):
            next = now + order[i]
            if next < 0 or next > 1000000:
                continue
            if visited[next]:
                continue
            visited[next] = visited[now] + 1
            q.append(next)
        next = now * 2
        if next <= 1000000 and not visited[next]:
            visited[next] = visited[now] + 1
            q.append(next)
    return visited[m] - 1

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    print(f"#{tc + 1} {bfs(n, m)}")
