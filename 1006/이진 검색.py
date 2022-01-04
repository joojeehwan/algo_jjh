'''


이진 검색

1) 정렬이 되어있어야 함

2) 바이너리 서치 구현 (반복과 재귀로 구현이 가능함)



어떤식으로 이진 검색 알고리즘 문제로 나오나?!(응용 방법 중 하나!)
"백만개의 데이터가 있는데,,, 어떤 수 k가 먗개 있는가?! 이런걸 1000번 물어볼거다!"

=> 1) 백만개 일일이 다,,, 백만 * 1000 => 십억번,, 너무 커!

=> 2) 그래서 나온게 이진검색!! (훨씬 시간이 줄어듬)


"특정숫자가 시작하는 위치와 끝나는 위치를 알면! 그 개숫의 총 갯수를 구할 수 있겠다!"
why? 정렬이 되어있자나!



'''


def binary_search(arr, target, start, end):

    while start <= end:

        mid = (start + end ) // 2

        if arr[mid] == target:
            return mid

        #왼쪽 확인
        elif arr[mid] > target:
            end = mid - 1
        #오른쪽 확인
        else:
            start = mid + 1

    return None


T = int(input())


for tc in range(1, T+1):

    N, M  = map(int, input().split())

    lst_N = list(map(int, input().split()))

    lst_M = list(map(int, input().split()))

    cnt = 0

    for i in range(len(lst_M)):

        if binary_search(lst_N, lst_N[i],0, N-1) == None:
            print("#")





# 이진 탐색

def binary_search(A, value):
    # A라는 배열에서 value를 찾아라
    l = 0
    r = len(A) - 1
    flag = 1
    # 1 : 아직 아무것도 안고른 상태
    # 0 : 왼쪽 구간을 고른 상태
    # 2 : 오른쪽 구간을 고른 상태

    # l~r
    while l <= r: # 범위가 정상적이라면
        mid = (l + r) // 2 # 하나를 예상해서 골라준다.
        if A[mid] < value and flag <= 1: # 고른얘가 찾고자 하는 값보다 작으면 찾을 값은 더 오른쪽에 있다.
            l = mid + 1
            flag = 2
        elif A[mid] > value and flag >= 1: # 고른얘가 찾고자 하는 값보다 크면 찾을 값이 더 왼쪽에 있다.
            r = mid - 1
            flag = 0
        elif A[mid] == value: # 완벽하게 일치한다.
            return True
        else : # 앞에서 고른 구간을 또 고른 상태
            return False
    return False


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    ans = 0
    for value in B:
        if binary_search(A, value):
            ans += 1
    print(f"#{tc + 1} {ans}")