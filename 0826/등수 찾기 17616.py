

'''



인접행렬로 할 수 없다,,! 37기가,,



해결 전략,,!

등수의 높고 낲음을 그래프로 표현하고 !

낮은 곳, 높은 곳으로 dfs, bfs 탐색(완전탐색)으로 갯수르 구한다!

방향이 2개라서! 두개로 데이터를 따로 저정한다!


뮨제점,,!

1) 더 못본 친구가 겹칠 수 있다.


now룰 세면 되겠네,,! x로 부터 근처에 있는 애들이 now로 나오자나! !


최저등수랑 최고등수는 한 끗 차이!
now에서 next를 찾는 곳이 달라 지느ㅡㄴ 곳! 

'''


from collections import deque
import sys

N, M, X = map(int, sys.stdin.readline().split())
data_up = [[] for _ in range(N + 1)] # 더 잘본 얘들
data_down = [[] for _ in range(N + 1)] # 더 못본 얘들

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    data_down[A].append(B)
    data_up[B].append(A)
# 그래프 구성

# 1) 더 못본얘들 위주
# 2. queue생성
q = deque()
visited = [0] * (N + 1)
# 3. 시작점 세팅
visited[X] = 1
q.append(X)
# 7. 4~6단계 반복
cnt = 0# 나보다 몇 명이 못봤는지
while q:
    # 4. now꺼내기
    now = q.popleft()
    cnt += 1
    # 5. now에서 갈 수 있는 next
    for next in data_down[now]:
        if visited[next] != 0:
            continue
        #6. next를 queue에 추가
        visited[next] = 1
        q.append(next)
ans1 = N - cnt + 1 # 최소 등수

# 1) 더 잘본 얘들 위주
# 2. queue생성
q = deque()
visited = [0] * (N + 1)
# 3. 시작점 세팅
visited[X] = 1
q.append(X)
# 7. 4~6단계 반복
cnt = 0# 나보다 몇 명이 못봤는지
while q:
    # 4. now꺼내기
    now = q.popleft()
    cnt += 1
    # 5. now에서 갈 수 있는 next
    for next in data_up[now]:
        if visited[next] != 0:
            continue
        #6. next를 queue에 추가
        visited[next] = 1
        q.append(next)
ans2 = cnt
print(ans2, ans1)