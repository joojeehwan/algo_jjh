'''


퀵정렬,,

=> 파티셔닝? 피봇의 위치를 결정 => 피봇 위치에 따라 정렬 알고리즘이 조금씩 바뀜

(피벗 선택 자체의 시간을 1번으로 하기 위해서! 왼쪽, 오른쪽을 선택 하는 것! 1번의 시간 복잡도로! 피벗을 선택)

호올스파티션 : 와일문이 2개 i j가 양뱡향으로 이동 (대표) , 피벗을 가장 왼쪽


루모토 파티션 : for문이 하나네?! (이것도 알면!) 단방향! , 피벗이 가장 오른쪽




큌 정렬"의 핵심 : 기준(피봇)을 정해서 분류

 피본 기준 왼쪽은 피봇 보다 작은애, 오른쪽은 큰애,,!

'''


# 호올스 파티션

#오름차순
def hoare_p(A, start, end):

    #왼쪽값을 피봇

    pivot = A[start]

    #원래 존재하던 위치도 알아야 하기에,,! 그래야 값을 swap 할 수 있자나! 그래서 복사 하는 것!
    left = start #새롭게 할당
    right = end #새롭게 할당

    while left <= right:
        #피벗 보다 큰 데이터를 찾을 때까지 반복
        while left <= right and A[left] <= pivot:
            left += 1

        #피벗 보다 작은 데이터를 찾을 때까지 반복
        while left <= right and A[right] >= pivot:
            right -= 1

        #정상 범위
        if left < right:
            A[left], A[right] = A[right], A[left]

    #정상 범위가 아님! 피벗과 라이트 값을 교환! #원래 있던 start가
    #경계 구역이 정해짐
    A[start], A[right] = A[right], A[start]

    return right #여기에 피벗이 있으니깐! 위에서 니가 바꿧자나!

#내림차순
def hoare_p_desc(A, start, end):

    #왼쪽값을 피봇

    pivot = A[start]

    #원래 존재하던 위치도 알아야 하기에,,! 그래야 값을 swap 할 수 있자나! 그래서 복사 하는 것!
    left = start #새롭게 할당
    right = end #새롭게 할당

    while left <= right:
        #피벗 보다 큰 데이터를 찾을 때까지 반복
        while left <= right and A[left] >= pivot: #여기에 등호만 바꾸면 오름 차순 <-> 내림 차순 체인지 가능
            left += 1

        #피벗 보다 작은 데이터를 찾을 때까지 반복
        while left <= right and A[right] <= pivot:
            right -= 1

        #정상 범위
        if left < right:
            A[left], A[right] = A[right], A[left]

    #정상 범위가 아님! 피벗과 라이트 값을 교환! #원래 있던 start가
    #경계 구역이 정해짐
    A[start], A[right] = A[right], A[start]

    return right #여기에 피벗이 있으니깐! 위에서 니가 바꿧자나!




def loumuto_p(A,start, end):
    pivot = A[end]
    i = start - 1

    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[start], A[end] = A[end], A[start]

    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1


def loumuto_p_desc(A,start, end):
    pivot = A[end]
    i = start - 1

    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            A[start], A[end] = A[end], A[start]

    A[i + 1], A[end] = A[end], A[i + 1]
    return i + 1



def quick_sort(A, start, end):

    if start < end:
        p = hoare_p(A, start, end)
        p_2 = hoare_p_desc(A, start, end)
        p3 = loumuto_p_desc(A, start, end)
        quick_sort(A, start, p3 - 1) #비봇 보다 작은
        quick_sort(A, p3 + 1, end) #피봇 보다 큰




arr = [9,4,0,3,2]
n = len(arr)
quick_sort(arr,0, n-1)

print(arr)




def hoare_p(A, start, end):


    pivot = A[start]

    left = start
    right = end

    while left <= right:

        while left <= right and A[left] <= pivot:
            left += 1

        while left <= right and A[right] >= pivot:
            right -= 1

        if left < right:
            A[left] , A[right] = A[right], A[left]

    A[start], A[right] = A[right], A[start]

    return right



def quick_sort(A, start, end):

    if start < end:

        p = hoare_p(A, start, end)
        quick_sort(A, start, p - 1)  # end가 비봇 보다 작은
        quick_sort(A, p + 1, end)  # start가 피봇 보다 큰


