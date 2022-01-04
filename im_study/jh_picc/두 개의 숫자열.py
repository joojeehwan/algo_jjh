import sys
sys.stdin = open("두 개의 숫자열_input.txt")


T = int(input())

#이건 내가 한번에 풀어버림,,! 개 지렷다,, 주지환

for tc in range(1, T+1):

    N, M = map(int, input().split())

    lst_a = list(map(int, input().split()))

    lst_b = list(map(int, input().split()))


    if len(lst_a) > len(lst_b): #길이가 긴것 짧은것 구분해야 해서!

        multiple_sum = 0
        for i in range(N - M + 1):

            temp = 0

            for j in range(M):

                temp += lst_b[j] * lst_a[i+j]

            if multiple_sum < temp :
                multiple_sum = temp

    else:
        multiple_sum = 0
        for i in range(M - N + 1):

            temp = 0

            for j in range(N):
                temp += lst_b[i + j] * lst_a[j]

            if multiple_sum < temp:
                multiple_sum = temp

    print("#{} {}".format(tc, multiple_sum))













