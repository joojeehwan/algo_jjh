''''




최소의 갯수,,, 어떻게 하면 최소가 될까?!
=> 그리디 적 생각,, 가장 많은 것을 켜는 방향으로,,! 그 다음에 끄는 생각!


최소 갯수,, => 가장 많은 것을 키고, 그 다음에 끈다!

탐색 하면서 가장 맨 앞에 있는 것을 만나면 그것을 일단 키고! 같은지 확인 하고!
그 다음에 다음의 수를 키고 같은지 확인하는 방법으로 간다!

같은지 확인은 어떻게 하지,,? 리스트 안 값을 str으로 바꾸어서 그 값이 동일 한지 확인!
문자로 같은지 비교 할 수 있으니깐!


타켓에서 비어 있는 인덱스 알아와야 한다! 맞지?

'''
'''

 5                  
 5                   
 1 1 0 0 1       
 6                   
 0 1 1 1 0 0     
 7
 1 1 1 1 1 1 1
 10 
 0 1 0 1 0 1 0 1 0 1 
 20 
 0 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 1 1 0 0




'''


import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    lst = [0] * N
    target = list(map(int, input().split()))
    cnt = 0
    zero_taget_idx = []
    flag = 0
    for i in range(len(target)):
        if target[i] == 0:
            zero_taget_idx.append(i)

    if target[0] == 1:
        for i in range(N):
            lst[i] = 1
        cnt += 1

        for i in range(len(zero_taget_idx)):

            for j in range(zero_taget_idx[i], N, zero_taget_idx[i]*2):
                if lst[j] == 0:
                    lst[j] = 1
                else:
                    lst[j] = 0
            cnt += 1
            if "".join(map(str, lst)) == "".join(map(str, target)):
                break
        # for i in range(N):
        #     if lst[::-1] == 1:
        #         cnt += 1

    # for i in range(1, 3): # 맨 처음 부터 누르는 것!
            # i = 1 #1번쨰 인덱스 1부터 시작으로 함! 이게 커가는게 곱하기로 커간다!
    else:
        one_pos = []
        for i in range(len(target)):
            if target[i] == 1:
                one_pos.append(i)

        for i in one_pos:

            for j in range(i, N, i*2):

                if lst[j] == 1:
                    lst[j] = 0
                else:
                    lst[j] = 1
            cnt += 1
            if "".join(map(str, lst)) == "".join(map(str, target)):
                break


    print("#{} {}".format(tc, cnt))






