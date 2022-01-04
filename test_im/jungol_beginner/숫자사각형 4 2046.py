#숫자 사각형 재밋구먼!
n, m = map(int, input().split())


if m == 1:

    num = 1
    for row in range(n):
        for col in range(n):
            print(num, end = " ")
        num += 1
        print()

elif m == 2:

    for row in range(n):
        if row % 2 == 0:
            for col in range(n):
                print(col + 1, end = " ")
            print()
        else:
            for col in range(n-1, -1, -1):
                print(col + 1, end = " ")
            print()


else:
    num = 1
    for row in range(n):
        for col in range(num, num * n + 1, num):
            print(col, end = " ")
        num += 1

        print("")

