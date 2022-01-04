

import sys
sys.stdin = open("회문_2_input.txt")

T = 10
for tc in range(1, T+ 1):

    N = int(input())
    str_lst = [input() for _ in range(100)]

    for i in range(100):
        temp = ""
        for j in range(100):
            temp += str_lst[j][i]

        str_lst.append(temp)

    ans = ""
    max_ans = 0
    max_ans = 0
    for str_temp in str_lst:
        for i in range(100 + 1):
            for j in range(i + 1, 100 + 1):
                temp = str_temp[i:j]

                cnt = 0
                for j in range(len(temp) // 2):
                    if temp[j] == temp[len(temp) - 1 - j]:
                        cnt += 1
                if cnt == len(temp) // 2:
                    ans = temp

                if max_ans <= len(ans):
                    max_ans = len(ans)

    print(f"#{N} {max_ans}")

# T = 10
# for tc in range(1, T+ 1):
#
#     N = int(input())
#     str_lst = [input() for _ in range(100)]
#
#     for i in range(100):
#         temp = ""
#         for j in range(100):
#             temp += str_lst[j][i]
#
#         str_lst.append(temp)
#
#     ans = ""
#     max_ans = 0
#     for str_temp in str_lst:
#         for i in range(100 + 1):
#             for j in range(i + 1, 100 + 1):
#                 temp = str_temp[i:j]
#
#                 cnt = 0
#                 for j in range(len(temp) // 2):
#                     if temp[j] == temp[len(temp) - 1 - j]:
#                         cnt += 1
#                 if cnt == len(temp) // 2:
#                     ans = temp
#
#                 if max_ans <= len(ans):
#                     max_ans = len(ans)
#
#     print(f"#{N} {max_ans}")




T = 10
for tc in range(T):
    N= int(input())
    size = 100
    str_list = [input() for _ in range(size)]

    for i in range(size):
        # i : 가로 기준점
        temp = ""
        for j in range(size):
            # j : 세로 줄 번호
            temp += str_list[j][i]
        str_list.append(temp)

    ans = 0
    flag = 0 # 찾았는가?
    for M in range(size, 1, -1):
        for str_temp in str_list:
            for i in range(size - M + 1):
                temp = str_temp[i:i + M] # i~i+M-1 <- M개의 길이 문자열
                #회문 : 앞에서 부터 읽은 문자열 == 뒤에서 부터 읽은 문자열
                cnt = 0
                for j in range(len(temp)):
                    if temp[j] == temp[len(temp) -1 -j]:
                        cnt += 1
                if cnt == len(temp):
                    ans = M
                    flag = 1

    print("#{} {}".format(tc + 1, ans))

# T = 10
#
#
# for tc in range(1, T+1):
#
#
#     N = int(input())
#     size = 100
#     str_list = [input() for _ in range(size)]
#
#
#     #데이터 전처리! 세로 문을 가로 회문으로 보기 위해서!
#
#     for i in range(size):
#         temp = "" #세로 하나 보고 넣어야 해서!
#         for j in range(size):
#             temp += str_list[j][i]
#
#         str_list.append(temp) #세로 다 돌았어! 긔럼 넣어야지!
#
#
#     ans = 0
#
#     for M in range(size, 1, -1): #100개 부터 하나씨 주는 M 가장 큰것을 찾기 위함!
#
#         for str_temp in str_list:
#
#             for i in range(size - M + 1):
#
#                 temp = str_temp[i: i + M] #인덱싱이라서 값이 다 들어감!
#
#                 if temp == temp[::-1]:
#                     ans = M
#
#     print("#{} {}".format(tc, ans))


