

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
