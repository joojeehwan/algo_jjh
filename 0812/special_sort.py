T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    # 1. 어느 위치에 넣을 수를 찾을것인가?
    # 2. 해당 위치에 들어갈 수 찾기
    for index in range(N):
        # 0~N-1 위치
        # 원하는 수 <- 2가지 종류, 큰 or 작은 <- 번갈아가며
        found = 0 # 찾은 index
        if index % 2 == 0: # 큰 수 찾을 차례
            max_value = 0
            for i in range(index, N): #요게 포인트 index로 두고 앞으로 옮기는,,!
                if max_value < nums[i]:
                    max_value = nums[i]
                    found = i
        else : # 작은 수 찾을 차례
            min_value = 101
            for i in range(index, N):
                if min_value > nums[i]:
                    min_value = nums[i]
                    found = i
        nums[index], nums[found] = nums[found], nums[index]
    print("#{} ".format(tc + 1), end = "")
    for i in nums:
        print("{} ".format(i), end = "")
    print("")




# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     lst = list(map(int, input().split()))
#
#     #선택정렬로 풀기! => 자리를 기억하는 tip,,!
#     #정렬 후에
#
#
#     for i in range(len(lst)):
#         min_idx = i
#         for j in range(i+1, len(lst)):
#             if lst[min_idx] > lst[j]:
#                 min_idx = j
#         lst[i], lst[min_idx] = lst[min_idx], lst[i]
#
#
#
#     for _ in range(len(lst) // 2):
#         print(f"{lst.pop(len(lst)-1)} {lst.pop(0)}, end=" ")

