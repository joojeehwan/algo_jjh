

n, m = map(int, input().split())

if n > 100 or m > 3 or n < 1 or m < 1:
    print("INPUT ERROR!")

else:

    if m == 1:
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end = "")
            print()

    elif m == 2:
        for i in range(n, -1, -1):
            for j in range(i):
                print("*", end = "")
            print()

    else:

        for i in range(1, n+1):

            for j in range(1, n-i+1):
                print(" ", end= "")

            for k in range(1, 2*i):
                print("*", end="")

            print()



