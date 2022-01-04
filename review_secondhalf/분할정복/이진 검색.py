


#이진 탐색 반복문

arr = [9,4,0,3,2]
N = len(arr)
def binart_search_while(arr, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - -1

        else:
            start = mid + 1


    return None



def binary_recurision(arr, target, start, end):
    

    #기저 조건

    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        binary_recurision(arr, target, start, mid - 1)

    else:
        binary_recurision(arr, target, mid + 1, end)
