


# for i in range(0):
#     print(i)



n, m  = map(int, input().split())




if n >100 or n % 2==0 or n<1 :
    print("INPUT ERROR!")

else:


    if m == 1:

        cnt = 0

        for i in range(1, n+1):

            if i % 2 == 0:
            #짝수에서 역주행을 하니깐 그걸 구현하기 위헤서!
                cnt += i

            for j in range(i):
                if i % 2 == 0:
                    #짝수번은 역주행이다!
                    print(f"{cnt-j}", end= " ")

                else:
                    cnt += 1
                    print(f"{cnt}", end=" ")

            print()


    elif m == 2:

        for i in range(n + 1):

            for j in range(i):
                print(" ", end=" ")

            for k in range(i * 2, n*2-1):
                print(i, end= " ")

            print()


    elif m == 3:


        #증가
        for i in range(1, n // 2 + 1):

            for j in range(1, i+1):
                print(j, end = " ")
            print()
        #감소
        for i in range(n//2 + 1, -1, -1):

            for j in range(1, i+1):
                print(j, end = " ")
            print()

    else:
        print("INPUT ERROR!")

