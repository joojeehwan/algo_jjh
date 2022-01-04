
# 버블 소트


def sort(arr):
    for i in range(len(arr) - 1, 0 , -1):

        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[ j +1] = arr[ j +1], arr[j]

    return arr



T = int(input())


for tc in range(1, T+1):

    N, M, K = map(int, input().split())

    lst = list(map(int, input().split()))

    sorted_arr = sort(lst)

    cnt = 0
    result = 1
    #손님이 도착했을 떄의 시간에 붕어빵이 몇 개 존재 하는지 파악,,!
    #0개 이하로 있다면 팔 수가 없어,,!

    for t in sorted_arr:
        b = (t // M) * K
        if b - cnt <= 0:
            result = 0
            break
        else:
            cnt += 1
    if result:
        print('#{} Possible'.format(tc))
    else:
        print('#{} Impossible'.format(tc))




#처리 라기 전에 전처리 과정이 필요 할 수도 있다,,! 정렬!

# 무조건 입력을 받았다고 해서 그대로 사용하지 말것!

#데이터가 의미하는 바가 무엇일까?!




#im 시험 볼떄 내장 함수 오지게 쓰자,,! 봉인 해제!

T = int(input())


for tc in range(1, T+1):

    N, M, K = map(int, input().split())

    guest = list(map(int, input().split()))

    guest.sort()

    for i in range():
        tg = i + 1#손님의 수
        tb = (guest[i]//M) + K #guest[i]초 안에 만들 수 있는 붕어빵의 수
        if tg > tb :
            result = "Imposible"
            break


        else:
            result = "가능"
