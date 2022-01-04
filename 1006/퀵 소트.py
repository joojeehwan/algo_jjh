'''


퀵정렬,,

=> 파티셔닝? 피봇의 위치를 결정 => 피봇 위치에 따라 정렬 알고리즘이 조금씩 바뀜

(피벗 선택 자체의 시간을 1번으로 하기 위해서! 왼쪽, 오른쪽을 선택 하는 것! 1번의 시간 복잡도로! 피벗을 선택)

호올스파티션 : 와일문이 2개 i j가 양뱡향으로 이동 (대표) , 피벗을 가장 왼쪽


루모토 파티션 : for문이 하나네?! (이것도 알면!) 단방향! , 피벗이 가장 오른쪽

이해는 되었다! 실력이 늘었네,, 나도,,



"큌 정렬"의 핵심 : 기준(피봇)을 정해서 분류

 피본 기준 왼쪽은 피봇 보다 작은애, 오른쪽은 큰애,,!

'''


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