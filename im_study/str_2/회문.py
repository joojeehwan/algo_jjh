
# 회문 중요함!


#여기서 풀때의 중요한 것!
# => 세로 회문을 가로 회문 처럼 생각함! => 데이터를 전처리 한다!!

import sys

sys.stdin = open("pali_input.txt")


T = int(input())


for tc in range(1,T+1):

    N, M = map(int, input().split())

    str_map = [input().rstrip() for _ in range(N)]

    #데이터 전처리 하기,,! 세로 회문을 가로 회문으로 만들어서 생각!

    for row in range(N):

        temp = "" #세로 하나하나마다 기억 해두고! 각 세로마다! 기억할려고!
        for col in range(N):
            temp += str_map[col][row] #세러 하나값마다 temp에 저장해서!
        str_map.append(temp) # 저장! 이제 가로 회문 체크만 하면 된다!


    ans = ""

    for str_temp in str_map: #각 가로 회문 하나마다 확인해야 하니깐!

        for i in range(N - M + 1):
            temp = str_temp[i:i + M] # 이 부분이 제일 중요함!!!!정말!! 배열로 따지면
            #N-M+1 이후에 있는 range(i, i+m)가 같은것,,! 문자열이랑 인덱싱으로!
            #인덱싱으로 그 범위안에 있는 것 다 볼려고!
            cnt = 0
            for j in range(len(temp) // 2): #반절 딱 나누고!
                if temp[j] == temp[len(temp) -1 -j]:#처음이랑 끝,, 이런식으로 안으로 들어가면서 비교!
                    cnt += 1

            if cnt == len(temp) // 2: # 반절 나누어서 비교하고 같아지는게 같아지면!
                ans = temp #정답 회문을 넣기!

            '''
            if temp == temp[::-1]:
                ans = temp
                
            위의 식 다 제끼고 이렇게 해도되네,,! 40 ~ 45 줄 없어도 된다,,!
            
            '''
    print("#{} {}".format(tc, ans))



T = int(input())


for tc in range(T):

    N, M = map(int, input().split())

    str_list = [input() for _ in range(N) ]
    ans = ""

    for row in range(len(str_list)):
        #가로 회문 검사
        for col in range(N - M + 1):
            temp = str_list[row][col:col + M]

            cnt  = 0
            for j in range(len(temp) // 2):
                if temp[j] == temp[len(temp) -j - 1]:
                    cnt += 1

            if cnt == len(temp) // 2:
                ans = temp
                
        #세로 회문 검사
        for col in range(N - M + 1):

            cnt = 0 #cnt 중복되게 써도 상관 없음! 위에서 가로 검사 다 하고 오는거니깐!
            for j in range(M // 2):
                if str_list[col + j][row] == str_list[col + M - 1 - j][row]:
                    cnt += 1

            if cnt == M // 2:
                ans = temp

    print("#{} {}".format(tc, ans))









