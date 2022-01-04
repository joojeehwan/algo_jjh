



# 오 이거 어제 푼 그 풀이랑 비슷하다!? 조건으 주고 그에 맞게 더하는 값을 변화 시키는!



T = 10
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 1
    while True:
        now = data.pop(0)
        now -= cnt
        if now <= 0:
            data.append(0)
            break
        data.append(now)

        cnt += 1 # 1 ~ 5
        if cnt == 6:
            cnt = 1
        de = 1
    print("#{} ".format(tc + 1), end = "")
    for i in data:
        print(i, end = " ")