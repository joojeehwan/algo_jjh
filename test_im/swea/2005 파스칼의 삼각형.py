
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    print(f"#{tc}")
    pa = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(1, i):
            temp += [pa[i - 1][j - 1] + pa[i - 1][j]]
        temp += [1]
        pa.append(temp)

    for p in pa:
        for k in p:
            print(k, end=" ")
        print("")