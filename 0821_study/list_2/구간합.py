


lst = [1,2,3,4,5]

m = 3
max_sum = -1
min_sum = 100 * 100000 + 1

#마지막 인덱스가 어디까지 가는지 고려해서 이렇게 짬
for i in range(len(lst) -m + 1):

#마지막 원래 j 만큼의 길이 만큼 확인해야 하는데 i를
    sum = 0
    for j in range(0, m):
        sum += lst[i+j]
    if max_sum < sum:
        max_sum = sum
    if min_sum > sum :
        min_sum = sum

print("#{}".format(max_sum - min_sum))

#1번 풀이,,, 이번 시험!

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    num_li = list(map(int, input().split()))
    # 모든 m 구간크기내에 합
    # 최댓값, 최솟값
    max_value = -1
    min_value = 100 * 10000 + 1
    for s in range(n - m + 1): # s : 구간의 시작 index
        sum = 0
        for i in range(m):
            sum += num_li[s + i] # m 구간내의 합
        if max_value < sum :
            max_value = sum
        if min_value > sum :
            min_value = sum
    print("#{} {}".format(tc+ 1, max_value - min_value))

#2 pre fix 합



T = int(input())

for tc in range(1, T+ 1):


    n, m  = map(int, input().split())
    num_li = list(map(int, input().split()))

    prefix = [0] * N
    prefix[0] = num_li[0]

    for i in range(1, N):
        prefix[i] = prefix[i -1] + num_li[i]


    max_value = -1
    min_value = 100 * 10000 + 1
    for s in range(n -m + 1): #구간의 시작점 s

        e = s + m - 1# 구간의 끝점

        sum = prefix[e] - prefix[s] + num_li[s]

        if max_value < sum:
            max_value = sum
        if min_value > sum:
            min_value = sum


# 슬라이딩 윈도우

    n, m = map(int, input().split())
    num_li = list(map(int, input().split()))






