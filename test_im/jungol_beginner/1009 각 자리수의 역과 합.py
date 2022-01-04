

def sol(n):
    sum = 0
    num = 0
    while n :
        #뒷자리부터 십의 자리씩 추가하면서 일의자리 나머지 숫자 만들기
        num = (num * 10) + (n % 10)
        #합 구하기! 각각 숫자 하나씩 구하는 방법! 나머지로!
        sum += (n % 10)
        n = n // 10

    print(f"{num} {sum}")



while True:
    n = int(input())
    if n == 0:
        break
    sol(n)


