from _ast import stmt

T = int(input())




for tc in range(1, T+1):
    st_r = list(input())
    ans = 0
    cnt = 0
    l = len(st_r)
    i = 0

    while i < l :

        if st_r[i] =="(" and st_r[i+1]==")":
            cnt += ans
            i += 2

        elif st_r[i] == "(":
            ans += 1
            i += 1

        else:
            cnt += 1
            ans -= 1
            i += 1


    print(f"#{tc} {cnt}")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(T):
    str1 = input()
    cnt = 0 # 현재까지의 막대기 개수
    ans = 0 # 답의 개수(완성된 막대기의 개수)
    flag = 0 # 레이저 사용여부
    for i in range(len(str1)):
        if flag == 1:
            flag = 0 #다시 0으로 만들고!
            continue # 레이저를 사용했었으면 무시
        if i != len(str1) - 1 and str1[i] == "(" and str1[i + 1] == ")":
            # 레이저가 쏴지는 지점
            ans += cnt
            flag = 1 # 레이저를 사용했다.
        elif str1[i] == "(":
            # 막대기가 시작하는 지점
            cnt += 1
        else :
            # 막대기가 끝나는 지점
            ans += 1
            cnt -= 1
    print("#{} {}".format(tc + 1, ans))