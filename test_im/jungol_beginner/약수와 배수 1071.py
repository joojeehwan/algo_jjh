


n = int(input())

lst = list(map(int, input().split()))

target = int(input())

divisor = []
multiple = []


for i in range(len(lst)):

    #약수 구하기
    if target % lst[i] == 0:
        divisor.append(lst[i])

    #배수 구하기
    if lst[i] % target == 0:
        multiple.append(lst[i])

print(sum(divisor))
print(sum(multiple))


#12의 배수는 3의 배수이면서 4의 배수인 수
