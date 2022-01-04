#연산

'''

중간결과도 항상 백만 이하의 자연수이다 => 중간결과를 항상 알아야 한다!

bfs를 쓰면서 for로 다음 숫자를 구할때 조건울 주어야 겠다는 생각이 들어야 한다.



'''

from collections import deque


# def bfs():
#
#
#     #1. 그래프 구성 => 연산으로 대체
#     #2. 큐 만들기
#     q = deque()
#
#
#
#     #3. 시작값 세팅
#     q.append(N)
#     #방문 표시
#     visited[N] = 1
#
#     #4 ~ 6 번 반복
#     while q:
#
#         #4. 큐에서 첫번째 값 꺼내기
#         now_num = q.popleft()
#
#         #추가 연산 처리
#
#         if now_num == M:
#             return visited[M] - 1 #몇번 만에 가는지를 물어보니깐! visited배열의 value를 반환하는 것!
#
#         #5. next 찾기
#
#         for next_num in [now_num + 1, now_num * 2, now_num -1, now_num-10]:
#                                             #방문하지 않은 곳
#             if 0 < next_num <= 1000000 and not visited[next_num]:
#                 visited[next_num] = visited[now_num] + 1
#                 q.append(next_num)



def bfs():


    q = deque()

    q.append(N)
    visited[N] = True

    ans = 0 #몇번만에 찾는지! 가장 최소를 만족한다!

    while q:
        size = len(q) #큐의 사이즈 만큼 반복한다! => 큐의 사이즈의 교체횟수가 곧 몇번만의 가는지 ,,!

        for i in range(size):
            num = q.popleft()
            if num == M:
                return ans

            for next_num in (num+1, num-1, num*2, num-10):
                if 0 < next_num <= 1000000 and not visited[next_num]:
                    visited[next_num] = True
                    q.append(next_num)

        ans += 1
T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    visited = [0] * 1000001

    ans = bfs()

    print(f"#{tc} {ans}")












