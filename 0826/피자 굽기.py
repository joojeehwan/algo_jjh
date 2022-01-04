



import sys
sys.stdin = open("피자 굽기_input.txt")


#번호를 출력하기 위해서,,! 큐에다가 인덱스랑 값을 같이 넣어준다!


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = []

    for i in range(M):
        q.append([i+1, lst[i]]) #인덱스 +1 = 번호

    in_fire = q[:N] #슬라이싱 0 ~ N
    out_fire = q[N:] #슬라이싱 N 부터 끝까지


    while len(in_fire) > 1 :

        check = in_fire.pop(0)
        check[1] //= 2
        if check[1] == 0:
            if out_fire: #밖에 피자가 있고
                in_fire.append(out_fire.pop(0))

        else:
            in_fire.append(check)

    print("#{} {}".format(tc, in_fire[0][0]))


#########################################


T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza = [ (pizza[i], i + 1) for i in range(m) ]
    oven = pizza[:n] #슬라이싱! 놏치지마!
    pizza = pizza[n:]

    while len(oven) != 1:
        now = oven.pop(0) # (치즈량, 피자 번호)
        cheese = now[0]
        num = now[1]
        # 피자 꺼내기
        cheese //= 2
        # 치즈량 갱신
        if cheese == 0:
            if len(pizza) != 0:
                oven.append(pizza.pop(0))
        else :
            oven.append( (cheese, num) )

    print("#{} {}".format(tc + 1, oven.pop()[1]))









