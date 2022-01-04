
'''

그리디 문제는 정렬을 하고 하는 경우가 많음.

'''


T = int(input())


for tc in range(1, T+1):

    #N : 컨테이너의 수 , M: 트럭 수 
    N, M = map(int, input().split())
    #weight : 화물의 무게 리스트
    weights = list(map(int, input().split()))
    # load_capacity : 트럭의 적재 무게 리스트
    load_capacitys = list(map(int, input().split()))


    #단순히 생각해서! 가장 큰 무게를 하나씩 선택해서, 그것을 담을 수 있는 트럭을 찾자! => 그리디 적 사고

    ans = 0
    for i in range(M):
        temp = [] #새로이 담을 곳을 만듬, 머릿속에 배열 3개 생각
        for j in range(N):
            if load_capacitys[i] >= weights[j]:
                temp.append(weights[j]) 
        if len(temp) != 0:
            ans += max(temp)
            for j in range(N):
                if weights[j] == max(temp):
                    weights[j] = 0 #적대되어서 이동되었으니 없는 표시
                    break

    print("#{} {}".format(tc, ans))



# 컨테이너 운반

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight.sort(reverse = True)
    truck.sort(reverse = True)
    # sort 시간 복잡도 nlogn

    w_idx = 0 # 화물 index
    t_idx = 0 # 트럭 index
    ans = 0 # 실은 화물들의 무게

    # 제일 용량이 큰 트럭           1개당
        # 제일 용량이 큰 화물    n개의 화물
                        #총 O(m * n)

    while w_idx < n and t_idx < m:
        if weight[w_idx] <= truck[t_idx]:
            # 화물을 실을 수 있음
            ans += weight[w_idx]
            t_idx += 1
        w_idx += 1

    print(f"#{tc + 1} {ans}")