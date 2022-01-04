

#머지 소트 구현



def merge_sort_desc(arr):
    
    if len(arr) < 2: #1개이거나 0개
        return arr

    mid = len(arr) // 2
    low = merge_sort_desc(arr[:mid]) #왼쪽 부분
    high = merge_sort_desc(arr[mid:]) #오른쪽 부분

    temp = [] # append 방식을 쓰자

    #l : low의 인덱스, h : high의 인덱스, idx : temp의 인덱스
    l = h = 0

    # low와 high를 서로 비교해서 진행, 두 리스트 중 하나라도 다 사용할 때까지
    while l <len(low) and h < len(high): #l과 h의 인덱스가 모두 범위 안에 있으면!

        if low[l] < high[h]: #작은 값을 앞에다 두면서 정렬을 하기 시작
            temp.append(high[h])
            h += 1 #그럼 다음 인덱스를 하나 증가

        else:
            temp.append(low[l])
            l += 1
    #나머지 하나의 리스트를 전부 사용
    while l < len(low): #low쪽이 남았다면 => while을 조건문 처럼 사용!
        temp.append(low[l])
        l += 1
    while h < len(high): #high쪽이 남았다면
        temp.append(high[h])
        h += 1

    return temp


def merge_sort_append(A):
    if len(A) < 2: # 1개거나 0개
        return A
    mid = len(A)//2
    low = merge_sort_append(A[:mid]) # 왼쪽 부분
    high = merge_sort_append(A[mid:]) # 오른쪽 부분

    # if low[len(low) - 1] > high[len(high) - 1]:
    #     global ans
    #     ans += 1

    temp = []
    l = h = 0
    # l : low의 index
    # h : high의 index
    # idx : temp의 index
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            temp.append(low[l])
            l += 1
        else :
            temp.append(high[h])
            h += 1
    # low와 high를 서로 비교해서 진행, 두 리스트 중 하나라도 다 사용할 때까지

    # 나머지 하나의 리스트를 전부 사용
    while l < len(low): # low쪽이 남았다면
        temp.append(low[l])
        l += 1
    while h < len(high) : # high쪽이 남았다면
        temp.append(high[h])
        h += 1

    return temp


lst = [9,4,0,3,2] #오름 차순 정렬

#내림 차순은 어떻게 해?!

arr = merge_sort_desc(lst)

print(arr)


def merge_sort(A):

    if len(A) < 2:
        return A

    mid = len(A) // 2

    low = merge_sort(A[:mid])
    high = merge_sort(A[mid:])

    l = h = 0
    temp = []


    while l < len(low) and h < len(high):

        if low[l] < high[h]:
            temp.append(low[l])
            l += 1

        else:
            temp.append(high[h])
            h += 1

    while l < len(low):
        temp.append(low[l])
        l += 1

    while h < len(high):
        temp.append(high[h])
        h += 1

    return temp
       
