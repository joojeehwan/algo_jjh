''''

배수 관계에 있기 떄문에 그리디가 적용이 됨

배수관계가 아니라면 다이나믹 프로그래밍 방법으로 고민을 해야 함 

'''

#거슬러 줄 수 있는 가장 최대의 값으로 거슬러 주는게 맞다


T = int(input())

for tc in range(1, T+1):

    N = int(input())

    moneys = [50_000, 10_000, 5_000, 1_000, 500, 100, 50, 10]

    changes = [0] * 8


    for i in range(len(moneys)):

        if N // moneys[i] != 0 :
            changes[i] = N // moneys[i]
            N %= moneys[i]

    print(f"#{tc} ")
    print(*changes)




    