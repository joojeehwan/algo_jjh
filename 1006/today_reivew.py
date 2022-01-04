

#merge sort

#1개씩 요소가 남을때까지 재귀적으로 나누고
# 그후에 2새씩의 요소들을 반복적으로 merge

# def merge_sort(arr):
#
#
#     if len(arr) <= 1:
#         return arr
#
#
#     mid = len(arr) // 2
#
#     leftlist = arr[:mid]
#     rightlist = arr[mid:]
#
#
#     left = merge_sort(leftlist)
#     right = merge_sort(rightlist)
#     return merge(left, right)
#
#
# def merge(left, right):
#
#     i = 0 #인덱스를 가리키는 포인터 같은 역활
#     j = 0
#
#     sorted_list = [] #정렬할 리스트
#
#     while (i < len(left)) and (j < len(right)):
#
#         if left[i] < right[j]:
#             sorted_list.append(left[i])
#             i += 1
#         else:
#             sorted_list.append(right[j])
#             j += 1
#
#     while (i < len(left)): #와일을 if문 까지 쓸 수 있구나,,
#         #반복 if문이 while같은 느낌인,, 그 i의 조건을,,주면서,,!
#
#         sorted_list.append(left[i])
#         i += 1
#
#     while (j < len(right)):
#         sorted_list.append(right[j])
#         j += 1
#
#     #이런식으로 병합정렬에서 나머지를 넣을 수도 있어!
#     #merged_arr += low_arr[l:]
#     #merged_arr += high_arr[h:]
#     return sorted_list
#
#
#
#
# lst = [9,4,0,3,2]
#
# print(merge_sort(lst))
#
#
# #병합 결과를 담을 새로운 배열을 생성해서 리턴하지 않고, 인덱스 접근을 이용해
# # 입력 배열을 계속해서 업데이트 하면 메모리 사용량을 대폭 줄일 수 있습니다.(in-place sort)
#
#
# def merge_sort_new(arr):
#     def sort(low, high):
#         if high - low < 2:
#             return
#         mid = (low + high) // 2
#         sort(low, mid)
#         sort(mid, high)
#         merge(low, mid, high)
#
#     def merge(low, mid, high):
#         temp = []
#         l, h = low, mid
#
#         while l < mid and h < high:
#             if arr[l] < arr[h]:
#                 temp.append(arr[l])
#                 l += 1
#             else:
#                 temp.append(arr[h])
#                 h += 1
#
#         while l < mid:
#             temp.append(arr[l])
#             l += 1
#         while h < high:
#             temp.append(arr[h])
#             h += 1
#
#         for i in range(low, high):
#             arr[i] = temp[i - low]
#
#     return sort(0, len(arr))
#
# arr2 = [8,4,1,9,3,2]
#
# print(merge_sort_new(arr2))



# def merge_sort(arr):
# 
#     if len(arr) < 2:
#         return arr
# 
# 
#     mid = len(arr) // 2
#     low = merge_sort(arr[:mid])
#     high = merge_sort(arr[mid:])
# 
# 
#     temp = [-1] * len(arr)
# 
#     l = h = idx = 0
# 
#     while l < len(low) and h < len(high):
#         if low[l] < high[h]:
#             temp[idx] = low[l]
#             l += 1
# 
#         else:
#             temp[idx] = high[h]
#             h += 1
# 
#         idx += 1
# 
# 
#     while l < len(low):
#         temp[idx] = low[l]
#         l += 1
#         idx += 1
# 
#     while h < len(high):
#         temp[idx] = high[h]
#         h += 1
#         idx +=1
# 
#     return temp
# 
# 
# def merge_sort_append(arr):
# 
#     if len(arr) < 2:
#         return arr
# 
# 
#     mid = len(arr) // 2
#     low = merge_sort(arr[:mid])
#     high = merge_sort(arr[mid:])
# 
# 
#     # 이 부분이 달라진다!
#     # temp = [-1] * len(arr)
#     #
#     # l = h = idx = 0
# 
#     temp = []
#     l = h = 0
# 
#     while l < len(low) and h < len(high):
#         if low[l] < high[h]:
#             temp.append(low[l])
#             l += 1
# 
#         else:
#             temp.append(low[h])
#             h += 1
# 
#     while l < len(low):
#         temp.append(low[l])
#         l += 1
# 
#     while h < len(high):
#         temp.append(low[h])
#         h += 1
# 
#     return temp
# 
# lst = [8,7,3,1,5,9]
# 
# 
# a = merge_sort(lst)



#퀵 정렬

#hoare-partition 알고리즘



# def quick_sort(arr, left, right):
#
#     if left >= right:
#         return
#
#     p = partition_hoare(arr, left, right)
#     #p = partition_loumuto(arr, left, right)
#
#     quick_sort(arr, left, p - 1)
#     quick_sort(arr, p + 1, right)
#
#
# def partition_hoare(arr, left, right):
#
#     pivot = arr[right]
#     p = right
#
#     right -= 1
#
#
#     while left <= right:
#         while arr[left] < pivot:
#             left += 1
#
#         while arr[right] > pivot:
#             right -= 1
#
#         if left <= right :
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#
#
#     arr[left],arr[p] = arr[p], arr[left]
#     return left
#
#
#
# def partition_loumuto(arr, left, right):
#d
#     pivot = arr[right]
#     i = left - 1
#
#     for j in range(left, right):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i+1], arr[right] = arr[right], arr[i + 1]
#
#     return i + 1

#이진 검색 구현


# def binary_search(arr, target, start, end):
#
#     while start <= end:
#
#         mid = (start + end) // 2
#
#         if arr[mid] == target:
#             return mid
#
#         elif arr[mid] > target:
#
#             end = mid - 1
#
#         else:
#             start = mid + 1
#
#     return None

#재귀 구조

# def binary_search_recursion(arr, target, start, end):
#
#
#     if start > end:
#        return None
#
#     mid = (start + end) // 2
#
#     if arr[mid] == target:
#         return mid
#
#     elif arr[mid] > target:
#
#         return binary_search_recursion(arr, target, start,mid - 1)
#
#     else:
#         return binary_search_recursion(arr, target, mid + 1, end)



#부분 집합의 합이 10이 되는 방법 찾기

# def dfs(now = 0, sum = 0, path = []):
#
#     #now
#     if sum == 10:
#         ans_set.add(tuple(path))
#         return
#
#     #가지치기 2가지 방법..
#
#     #합이 10을 넘으면 굳이 할 필요가 없자나!
#     if sum > 10:
#         return
#     #배열의 끝까지 탐색하면 그것도 종료
#     if now == len(arr):
#         return
#
#     #1. now를 사용한다.
#
#     if sum + arr[now] <= 10:
#         dfs(now + 1, sum + arr[now], path + [arr[now]])
#
#     #2 now를 사용하지 않는다.
#     dfs(now + 1, sum , path)
#
#
#
#
#
# arr = [1,2,3,4,5,6,7,8,9,10]
#
#
# #중복되는 값을
# ans_set = set()
#
# dfs()
#
# for ans in ans_set:
#     print(ans)

#트리 입력 정리


'''

3 1
3 5 
1 2
1 4 

큰 방법은 두가지, 리스트 형태로 받을것인가, 격자로 하나로 받을 것인가

'''


#1 방법 1 격자로

# n = 5
#
# graph1 = [[0] * (n + 1) for _ in range(n + 1)]
#
#
#
# for i in range(4):
#     frm, to = map(int, input().split())
#     graph1[frm][to] = 1
#
#
# print(graph1)


#리스트로

# n = 5
# #보통 트리가 0번 인덱스를 사용하지 않고
# # 1부터 n번까지 사용하기 때문에 이렇게 사용 
# graph2 = [[] for _ in range(n + 1)]
# 
# for i in range(4):
#     frm, to = map(int, input().split())
#     graph2[frm].append(to)
# 
# print(graph2)



#이진트리에서 레프트 라이트가 주어질 때
# n = 5
# #보통 트리가 0번 인덱스를 사용하지 않고
# # 1부터 n번까지 사용하기 때문에 이렇게 사용
# graph3_tree = [[0] * 2 for _ in range(n + 1)]
#
# for i in range(4):
#     frm, to, pos = map(int, input().split())
#     if pos == 1:
#         graph3_tree[frm][0] = to
#
#     elif pos == 2:
#         graph3_tree[frm][1] = to
#
# print(graph3_tree)


#부모를 저장
import sys

N = 5

# #0번 노드는 없으니깐! 보통 -1로 안쓰는 것을 표현
# tree2 = [0] + [-1] * N
#
# for i in range(4):
#     frm, to = map(int, input().split())
#     tree2[to] = frm
#
#
# print(tree2)

#자식을 저장
# tree3 =  [-1] * (N + 1)
#
# '''
#
# 1 3
# 2 1
# 3 5
# 4 2
# 5 4
#
# '''
#
#
# for i in range(5):
#     index, val = map(int, input().split())
#     tree3[index] = val
#
# print(tree3)

#색종이 만들기

import sys



ans_white = 0
ans_blue = 0


# def check(row, col, size):
#     for r in range(row, row+size):
#         for c in range(col, col + size):
#             if MAP[row][col] != MAP[r][c]:
#                 return False
#
#     return True
#
#
# def func(row, col, size, div = 2):
#     global ans_blue
#     global ans_white
#     c = check(row, col, size)
#
#     if c:
#         if MAP[row][col] == 1:
#             ans_blue += 1
#
#         elif MAP[row][col] == 0:
#             ans_white += 1
#
#     else:
#         for nr in range(row, row + size, size//div):
#             for nc in range(col, col + size, size//div):
#                 func(nr, nc, size//div)
#
# n = int(input())
# MAP = [list(map(int, sys.stdin.readline().split()) for _ in range(n))]
#
# func(0, 0, n)
#
# print(ans_blue)

# import sys
#
# N = int(sys.stdin.readline())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# white = 0
# blue = 0
#
#
# def partition(x, y, n):
#     global blue, white
#     check = board[x][y]
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if check != board[i][j]:
#                 partition(x, y, n // 2)  # 1사분면
#                 partition(x, y + n // 2, n // 2)  # 2사분면
#                 partition(x + n // 2, y, n // 2)  # 3사분면
#                 partition(x + n // 2, y + n // 2, n // 2)  # 4사분면
#                 return
#     if check == 0:
#         white += 1
#         return
#     else:
#         blue += 1
#         return
#
#
# partition(0, 0, N)
# print(white)
# print(blue)


#N-queen

#교수님 풀이 review

def dfs(now):

    if now >= N:

        global ans
        ans += 1
        print(f"------{ans}------")
        for row_MAP in MAP:
            print(row_MAP)
        print()
        return

    for col in range(N):
        if check_col[col]:
            continue

        if check_ru_ld[now + col]:
            continue

        if check_lu_rd[now - col]:
            continue

        check_col[col] = True
        check_ru_ld[now + col] = True
        check_lu_rd[now - col] = True
        MAP[now][col] = 1
        dfs(now + 1)

        MAP[now][col] = 0
        check_col[col] = False
        check_ru_ld[now + col] = False
        check_lu_rd[now - col] = False




N = int(input())

check_col = [False] * N
check_ru_ld = [False] *(2 * N + 1)
check_lu_rd = [False] *(2 * N + 1)
ans = 0
MAP = [[0] * (N) for _ in range(N)]

dfs(0)