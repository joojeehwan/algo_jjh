#bfs로 풀 수 있는 문제구만,,,!




'''


상원이의 생일 파티가 곧 열린다!

그렇기에 상원이는 반 친구들에게 생일 파티 초대장을 주려고 한다.

그러나 파티가 어색하게 되는 것을 원치 않는 상원이는 모든 친구들에게 초대장을 줄 생각이 없다.

같은 반에 있지만, 서로 친한 친구가 아닐 수도 있기 때문이다.

상원이는 우선 자신과 친한 친구들에게는 모두 초대장을 주기로 했다.

여기에 더해서 친한 친구의 친한 친구인 경우에도 초대장을 주기로 했다.

총 몇 명의 친구들에게 초대장을 주어야 하는지 구하는 프로그램을 작성하라.

상원이의 반에는 N명이 있으며, 각 학생들은 1번에서 N번까지의 번호가 붙어 있다.

여기서 1번 학생이 상원이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에 두 정수 N, M ( 2 ≤ N ≤ 500, 1 ≤ M ≤ 104 ) 이 공백으로 구분되어 주어진다.

M은 친한 친구 관계의 수 이다.

다음 M개의 줄의 각 줄에는 두 정수 a, b (1 ≤ a ＜ b ≤ N) 이 주어진다.

이는 a번 학생과 b번 학생이 서로 친한 친구 관계에 있다는 의미이다.

[출력]

각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 각 테스트 케이스마다 상원이의 생일 파티 초대장을 받는 친구의 수를 출력한다.

*상원이의 친구가 없을 수도 있다는 점에 유의해야 한다. 그리고 상원이는 초대장을 받는 사람에 속하지 않는다.



'''

from collections import deque


def bfs(value):

    q = deque()
    q.append(value)
    visited[value] = 1
    cnt  = 0
    dist = 0
    while q:

        for _ in range(len(q)):
            now = q.popleft()
            for i in adj_list[now]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        dist += 1 #층
        if dist == 2:
            break
    return cnt

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        frm, to = map(int, input().split())
        adj_list[frm].append(to)
        adj_list[to].append(frm)

    visited = [0] * (N + 1)
    ans = bfs(1)

    print(f"#{tc} {ans}")








##################################

# T = int(input())
#
# for tc in range(1, T + 1):
#
#     #N 노드의 수 M 간선의 수
#     N, M = map(int, input().split())
#     MAP = []
#
# #강수현님
# def bfs():
#     global friends_cnt
#
#     q = [1]
#     invited = [0] * (N + 1)
#     invited[1] = 1
#     cnt = 0
#     while q and cnt < 2:
#         for _ in range(len(q)):
#             now = q.pop(0)
#             for person in range(2, N + 1):
#                 if invited[person]:
#                     continue
#                 if MAP[now][person]:
#                     invited[person] = 1
#                     friends_cnt += 1
#                     q.append(person)
#         cnt += 1
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     MAP = [[0] * (N + 1) for _ in range(N + 1)]
#     for _ in range(M):
#         person1, person2 = map(int, input().split())
#         MAP[person2][person1] = 1
#         MAP[person1][person2] = 1
#     friends_cnt = 0
#     bfs()
#     # wanted_friend_set.remove(1)
#     # friends_cnt = len(wanted_friend_set)
#     # for idx in range(N + 1):
#     #     if idx in wanted_friend_set:  # 1번의 친구 제외
#     #         continue
#     #     if parents[idx] in wanted_friend_set:
#     #         friends_cnt += 1
#
#     print(f'#{tc} {friends_cnt}')
#
# #윤창목님
# from collections import deque
#
# for t in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     f = [[] for i in range(n + 1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         f[a].append(b)
#         f[b].append(a)
#     inv = 0
#     checked = [0] * (n + 1)
#     q = deque([(1, 0)])
#     checked[1] = 1
#     while q:
#         now, depth = q.popleft()
#         if depth == 2:
#             continue
#         for friend in f[now]:
#             if checked[friend]:
#                 continue
#             inv += 1
#             checked[friend] = 1
#             q.append((friend, depth + 1))
#
#     print(f'#{t} {inv}')
#
# #임지환님
# def bfs(num):
#     global count
#     q = []
#     q.append(num)
#     depth = 0
#     visited[num] = 1
#     while q:
#         for _ in range(len(q)):
#             temp = q.pop(0)
#             for j in tree[temp]:
#                 if visited[j] == 0:
#                     q.append(j)
#                     visited[j] += 1
#                     count += 1
#         depth += 1
#         if depth == 2:
#             break
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     answer = 0
#     N, M = map(int, input().split())
#     tree = [[] for _ in range(N + 1)]
#     visited = [0] * (N + 1)
#     for _ in range(M):
#         a, b = map(int, input().split())
#         tree[a].append(b)
#         tree[b].append(a)
#     count = 0
#     bfs(1)
#     print(f'#{test_case} {count}')