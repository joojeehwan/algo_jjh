


T = int(input())


for tc in range(1 , T+1):

    str1 = input()
    cnt = 0 #현재 까지의 막대기 개수

    ans = 0 #답의 개수(완성된 막대기의 개수)
    
    flag = 0 #레이저 사용여부

    for i in range(len(str1)):
        if flag == 1:
            flag = 0 #다시 0으로 만들고!
            continue # 레이저를 사용했었으면 무시

        if i != len(str1) - 1 and str1[i] == "(" and str1[i+1] == ")":
            ans += cnt
            flag = 1

        elif str[i] == "(" :
            cnt += 1

        else :
            ans += 1
            cnt -= 1
    print("#{} {}".format(tc, ans))
