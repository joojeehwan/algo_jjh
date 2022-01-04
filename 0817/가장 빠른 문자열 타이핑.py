

#완전검색



T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    len_a = len(a)
    len_b = len(b)
    i = 0
    key = 0

    while i < len_a:
        if a[i] == b[0]:
            if a[i:i+len_b] == b:
                key += 1
                i += len_b
            else:
                key += 1
                i += 1
        else:
            key += 1
            i += 1
    print('#{} {}'.format(tc,key))



# while 풀이는 인덱스를 내가 바꾸는 것!


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(T):
    str1, str2 = input().split()
    # banana  bana

    # !...!!
    flag = 0 # 찾았다라는 기록(몇 개의 문자를 건너뛸것인가?)
    ans = 0 # 버튼누른 수
    for i in range(len(str1) - len(str2) + 1):
        if flag != 0:
            flag -= 1
            continue
        cnt = 0
        for j in range(len(str2)):
            if str1[i + j] == str2[j]:
                cnt += 1
        if cnt == len(str2):
            flag = len(str2) - 1
        ans += 1
        # 남은 문자수 : len(str2) - 1
        # 무시해야하는 문자(타이핑 X) : flag
    ans += len(str2) - 1 - flag
    print("#{} {}".format(tc + 1, ans))



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(T):
    str1, str2 = input().split()
    # banana  bana
    i = 0
    ans = 0
    while i < len(str1) - len(str2) + 1:
        # 비교를 시작할 기준점 i
        cnt = 0
        for j in range(len(str2)):
            if str1[i + j ] == str2[j]:
                cnt += 1
        if cnt == len(str2):
            i += len(str2)
        else :
            i += 1
        ans += 1
    #   전체 문자 길이 - 지금 문자 위치 = 남은 문자 개수
    ans += len(str1) - i
    print("#{} {}".format(tc + 1, ans))



    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for tc in range(T):
        str1, str2 = input().split()
        # asdf bana na  bana
        #      i

        i = 0
        ans = 0
        while i < len(str1) - len(str2) + 1:
            # 비교를 시작할 기준점 i
            cnt = 0
            for j in range(len(str2)):
                if str1[i + j] == str2[j]:
                    cnt += 1
            if cnt == len(str2):
                str1 = str1[:i] + "5" + str1[i + len(str2):]
            i += 1
        #   전체 문자 길이 - 지금 문자 위치 = 남은 문자 개수
        ans = len(str1)
        print("#{} {}".format(tc + 1, ans))
