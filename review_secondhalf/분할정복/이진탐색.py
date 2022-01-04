#이진 탐색 구현하기

'''

이진탐색을 구현하자!

서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.
=> def 이진탐색(배열, 값)을 만들어서 배열에 A배열 넣고, 값에다가 for문으로 B의 값을 넣으면 된다.


근데 조건이

양쪽 구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 함,,!
=> 플래그를 사용하면서!

반복문을 돌리면서 양쪽을 번갈아 이동하는 친구를 찾앗을 때 TRUE값을 반환하는 이진 탐색 함수를 만들자!
아니면 FALSE

True의 갯수만 세면 되자나!
'''


# def bibary_sarch

def binary_search(A, value):
    start = 0
    end = len(A) - 1
    flag = 1
    # 1 : 아직 아무것도 안고른 상태
    # 0 : 왼쪽 구간을 고른 상태
    # 2 : 오른쪽 구간을 고른 상태

    #l ~ r 반복문으로 구현!

    while start <= end: #범위가 정상적이라면!
        mid = (start + end) // 2

        #애는 이제 오른쪽을 탐색하게 되는데! 따라서 전애는 왼쪽을 탐색하는 친구가 와야 하니깐!
        if A[mid] < value and flag <= 1 :
            start = mid + 1
            flag = 2 #이제 오른쪽 구간을 탐색하니깐!
        #애는 이제 왼쪽을 탐색하게 되는데 따라서 전에는 오른쪽을 탐색하는 친구과 와야 해!
        elif A[mid] > value and flag >= 1 :
            end = mid - 1
            flag = 0

        elif  A[mid] == value:
            return True

        else:
            return False

    return False

T = int(input())


for tc in range(1, T+1):

    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    ans = 0

    for value in B:
        if binary_search(A, value):
            ans += 1

    print(f"#{tc} {ans}")

