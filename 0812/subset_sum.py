


# T = int(input())
#
# N, K  = int(input())
#


lst = [1,2,3,4,5,6,7,8,9,10,11,12]

print(1<<12)
# n = len(lst)
#
# res = []
# for i in range(1<<n):
#
#     for j in range(n):
#
#         if i & (1<<j):
#             print(lst[j] ,end = " ")
#             res.append(lst[j])
#     print()
# print()

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1 << 12):
        # bit 들을 만듦(하나의 부분집합)
        sum = 0
        cnt = 0
        for j in range(12):
        # j번째 수를 사용할 것인가?
            if i & (1 << j) != 0:
                # j번째 bit를 filtering한 결과가 1이 있으면
                # => 0이 아니라면 j번째 수를 사용하겠다는 의미
                sum += j + 1
                cnt += 1
        if sum == K and cnt == N:
            ans += 1
    print("#{} {}".format(tc + 1, ans))