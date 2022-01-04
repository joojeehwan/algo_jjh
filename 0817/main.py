


import sys

sys.stdin = open("main_input.txt")



TC = int(input())

for tc in range(1, TC+1):


    str1 = input()
    str2 = input()

    count = 0
    for st2 in str2:
        for st1 in str1:
            if st1 == st2:
                count += 1
                break
        if count == len(str1):
            break

    if count == len(str1):
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")

        #이건 아마 완전 탐색이 아니리서!


#이건 문자를 찾는것!
T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    flag = 0  # 찾았는지 기록

    for i in range(len(str2) - len(str1) + 1):
        # 기준점 잡기
        cnt = 0
        for j in range(len(str1)):
            if str1[j] == str2[i + j]:
                cnt += 1
        if cnt == len(str1):
            flag = 1
    print("#{} {}".format(tc + 1, flag))