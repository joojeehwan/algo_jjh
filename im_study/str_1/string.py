

T = 10
for tc in range(1, T + 1):
    t = int(input())
    patt = input().rstrip()
    text = input().rstrip()

    Tx = len(text)
    P = len(patt)
    cnt = 0

    for t in range(Tx - P + 1):
        flag = 1
        for p in range(P):
            if text[t + p] != patt[p]:
                flag = 0
                break
        if flag:
            cnt += 1

    print('#{} {}'.format(tc, cnt))



#요것은 그 패턴인 문자가 있는데 몇개 있냐? 를 찾는 것!
T = 10

for tc in range(1, T+1):

    T = int(input())
    pattern = input().rstrip()
    text = input().rstrip()

    cnt = 0 # 문자열에서 패턴에 맞는 것이 몇개나 있어?

    for i in range(len(text) - len(pattern) + 1):
        flag = 1

        for j in range(len(pattern)): #플래그가 0이 되면 갯수를 증가 못시키니깐 문자끼리 달라지면 플래그가 0이 되게 만든다!
            if pattern[j] != text[i + j]:
                flag = 0
                break #문자가 하나라도 다르면 더 볼필요 없이 다음 text의 다음문자랑 비교 하기위함!
        if flag:
            cnt += 1

    print('#{} {}'.format(tc, cnt))


#이건 그 패턴인 문자가 있냐?를 찾는것!
T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    flag = 0  # 찾았는지 기록

    for i in range(len(str2) - len(str1) + 1):
        # 기준점 잡기
        cnt = 0 #  텍스트의 일정 문자열이 패턴의 문자열 길이와 같은지 비교,, 같이 같다면 cnt를 증가 시켜서 만약에
        #cnt가 패턴의 길이와 같으면 해당 패턴이 문자열에 있음을 확인
        for j in range(len(str1)):
            if str1[j] == str2[i + j]:
                cnt += 1
        if cnt == len(str1):
            flag = 1
    print("#{} {}".format(tc + 1, flag))