#선택정렬

#반복문 버젼
# arr = [9,4,0,3,2]
#
# for i in range(len(arr) - 1):
#     min_idx = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#
# def selectioSort(arr):
#
#     n = len(arr)
#
#     for i in range(0, n-1): # 맨 끝인 n-1 인덱스 까지 하는게 아니라 그 하나 앞까지 함! 이미 거기까지 하면 교환은 다 이루어 졌기 떄문에
#         min_idx = i # 처음 인덱스가 가장 작다고 가정하고,
#
#         for j in range(i+1, n): #기준 인덱스 다음 부터 값을 비교하면서 최소값을 찾는다
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#
#         #포문이 끝나서 기준 인덱스 이후에서 가장 작은 인덱스를 찾게 되면 그 최소값을 맨 앞으로  인덱스를 체인지
#
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#
#
# arr = [7,5,1,4,3,2,6]
#
#
# selectioSort(arr)
#
# print(arr)



#재귀 버젼

def selction_sort_recursion(arr, k): #k는 인덱스

    n = len(arr)


    #k값이 맨 마지막 n-1번쨰 인덱스까지 가면 재귀를 종료!
    #종료조건
    if k == n-1 :
        return
    
    min_idx = k

    for i in range(k+1, n): #k
        if arr[min_idx] > arr[i]:
            min_idx = i

    arr[k], arr[min_idx] = arr[min_idx], arr[k]

    selction_sort_recursion(arr, k+1) # 그 다음 k+1을 검사 해봐야 하니깐




arr = [7,5,1,4,3,2,6]

selction_sort_recursion(arr, 0)

print(arr)

