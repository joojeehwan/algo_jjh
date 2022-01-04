





#선택 정렬 사용!

import sys
sys.stdin  = open("특별한정렬_input.txt")

T = int(input())

for tc in range(1, T+1): #고정하고!
    N = int(input())
    nums = list(map(int, input().split()))

    #1. 어느 위치에 넣을 수를 찾을 것인가?
    #2. 해당 위치에 들어갈 수 찾기


    for index in range(N):

        #원하는 수 2가지! 종류, 큰거 작은거,,! 번갈아가면서!

        found = 0
        if index % 2 == 0:
            max_value = 0
            for i in range(index, N): #옮겨 가면서 검색하기 위해서,,!
                if max_value < nums[i]:
                    max_value = nums[i]
                    found = i #이것을 찾는 이유는! 인덱스에 맞게, 그 값을 넣기 위해서!

        else:
            min_value = 101
            for i in range(index, N):
                if min_value > nums[i]:
                    min_value = nums[i] #min valu를 이용해서 인덱스를 찾기 위해서!
                    found = i  #이때의 인덱스,,!


        nums[index], nums[found] = nums[found], nums[index]

    print("#{} ".format(tc), end="")
    for i in nums: # {} 뒤에 한칸 뛰는게 포인트!
        print("{} ".format(i), end="")
    print("") #다음 테스트 케이스를 위해서 반드시!! 안하면 안돼







################################

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