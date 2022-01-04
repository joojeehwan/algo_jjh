

n = int(input())

if n <= 0 or n > 100 or n % 2 == 0:
    print("INPUT ERROR!")


else:

    for i in range(n//2 + 1):


        for j in range(i):
            print(" ", end= "")

        for k in range(i*2+1):
            print("*", end="")

        print()

    for i in range(n//2):

        for j in range(n // 2 - i-1):

            print(" ", end="")

        for k in range(n, i*2+2, -1):
            print("*", end="")

        print()