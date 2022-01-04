


import sys

from list_3.list_review import binary_search

sys.stdin = open("binary_search_input.txt")





def binary_search(target, start, end):

    cnt = 0

    while start <= end: #요거를 적는게 중요함,,!
        cnt += 1
        mid = (start + end) // 2

        if mid > target:
            end = mid

        elif mid > target:
            start = mid

        else:
            break

    return cnt



T = int(input())

for tc in range(1, T+1):

    n, m, k = map(int, input().split())


    A = binary_search(m, 1, n)
    B = binary_search(k, 1, n)

    if A > B:
        print(f"#{tc} B")
    elif A < B:
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")