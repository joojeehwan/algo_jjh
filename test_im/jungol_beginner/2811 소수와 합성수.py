'''

소수 : 1보다 큰 자연수 중 1과 자기 자신 두 개만을 약수로 갖는 수를 말한다.

합성수 : 1보다 큰 자연수 중 소수가 아닌 수를 말하며 3개 이상의 약수를 갖는다.


'''

#소수 확인 함수
import math

def isPrime(n):

    if n < 2 :
        return False

    #0이 되는게 있으면 이건 소수가 아니야!
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


#1차원 배열로 입력받기

lst = list(map(int, input().split()))

for num in lst:

    if num < 2:
        print("number one")
        continue

    elif isPrime(num):
        print("prime number")

    else:
        print("composite number")

    


