'''


용액

결국 리스트안에서 2개의 값을 더해서 0에 가장 가까운 값을 구하라는 이야기!

투 포인터?!,,, 투 포인터가 뭐더라,, 인덱스 2개로 탐색하는 그런거엿나,,?!

입력이 오름차순정렬?! => 투 포인터 아주 쓰기 좋은 날이구먼,,

,,

0에 가장 가까원 지는 2개의 값의 인덱스를 반환하면 된다.

2개의 값의 차이가 가장 작아지는 부분의 인덱스를 저장하는 거! 변수 필요!

양수가 되면 값이 작아져야 하니깐 오른쪽에 있는 인덱스를 왼쪽으로 한칸
음수가 되면 값이 커져야 하니깐 왼쪽에 있는 인덱스를 오른쪽으로 한칸


이거 근데 이분탐색으로 풀 수 있음???!!

'''

# N = int(input())
#
# #이미 정렬되어 있게 들어온다.
# lst = list(map(int, input().split()))
#
# start = 0
#
# end = N - 1
#
# min_value = 1100000000000000000
#
#
# index_left = 0
#
# index_right = 0
#
# while start < end:
#
#     SUM = lst[start] + lst[end]
#
#     if abs(SUM) < min_value:
#
#         index_left = start
#
#         index_right = end
#
#         min_value = abs(SUM)
#
#     if SUM < 0:
#         start += 1
#
#     else:
#         end -= 1
#
# # print(lst[start], lst[end]) # 아 이러니깐 답이 안나오지,,!
# print(lst[index_left], lst[index_right])



#이분 탐색,,!

def binary_search(arr, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환!
    if arr[mid]  == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, end)


# 투 포인터 구현

arr = [3, 9, 25, 22, 1, 6, 5, 11, 19, 28, 17, 12, 16] # 주어진 배열. 중복 수 없음
S = 23 # 목표 합계

arr.sort()
l, r = 0, len(arr) - 1
while l <= r:
    if arr[l] + arr[r] > S:
        r -= 1
    elif arr[l] + arr[r] < S:
        l += 1
    elif arr[l] + arr[r] == S:
        print(l, '번째 수 (', arr[l], ') + ', r, '번째 수 (', arr[r], ')')
        # 또 찾아라 이 자식들아! 
        r -= 1
        l += 1






#이코테
# n = 5 # 데이터의 개수 N
# m = 5 # 찾고자 하는 부분합 M
# data = [1, 2, 3, 2, 5] # 전체 수열
#
# count = 0
# interval_sum = 0
# end = 0
#
# # start를 차례대로 증가시키며 반복
# for start in range(n):
#     # end를 가능한 만큼 이동시키기
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1
#     # 부분합이 m일 때 카운트 증가
#     if interval_sum == m:
#         count += 1
#     interval_sum -= data[start]
#
# print(count)