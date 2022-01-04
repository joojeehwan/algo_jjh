

n, m = map(int, input().split())

if n <= 0 or n > 100 or n % 2 == 0:
    print("INPUT ERROR!")

else:


    if m == 1:

        #중간까지는 늘었다가 그 이후부터 줄었다가,,!
        for i in range(1, n//2+1):

            for j in range(0, i):
                print("*", end= "")

            print()

        # 중간 이후

        for i in range(0, n//2+1):

            for j in range(n//2-i, -1, -1):

                print("*", end= "")

            print()


    elif m == 2:
        #1번의 모양을 끝에서 부터 한다
        for i in range(1, n//2 + 1):

            for j in range(n//2-i+1):
                print(" ", end= "")

            for k in range(i):
                print("*", end="")
            print()
        #중간 이후
        for i in range(0, n//2 + 1):

            for j in range(i):
                print(" ", end="")

            for j in range(n // 2 - i, -1, -1):
                print("*", end="")

            print()

    elif m == 3 :

        for i in range( n // 2 + 1):

            for j in range(i):
                print(" ", end = "")

            for k in range(n-i*2):
                print("*", end = "")

            print()
        # 중간 이후
        for i in range(1, n // 2 + 1):

            for j in range(n //2 - i):
                print(" ", end="")

            for j in range(i*2+1):
                print("*", end="")

            print()



    elif m == 4:

        for i in range(n // 2 + 1):
            for j in range(i):
                print(" ", end= "")

            for k in range(n//2-i+1):
                print("*", end="")

            print()


        for i in range(1, n // 2 + 1):
            for j in range(n//2):
                print(" ", end="")

            for j in range(i+1):
                print("*", end="")

            print()








