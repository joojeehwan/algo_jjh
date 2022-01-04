





#아스키 코듣로 ! ord함수로 아스키 코드 값을 알 수 있다.


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    res = list(input().split())


    a = ""
    for i in range(len(res)):
        if res[i][0].islower():
           a += res[i][0].upper()

    print(f"#{tc} {a}")


    # print(f"#{tc} ")