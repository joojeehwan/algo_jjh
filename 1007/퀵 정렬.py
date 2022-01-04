'''


어느 한 목표를 향해서 가는거라,,!

while이 어울린다,,! 


'''

def quick_sort(arr, start, end):


    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1


        if left > right :
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:
            arr[left], arr[right] = arr[right], arr[left]


    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


T = int(input())


for tc in range(1, T+1):


    N = int(input())

    lst = list(map(int, input().split()))

    quick_sort(lst, 0, len(lst) - 1)

    print(f"#{tc} {lst[N//2]}")
    



#교수님 퀵 소트

# quick 정렬

def quick_sort(A, l, r):
    # A의 l~r범위를 정렬
    if l >= r:
        return
    p = partition(A, l, r)
    # p : pivot의 위치
    quick_sort(A, l, p - 1)
    quick_sort(A, p + 1, r)

def partition(A, l, r):
    # A의 l~r범위를 pivot을 기준으로 분류, pivot의 위치를 반환
    pivot = arr[r]
    p = r
    # 실제로 분류할 범위 : l ~ r-1
    r -= 1

    while l <= r:
        while arr[l] < pivot:
            # 정상인 경우
            l += 1 # 그냥 넘어감
        while arr[r] > pivot:
            r -= 1 # 그냥 넘어감
        # 비정상적인 위치에 해당하는 l, r
        if l <= r : # l과 r의 위치가 정상적이라면
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    arr[l], arr[p] = arr[p], arr[l]
    return l


t = int(input())

for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, n - 1)

