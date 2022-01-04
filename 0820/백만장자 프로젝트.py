


#마지막날은 사지 않는다!! 고려할 필요도 없이

#사야 하나? 팔아야 하나? => 시간초과


'''






첫날의 가격보다 큰 값을 찾기로 분기한다!

큰 값이 있다면 그 값으로 팔기! 



'''

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

#배열이 1개 있어도, 이중 포문을 통해서, 값을 고정하고! 그 수만큼 반복돌려서 값찾기가 가능..!
# 1차원 배열에서만 이중 포문이 나오는 것이 아니라는 것! 밖의 포문은 고정의 의미! 안의 포문이 변화!
    for i in range(N-1):
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]


        if max_cost > cost[i]:
            ans += max_cost - cost[i] #이익을 구하자

    print("#{} {}".format(tc, ans))

#2. 팔 수 있는지 없는지 체크

'''
나 보다 큰값이 있는지 없는지 나중에 나오는지 확인

만약에 나오면 표시! 

=> 이후에 과정에서 다시 한번 전체 과정 돌면서 !

그날이 사도 되는게 체크된 녀석이면! 사고! CNT를 증가! 

COST, CNT 변수 사용해서! 


파는 가격 * 개수 - 비용


'''


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

#3 반대로 생각해보자

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

    max_cost = cost[-1]


#N-2 ? N-1은 마지막 값이니깐! 아 그리고 range의 시작값이라서 값이 포함되니깐 N개의 수니깐 마지막 
    #의 인덱스가 N-1이라 그 하나 앞은 N-2가 맞다
    for i in range(N - 2, -1, -1):
        #내가 가진 값보다 보고 있는 값이 작을 때

        if max_cost > cost[i]:
            ans += max_cost - cost[i]

        else:
            max_cost = cost[i]





