'''


소수

약수의 개수가 1과 자기자신, 총 2개라는 점을 이용하여 구현
'''

count = 0

# def sum_Prime(m , n):
#
#     sum = 0
#     #이중 포문으로 완전검색
#     #찎고 돌리기!
#     for i in range(m, n+1):
#         count = 0
#         for j in range(1, i+1):
#             if i % j == 0 :
#                 count += 1
#         if count == 2:
#             sum += i
#
#     if sum == 0 :
#         return -1
#     return sum
#
#
# def min_Prime(m, n):
#
#     for i in range(m, n+1):
#         count = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 count +=1
#         if count == 2:
#             return i

# res_sum = 0
# res_min = 0
#
# res_sum = sum_Prime(M, N)
# res_min = min_Prime(M, N)
#
# if res_sum == -1:
#     print("-1")
#
# else:
#     print(f"{res_sum}")
#     print(f"{res_min}")


#방2
import math

M = int(input())
N = int(input())

ans = 0
MIN = 987654321
for i in range(M, N):

    if i == 1:
        continue

    flag = False

    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0: #소수가 아님!
            flag = True
            break #그러니깐 반복 종료

    if flag == False:
        ans += i
        MIN = min(MIN, i)

if ans == 0:
    print("-1")

else:
    print(f"{ans}")
    print(f"{MIN}")