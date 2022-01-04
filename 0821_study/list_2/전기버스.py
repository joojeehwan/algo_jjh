'''



그리디로 풀어보자!




'''



T = int(input())

for tc in range(T):

    k, n, m = map(int, input().split())
    charges = list(map(int, input().split()))
    
    #1 3 5 7 9 <- 위치 값
    # -> li[index] => index위치

    #정류장 번호를 1차원 배열에다가 구분지어서 만듬!

    li = [0] * n

    for i in range(len(charges)):

        li[charges[i]] += 1

    # 0 1 2 3 4 5 6 7 8 9 10
    # 0 1 0 1 0 1 0 1 0 1  0 이걸 만듬!

    now = 0
    cnt = 0



    while now + k < n : #끝까지 도착햇는가의 여부
        next = now
        for i in range(now + 1, now + k + 1): #제일 먼 충전소를 찾는단

            if li[i] == 1 :
                next = i
                
        # next값이 변하지 않는 문제
        if next == now:
            break
            
        now = next
        cnt += 1
        
    if now + k >= n:
        print("#{} {}".format((tc+1), cnt))
    else:
        print("#{} {}". format((tc+1), 0))
    
    








