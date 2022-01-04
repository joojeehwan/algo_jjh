



'''



while-else

else절은 break에 의해서



존재 유무는 그 수에서 뺴보면 알 수 있다.




'''




T = int(input())



for tc in range(1, T+1):


    n = float(input())

    ans = ""
    now = 0.5 #1/2
    while n > 0:
        if n >= now: #여기에 = 이거 있어야 대!
            ans += "1"
            n -= now

        else:
            ans += "0"

        now = now / 2 # 그 다음 1/4 1/8을 만들기 위해서!
        if len(ans) >= 13: #2번 케이스의 경우 계속 0이 생겨서,,! 결국엔!
            ans = "overflow"
            break
    print(f"#{tc} {ans}")