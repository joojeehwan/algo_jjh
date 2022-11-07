'''

아마존 인터뷰


찾고자 하는 값이 중간점하고 동일하다고 가정하고 프로그래밍

'''



#이진 탐색 소스 코드 구현(재귀 함수)


def binary_search(arr, start, end):


    #오름차순이기에 있을 수 없음! 
    if start > end:
        return None

    mid = (start + end) // 2
    
    #고정점을 찾은 경우 인덱스 반환
    if arr[mid] == mid:
        return mid
    
    #중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif arr[mid] > mid:
        return binary_search(arr, start, mid-1)
    
    #중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(arr, mid + 1, end)


n = int(input())

arr = list(map(int, input().split()))

#이진 탐색 수행
#인덱스값이니깐 0부터 n-1을 넣는다!
index = binary_search(arr, 0, n-1)

#고정점이 없는 경우 -1을 출력
if index == None:
    print(-1)

else:
    print(index)

