

import sys

sys.stdin = open("hyeonjoo_box_change_input.txt")





T = int(input())




for tc in range(T + 1):

    N, Q = map(int, input().split())


    li = [0] * (N+1) #왜냐면 1번 인덱스부터 사용할려고!

    for i in range(1, Q + 1): # 아 1로 시작해서 자연스럽게 i반째 작업을 숫자를 넣어준다!

        L, R = map(int, input().split())
        for j in range(L, R+1):

            li[j] = i #인덱스에 바로 넣어버릴려고!



        print("#{}". format(tc), end ="")
        for i in range(1, N+1): #여기선 이 방법을 써야만 한다!
            #왜냐면 앞에 불필요한 인덱스를 하나 썻으므로! JOIN으로 풀 수가 없다!

            print("{} ".format(li[i]) , end = "")

        print("")


