

T = 10


for tc in range(T):

    dumps = int(input())

    boxes = list(map(int, input().split()))
    
    
    #counts 리스트 만들기!
    #어떤 높이가 몇개 있는지 세어둔 리스트,,!

    counts = [0] * 101

    #index가 높이, value : 해당 높이가 몇개 있는가?

    max_height = 0 # 최대 높이
    min_height = 101 # 최소 높이

    for box in boxes :

        counts[box] += 1

        if max_height < box :
            max_height = box
        if min_height > box :
            min_height = box


        for i in range(dumps):
            counts[max_height] -= 1 #이것이 밑으로 내려간다 생각
            counts[max_height -1] += 1
            counts[min_height] -= 1 #이것이 올라간다고 생각
            counts[min_height +1] += 1

            if counts[max_height] == 0:
                max_height -= 1

            if counts[min_height] == 0:
                min_height += 1


        ans = max_height - min_height
        print("#{} {}".format(tc + 1, ans))

T = 10
for tc in range(1, T + 1):

    N = int(input())
    res = list(map(int, input().split()))

    for _ in range(N):

        max_val_idx = res[0]
        min_val_idx = res[0]

        for i in range(len(res)): #최대 값의 인덱스를 구한다!

            if res[max_val_idx] < res[i]:
                max_val_idx = i

            if res[min_val_idx] > res[i]:
                min_val_idx = i

        res[max_val_idx] = res[max_val_idx] - 1 #최댑갓의 값을 빼고
        res[min_val_idx] = res[min_val_idx] + 1 #최소값을 값을 증가!

        # print(res)
        # print(res[max_val_idx], res[min_val_idx])

    max_val = res[0] #그 다음 최고값과 최고 값을 구한다!
    min_val = res[0]

    for i in range(len(res)):

        if max_val < res[i]:
            max_val = res[i]
        if min_val > res[i]:
            min_val = res[i]

    print(f"#{tc} {max_val - min_val}")


    