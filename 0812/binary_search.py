
# T = int(input())
# def binary_search(left, right, value):
#     # left ~ right사이에 value를 찾는다.
#     # value를 찾기위한 비교 횟수
#     ret = 0
#     while left<=right :
#         ret += 1
#         mid = (left + right) // 2
#         # mid : 가정해볼 수
#         if mid < value:
#             left = mid
#         elif mid > value:
#             right = mid
#         else:
#             break
#     return ret
#
# for tc in range(T):
#     P, A, B = map (int, input().split())
#     cnt_A = binary_search(1, P, A)
#     cnt_B = binary_search(1, P, B)
#     if cnt_A == cnt_B:
#         print("#{} 0".format(tc + 1))
#     elif cnt_A < cnt_B:
#         print("#{} A".format(tc + 1))
#     else:
#         print("#{} B".format(tc + 1))



import sys

sys.stdin = open("binary_search_input.txt")



def binary_search(target, start, end):
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) // 2

        if mid > target:
            end = mid

        elif mid < target:
            start = mid
        else:
            break

    return cnt



T = int(input())

for tc in range(1, T+1):

    n, m, k = map(int, input().split())

    A = binary_search(m, 1, n)
    B = binary_search(k, 1, n)

    if A > B :
        print(f"#{tc} B")
    elif A < B :
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")