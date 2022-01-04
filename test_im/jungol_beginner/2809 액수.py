


# N = int(input())
#
# divisor = []
#
# for i in range(1, N+1):
#
#     if N % i == 0:
#         divisor.append(i)
#
# print(*divisor)


#아 당연히 이렇게 하면 시간초과가 나는 구먼! 다른 방법으로 구해야 한다!
import math

ans = []

N = int(input())

sq = int(math.sqrt(N))

for i in range(1, sq+1): #반복의 구간은 제곱근 만큼 이루어지는 구나!

    if N % i == 0 : #작은수 저장
        ans.append(i)

        if N / i != i : #큰수 저장 홀수개일때의 중간의 것은 이 조건을 만족 못하고 위에서 넣어지고 끝!
            ans.append(int(N / i))

res = sorted(ans)

print(*res)