'''

1.일단은 N자리 이진수에 1이 K개 있는 수들의 경우의 수를 구해야 한다.
=> 조합,,!

combi :

2. 그럼 다음에 그런 이진수를 3의 배수 인지 판단!
=> 10진수로 바꿔서 3으로 나누어서 0인지 확인!

3. 전체 경우의 수 중에서 "2."의 조건을 만족하는 경우의 수를 출력


'''

#아니 이걸 반복문으로 구한다라?!
def combination(n, r):
    result = 1

    if n < r:
        return 0

    for i in range(r + 1, n + 1):
        result *= i

    for i in range(1, n - r + 1):
        result //= i

    return result



ans = combination(4,2)
print(ans)


def combination(n, r):
    result = 1
    if n < r:
        return 0

    for i in range(r + 1, n + 1):
        result *= i

    for i in range(1, n - r + 1):
        result //= i

    return result


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    minus = N // 2
    plus = N - minus

    answer = 0
    for k in range(0, K + 1):
        if (2 * k - K) % 3 == 0:
            answer += combination(plus, k) * combination(minus, K - k)

    print(f'#{tc} {answer}')