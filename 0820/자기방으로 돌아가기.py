

'''




복도 셋팅 홀수



복도셋팅 짝수



복도를 하나로 만들게 되었고, 이제 작은방에서 큰방으로 가는거나, 큰방에서 작은 방으로 가는 것은 의미가 없게 되었다,


약간 이해가 안가지만! 입력 받는 TIP만 얻어가자!


'''




#약간의 장치,,,! 복도 값으로 다 바꾸어 버린다!


road = [0] * 201 #0번 부터 200번까지 사용해야 하므로!



def div(num):
    return (int(num)+1) // 2



T = int(input())


for tc in range(1, T+1):


    N = int(input())

    students = [list(map(div, input().split())) for _ in range(N)]


    road = [0] * 201


    for i in range(N): #예시가 다 보면 뒤에 값이 작아 보여서 안해도 된다고 생각하지만,,! 이것을 해야함,,! 그래서 ,,,!
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1] + 1):
            road[j] += 1

    print("#{} {}".format(tc, max(road)))







