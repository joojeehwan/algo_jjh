
import sys

sys.stdin = open("pali_input.txt")



T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]
    for i in range(N):
        # i : 가로 기준점
        temp = ""
        for j in range(N):
            # j : 세로 줄 번호
            temp += str_list[j][i]
        str_list.append(temp)
    ans = ""
    for str_temp in str_list: #문자열이 하나씩 들어오니깐!
        for i in range(N - M + 1):
            temp = str_temp[i:i + M] # i~i+M-1 <- M개의 길이 문자열
            #회문 : 앞에서 부터 읽은 문자열 == 뒤에서 부터 읽은 문자열
            cnt = 0
            for j in range(len(temp) // 2):
                if temp[j] == temp[len(temp) -1 -j]:
                    cnt += 1
            if cnt == len(temp) // 2:
                ans = temp
            """
            if temp == temp[::-1]:
                ans = temp
            """
    print("#{} {}".format(tc + 1, ans))


#회문 세로 처리 없이 index로 계산!

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]
    ans = ""
    for row in range(len(str_list)):
        for col in range(N - M + 1):
            temp = str_list[row][col:col + M] # i~i+M-1 <- M개의 길이 문자열
            #회문 : 앞에서 부터 읽은 문자열 == 뒤에서 부터 읽은 문자열
            cnt = 0
            for j in range(len(temp) // 2):
                if temp[j] == temp[len(temp) -1 -j]:
                    cnt += 1
            if cnt == len(temp) // 2:
                ans = temp

        for col in range(N - M + 1):
            #회문 : 앞에서 부터 읽은 문자열 == 뒤에서 부터 읽은 문자열
            cnt = 0
            for j in range(M // 2):
                if str_list[col + j][row] == str_list[col + M - 1 - j][row]:
                    cnt += 1
            if cnt == M // 2:
                ans = temp

            """
            if temp == temp[::-1]:
                ans = temp
            """
    print("#{} {}".format(tc + 1, ans))