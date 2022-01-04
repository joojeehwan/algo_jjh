


N = int(input())


MAP = [[-1] * 100 for _ in range(100)]

row = -1
col = -1
number = 0

for i in range(N):
    for j in range(i, N):

        if i % 3 == 0:
            row += 1
            col += 1

        elif i % 3 == 1:
            col -= 1

        elif i % 3 == 2:
            row -= 1

        MAP[row][col] = number % 10
        number += 1

for i in range(N):
    for j in range(i+1):
        print(MAP[i][j], end=" ")
    print()





# #달팽이의 이동방향
# dr = [1, 0, -1]
# dc = [1, -1, 0]
#
#
# MAP = [[-1] * 100 for _ in range(100)]
#
#
# #이게 참이면 이제 방향 전환을 해야해!
# def isPossible(row, col):
#
#     if row >= N or col >= N or row < 0 or col < 0 or MAP[row][col] >= 0 :
#         return True
#
#     return False
#
#
# row = 0
# col = 0
# cnt = 0
#
# while True:
#     MAP[row][col] = cnt % 10
#
#
#     for dir in range(3):
#
#         next_row = row + dr[dir]
#         next_col = col + dc[dir]
#
#         if isPossible(next_row, next_col):
#             dir = (dir + 1) % 3
#             next_row = row + dr[dir]
#             next_col = col + dc[dir]
#             if isPossible(next_row, next_col):
#                 break
#
#         row = next_row
#         col = next_col
#         cnt += 1


#이 풀이 잠깐만 keep





