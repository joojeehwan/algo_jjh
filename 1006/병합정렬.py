

'''



병합정렬의 스킬을 적용! 

=> 두개의 리스트를 정렬해서 합치고 싶을때!

1) 그냥 2개 합쳐서 정렬! => n로그n 시간이 걸려,,!

2) 병합 정렬 1단계 스킬? n번의 시간만!!! => 이게 훨씬 더 효율적



'''

#일단 merge sort 만들어보기

def merge(left, right):
    arr = list()

    global cnt

    i = 0
    j = 0

    while(i < len(left) or j < len(right)) :

        if i < len(left) and j < len(right):

            if left[i] <= right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1
        elif i < len(left):
                arr.extend(left[i:])
                cnt += 1
                break
        else:
            arr.extend(right[j:])
            break

    return arr
    # while(i<len(left) and j < len(right)):
    #     if left[i] <= right[j]:
    #         arr.append(left[i])
    #         i += 1
    #
    #     else:
    #         arr.append(right[j])
    #         j += 1
    #
    # if i == len(left):
    #     arr = arr + right[j:len(right)]
    # if j == len(right):
    #     arr = arr + left[i:len(left)]
    #
    # return arr


def merge_sort(arr):
    if len(arr) <= 1 :
        return arr

    m = len(arr) // 2

    left = merge_sort((arr[0:m]))
    right = merge_sort(arr[m:len(arr)])
    return merge(left, right)


T = int(input())

for tc in range(1, T+ 1):

    cnt = 0
    N = int(input())

    lst = list(map(int, input().split()))

    ans = merge_sort(lst)

    print(f"#{tc} {ans[N // 2]} {cnt}")



#교수님이 구현한 병합정렬

# 병합 정렬
def merge_sort(A):
    if len(A) < 2: # 1개거나 0개
        return A
    mid = len(A)//2
    low = merge_sort(A[:mid]) # 왼쪽 부분
    high = merge_sort(A[mid:]) # 오른쪽 부분

    if low[len(low) - 1] > high[len(high) - 1]:
        global ans
        ans += 1

    temp = [-1] * len(A)
    l = h = idx = 0
    # l : low의 index
    # h : high의 index
    # idx : temp의 index
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            temp[idx] = low[l]
            l += 1
        else :
            temp[idx] = high[h]
            h += 1
        idx += 1
    # low와 high를 서로 비교해서 진행, 두 리스트 중 하나라도 다 사용할 때까지

    # 나머지 하나의 리스트를 전부 사용
    while l < len(low): # low쪽이 남았다면
        temp[idx] = low[l] # low에 남은 data를 temp에 추가
        l += 1
        idx += 1
    while h < len(high) : # high쪽이 남았다면
        temp[idx] = high[h]
        h += 1
        idx += 1

    return temp


def merge_sort_append(A):
    if len(A) < 2: # 1개거나 0개
        return A
    mid = len(A)//2
    low = merge_sort(A[:mid]) # 왼쪽 부분
    high = merge_sort(A[mid:]) # 오른쪽 부분

    if low[len(low) - 1] > high[len(high) - 1]:
        global ans
        ans += 1

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


t = int(input())

for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    sorted_arr = merge_sort_append(arr)
    de = 1
    print(f"#{tc + 1} {sorted_arr[n//2]} {ans}")



