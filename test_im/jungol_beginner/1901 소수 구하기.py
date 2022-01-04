import math
def check_down(num):

    for i in range(num, 0, -1):
        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            numbers.append(i)
            return

def check_up(num):

    for i in range(num + 1, 1000001):
        flag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            numbers.append(i)
            return



T = int(input())

for _ in range(T):

    numbers = []
    N = int(input())

    check_down(N)
    check_up(N)

    if len(numbers) == 1:
        print(numbers[0])

    else:

        if abs(numbers[0] - N) < abs(numbers[1] - N):
            print(numbers[0])

        elif abs(numbers[0] - N) > abs(numbers[1] - N):
            print(numbers[1])

        else:
            print(numbers[0], numbers[1])
