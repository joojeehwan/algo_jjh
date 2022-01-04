
data = input()

# 첫 번째 문자를
0
res = int(data[0])

for i in range(1, len(data)):

    # 두 수 중에 하나라도 0 혹은 1 이면 + 를 한다!
    num = int(data[i])

    if res <= 1 or num <= 1 :
        res += num


    else:
        res *= num


print(res)