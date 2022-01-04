


import sys

sys.stdin = open("숫자를정렬하자_input.txt")

# #이거 선택정렬로 풀자!
# T = int(input())
#
# N = int(input())
#
# for tc in range(1,T+1):
#     lst = list(map(int, input().split()))
#
#     for i in range(len(lst)-1, 0, -1):
#         for j in range(0, i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#
#     print(f"{tc} {''.join(str(lst))}")
#


T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    # 1. 이번에 맞춰줄 위치(바꿀 위치)
    # 2. 해당 위치에 들어갈 숫자
    # 3. 해당 위치에 들어갈 숫자를 넣어준다.

    # for index in range(N):
    #     min_value = 2135467890
    #     found = 0
    #     for i in range(index+1, N):
    #         if min_value > nums[i]:
    #             min_value = nums[i]
    #             found = i
    # nums[index], nums[found] = nums[found], nums[index]

    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


    print("#{} ".format(tc + 1), end = "")
    for i in nums:
        print("{} ".format(i), end = "")
    print("")