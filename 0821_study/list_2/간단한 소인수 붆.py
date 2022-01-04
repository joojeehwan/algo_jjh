

import sys

sys.stdin = open("easy_prime_factorization_input.txt")




T = int(input())



for tc in range(1, T+1):


    d = 2
    N = int(input())


    res = [0] * 5

    while d <= N: #나눌 숫자가 d보다 작아지면 소인수 분해를 멈춘다..나뉘어 지는 숫자가 소인수 분해를 하는 숫자에 가꿔워지면! 
        if N % d ==0 : #처음 start를 2로 두고! N % d가 나누어진다면 5개의 숫자를 인덱스로 구분하여 해당 값이 들어오면 값을 증가
            if d == 2:
                res[0] += 1
            elif d == 3:
                res[1] += 1
            elif d == 5:
                res[2] += 1
            elif d == 7:
                res[3] += 1
            else:
                res[4] += 1
            N = N / d #나누어져서 if절안에 들어왓으면 그 다음을 위해서, N을 d로 나누어서 와일문이 끝나가기를 윧ㅎ한다!
        else:
            d = d + 1 #나뉘어 지지 않았으면 다른 소인수를 찾아야 하기때문에 1씩 증가

        print(f"#{tc} {' '.join(map(str, res))}")

T = int(input())

for tc in range(T):
    N = int(input())
    divide = [2,3,5,7,11]
    cnt = [0] * 5
    for i in range(len(divide)): #나눌 수 있으면 계속 나누기 위해서!  for문으로 i를 고정하고!
        while N > 0 and N % divide[i] == 0:
            N //= divide[i]
            cnt[i] += 1

    print("#{} ".format(tc + 1), end='')
    for i in cnt:
        print("{} ".format(i), end='')
    print("")