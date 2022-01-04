'''

약수 구하기



'''



N, K = map(int, input().split())

divisor = []

for i in range(1, N+1): #자연스럽게 작은 수 부터 넣게 됨,,!

    if N % i == 0:
        divisor.append(i)

# print(divisor)

if len(divisor) < K:
    print("0")

else:
    print(divisor[K-1])