'''


오 N값이 너무 커지면,,

1. 입력

2. 리스트 에서 작은 값을 찾는다. 만약에 여러개라면 그것도!

3. 그 다음에 리스트 전체를 보면서 가장 값이 큰날의 값하고 뺼셈연산

4. 작은 리스트 찾기를 다시 처음부터 다시 한다.

5. 위와 같은 과정을 리스트 처음 부터 끝까지 한다.



이중 포문을 돌려야 되는데,,! 어떻게 돌려야 하나,,

=> 내 뒤에서 가장 큰 것을 찾아서 뺸다.

'''


'''
뒤에 날짜부터 앞으로 간다! 
마지막의 날의 값이 최고라고 생각! 앞으로 가면서 이익금 !
가다가 더 큰 값이 나오면 최고의 값을 바꾼다! 

1원마나면 +1

3원이 더 크니깐 갱신

1만나면 +2

1만나면 +2


문제 풀면서 앞으로 가면서 어려우면 뒤로 가면서,,! 생각해보아라! 

'''



T = int(input())


for tc in range(1, T+1):

    N = int(input())

    cost = list(map(int, input().split()))

    ans = 0


    #맨 뒤에 있는 값을 최대의 값이라 생각
    max_cost = cost[-1]

    #가장 마지막 인덱스는 제외하고 반복을 돌려야
    for i in range(N-2, -1, -1):

        #내가 가진 값 보다 작으면 뺴서 ans에 누적
        if max_cost > cost[i]:
            ans += (max_cost - cost[i])
        # 더 큰 값을 만나면 max_cost값 바꾸기
        else:
            max_cost = cost[i]

    print(f"#{tc} {ans}")





#서 교수님 풀이

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    lst = list(map(int, input().split()))

    max_price = 0

    ans = 0

    for i in range(N-1, -1, -1):

        max_price = max(max_price, lst[i])

        ans += (max_price - lst[i])





# T = int(input())
#
#
# for tc in range(1, T+1):
#
#     N = int(input())
#
#     cost = list(map(int, input().split()))
#
#     ans = 0
#
#     #팔아도 되는 날을 체크
#     is_sell = [False] * N
#
#
#     for i in range(N-1):
#         for j in range(i, N):
#
#             if cost[i] > cost[j]:
#                 is_sell[i] = True
#                 break


T = int(input())

for tc in range(1, T+1):

    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [False] * N


    #i idx이후에 그 값보다 큰 값을 찾으면 그 날에는 팔아도 되니깐
    #팔아도 되는 날의 인덱스를 체크
    for i in range(N-1):
        for j in range(i+1, N):
            if cost[i] > cost[j]:
                is_sell[i] = True
                break
    buy_cost = 0
    buy_cnt = 0

    for i in range(N):
        if is_sell[i]:
            buy_cost += cost[i]
            buy_cnt += 1
        else:
            ans += (cost[i] * buy_cnt) - buy_cost
            buy_cost = 0
            buy_cnt = 0

    print("#{} {}".format(tc, ans))