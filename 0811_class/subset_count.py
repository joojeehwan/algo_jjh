
import sys

sys.stdin = open("subset_count.txt")


#
# arr = [2,3,-2,-3,5]
#
# n = len(arr)
#
# lili = []
#
# for i in range(1 << n):
#     sum = 0
#     for j in range(n+1):
#         if i & (1<<j):
#             sum += arr[j]
#
# print(sum)



T = 10
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    #index:  0 1 2 3 4
    #value:  2 3-2-3 5
    # bit :  0 0 0 0 0 -> 0
    #        1 1 1 1 1 -> 31
    #      1 0 0 0 0 0 -> 32 => 1 << N
    #                1
    ans = 0 # 경우의 수
    for bit in range(1 << N) :
        # 부분집합에 사용할 원소들 고르는 작업
        # bit : 0  0  0  1  1 <- 2진'수'
        #index: 4  3  2  1  0
        sum = 0
        for index in range(N):
            # 부분집합에 사용하는 원소 구별(어떤 원소를 사용했는가?)
            if 1 << index & bit != 0 :
                # 1 << index & bit = index위치에 어떤 값이 있는가?
                # 1 << index & bit != 0 => 어떤 값이 있다!
                sum += nums[index]
                # 부분집합에 사용하는 원소 합산
        if sum == 0:
            ans += 1
    print("#{} {}".format(tc + 1, ans))


# 아 오키 이해했음!


