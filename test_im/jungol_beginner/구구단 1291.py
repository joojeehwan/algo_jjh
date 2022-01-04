



# s, e = map(int, input().split())
#
# if s > e :
#
#     for i in range(s, e-1, -1):
#         for j in range(1,10):
#             print(f"{i} * {j} = {i*j}")
#
#         print()
# else:
#
#     for i in range(s, e+1, 1):
#         for j in range(1,10):
#             print(f"{i} * {j} = {i*j}")
#
#         print()


# 아 이거 출력이 조금 빡세네,,!

def gugudan(n):
    strFormat = '%-1s * %-1s = %+2s' # 이렇게 정렬 하는게 포인트 구나,,!
    s = ''
    start = int(n[0])
    end =0

    FloorValue = 1 #스위치 같이 구구단의 내림차순 오름차순을 결정하는!

    if start == int(max(n)): # 내림차순 구구단
        end = int(min(n))
        FloorValue = -1
    else:                    #오름차순 구구단
        end = int(max(n))

    for i in range(1,10): #실제로 범위만큼 구구단이 이루어지는 현장!
        s =''
        for j in range(int(start),int(end)+FloorValue,FloorValue):
            if int(j) != int(end):
                s += strFormat % (str(j),str(i),str(int(j)*i))+"   "
            else:
                s += strFormat % (str(j), str(i), str(int(j) * i))
        print(s)



while(True):
    isable = True
    result =[]
    data = input().split()

    for j in range(0, len(data)):
        if int(data[j]) <2 or int(data[j])>9:
            print('INPUT ERROR!')
            isable = False
            break
        else:
            if len(result) == 0:
                result.append(data[j])
            else:
                for i in range(0,len(result)):
                    if result[i]!=data[j]:
                        result.append(data[j])

    if len(result)!= 0 and isable:
        gugudan(result)