import os
import time


'''

백트래킹! (기본은 dfs)
다 해보면 시간이 너무 오래걸려,,! 그래서 중간에 안해보는 경우를! 

끝까지 다 만들고 판단 한느 것이 아니라, 중간에 확인을 해본다! 

now와 now +1 의 관계

다음이 여러개면 그에 맞게 또 재귀,,! 





가지치기 : 현재에서 다음으로 가는데 다음으로 가도 되는지 확인하겠다,,!

가도 되는지 확인 하는 조건이 바로 "가지치기"



백트래킹 스킬

"패스" : 내가 어떻게 왓는지 기록! 

-1 : 모름, 0 : 사용안함 1 : 사용함

'''





def print_elements(sum):
    print("sum : ", sum)
    print("elements - 1 : used, 0 : unused , -1 : unknown")
    for i in range(1, 21):
        print("{}".format(i), end = "  ")
    print("")
    for i in range(1, 21):
        if path[i] != -1:
            print(" ", end = "")
        print("{}".format(path[i]), end = " ")
        if i >= 10:
            print(" ", end = "")

    print("")
    time.sleep(0.1)
    os.system("cls")

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    ans = 0
    path = [-1] * 21
    # 내가 어떻게 해왔는가? 를 기록
    # -1 : 확인 안됨, 0 : 사용 X, 1 : 사용 O
    def dfs(now, sum, cnt):
        # now : 이번에 확인할 값,
        # sum : 지금까지 만들어온 값,
        # cnt : 지금까지 사용한 값의 개수
        print_elements(sum)
        de = 1
        if now >= 21:
            # 기저조건 : 끝날 조건
            # '가지치기를 통과해서 끝까지 잘 도착했다' : 정답의 가능성이 있다.
            #---- 정확히 N개의 개수로 합이 K가 되는가?
            return

        # 사용한 경우
        if sum + now <= K and cnt < N: # 가지치기
            # k : 합, N : 개수
            path[now] = 1 # now를 사용했다라고 기록
            dfs(now + 1, sum + now, cnt + 1)

        #사용하지 X
        path[now] = 0 # now를 사용하지 않는다고 기록
        dfs(now + 1, sum, cnt)

        path[now] = -1 # now가 끝나서 초기값으로 되돌려 놓음

    dfs(1,0,0)
    print("#{} {}".format(tc + 1, ans))