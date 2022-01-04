

import sys
sys.stdin  = open("앞글자따기_input.txt")


# T = int(input())
#
#
# for tc in range(1, T+1):
#
#     N = int(input())
#
#     sen = input().split()
#
#     res =""
#     for se in sen:
#
#         res += se[0]
#
#
#     print("#{} {} ".format(tc, res.upper()))

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    res = list(input().split()) #입력 받기!


    a = "" #정답을 넣을 변수 str
    for i in range(len(res)):
        if res[i][0].islower(): #맨 앞글자가 소문자면
           a += res[i][0].upper() # 그 소문자를 대문자로 바꾸어서 넣자! 

    print(f"#{tc} {a}")
