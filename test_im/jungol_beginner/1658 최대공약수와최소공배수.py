'''


최대 공약수와 최소공배수

유클리드 호제법을 이용해서 하면 빠르게 구할 수 있음!

그전에 주먹구구식도 알아보자!


최소공배수(lcm)는 별도의 함수를 작성하여 구할 수도 있겠지만 두 수의 최대공약수를 알고 있다면 다음의 규칙을 이용하여 쉽게 구할 수 있다.

두 수의 곱은 그 두수의 최대공약수와 최소공배수의 곱과 같다.

a와 b의 최대공약수를 gcd(a, b), a와 b의 최소공배수를 lcm(a, b)라 하면 a * b = gcd(a, b) * lcm(a, b)
따라서 두 수의 최대공약수를 알 경우 최소공배수는 두 수의 곱을 최대공약수로 나눈 몫을 구하면 된다.
(lcm = a * b / gcd)

'''



# n, m = map(int, input().split())
#
# gcd = 0
# lcm = 0
#
# #최소 공배수를 구하는 반복문
# for i in range(1, n + 1):
#
#     if n % i == 0 and m % i == 0:
#
#         gcd = i
#
# print(gcd)
#
# lcm = (n * m) / gcd
#
# print(int(lcm))

#유클리드 호제법으로도 해보자!


'''
<유클리드 호제법>
A를 B로 나눈 나머지가 r이라면 A와 B의 최대공약수는 B와 r의 최대공약수와 같다.
 GCD(A, B) = GCD(B, r) 이 원리를 이용하면 두 수의 최대공약수를 간단하게 구할 수 있다.

'''

#반복문 버젼

n, m = map(int, input().split())

def gcd_get(x, y):

    while y!=0: #y가 0이면 x가 최대공약수 이므로 종료한다.
        r = x % y  #나머지를 구하고
        x = y # x를 y로
        y = r # y를 r로 바꾸고 다시 반복
    return x
# print(gcd_get(24 ,18))


#재귀 버젼 => 훨씬 쉬움!

def gcd_get_recurion(x, y):

    if y == 0 :
        return x

    return gcd_get_recurion(y, x % y)


print(gcd_get_recurion(24, 18))