import sys

sys.stdin = open('input_5205.txt', 'r')


def hoare_p(A, l, r):
    # 왼쪽값을 피봇
    pivot = A[l]

    #이렇게 새로운 변수에 저장하는 이유는?!
    #원래 있던 위치도 알아야 마지막에 값을 swap 할 수 있기 때문이다. 
    i = l #인덱스 값 i
    j = r #인덱스 값 j

    while i <= j:
        while i <= j and A[i] <= pivot: i += 1  # 피봇보다 큰 값을 만날때 까지 이도옹
        while i <= j and A[j] >= pivot: j -= 1  # 피봇보다 작은 값을 만날때 까지 이도옹

        #정상 범위
        if i < j:
            A[i], A[j] = A[j], A[i]

    #정상 아님! 피벗과 라이트 값을 교환
    # 경계구역이 정해짐
    A[l], A[j] = A[j], A[l]

    return j


def loumuto_p(A, l, r):
    pivot = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, l, r):
    if l < r:
        # p = hoare_p(A, l, r)
        p = loumuto_p(A, l, r)
        quick_sort(A, l, p - 1)  # 피봇보다 작은
        quick_sort(A, p + 1, r)  # 피봇보다 큰


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # N : 100만개

    nums = list(map(int, input().split()))  # 정렬하고 싶은 숫자들

    quick_sort(nums, 0, N - 1)

    print("#{} {}".format(tc, nums[N // 2]))
