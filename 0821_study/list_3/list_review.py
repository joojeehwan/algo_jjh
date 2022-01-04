

# 지그재그 순회


lst = [list(map(int, input().split())) for _ in range(5)]


lst2 = []

for _ in range(5):

    lst2.appned(list(map(int, input().split())))




M = len(lst[0])
for i in range(len(lst)):

    for j in range(len(lst[i])):

        lst[i][j + (M-1-2*j) * (i % 2)]



# 전내 중요한거 나옴! 델타 배열
#
# 2차원 배열의 한좌펴에서 4방향의 인접 배열 요소를 탐색하는 방법!



N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

#상하좌우 구현
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


#가로 길이
N = len(lst)


#고정 고정 변화,,!
for row in range(N):
    for col in range(N):
        for k in range(4):
            next_row = row + dr[k]
            next_col = col + dc[k]


            #그 다음에 범위를 생각!

            if 0 <= next_row < N and 0 <= next_col < M :
                arr[next_row][next_col]



# 부분집합 만들기 - loop


bit = [1, 2, 3, 4]

for i in range(2) :
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)






arr = [3,6,7,1,5,4]


n = len(arr)


# & 자체가 비트연산을 가능하게 한다! 숫자대 숫자로 보는것이 아니라 2진법으로 나타난 비트
# 끼리의 연산으로 나타내줌!
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=", ")

    print()
print()




# 순차탐색 구현


a = [0,4,1,2,5,9]

def sequentialSearch(a, n, key): #값이 있는 인덱스를 반환
    i = 0
    while i < n and a[i] != key :
        i += 1
    if i < n:
        return i #while문에서 걸러지지 못한 인덱스 i가 나온다!
    else:
        return -1


def sequentialsearch2(a, n, key):
    i = 0
    i += 1 #요게가 큰 조건! 더이상 검색을 하지 않게끔 한느!
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i  # while문에서 걸러지지 못한 인덱스 i가 나온다!
    else:
        return -1

def sequentialSearch_for(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i

    return -1






print(sequentialsearch2(a, len(a), 9))



# 이진 탐색 구현 => 정렬이 필수!



#반복문 스타일
def binary_search(array, target, start, end):
    cnt = 0
    while start <= end: #재귀와 다른점!
        cnt += 1
        mid =(start + end) // 2
        if array[mid] == target:
            return (mid, cnt)

        elif array[mid] > target:
            end  = mid - 1

        else:
            start = mid + 1

    return None




#재귀 함수 버젼, 이진 탐색 소스 코드

def binary_search_j (array, target, start, end):



    #값을 찾지 못한 경우를 생각!
    if start > end:
        return None


    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search_j(array, target, start, mid -1)

    else:
        return binary_search_j(array, target, mid + 1, end)



'''

선택 정렬

:주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식,,! 

=> 가장 작은 데이를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 
번째 데이터와 바꾸는 과정을 반복하면 어떨까?

=> 가장 원시적인 방법,, ! 매번 가장 작은 것을 선택!


'''



array = [7, 5, 9, 0, 3 ,1 ,6, 2, 4, 8]


#i값 고정, 그 후에 j로 탐색!
for i in range(len(array)):

    min_idx = i #가장 작은 원소의 인덱스 가 맨앞이라고 가정했기 때문에,,!

    #i + 1의 이유
    for j in range(i+1, len(array)): #앞의 값을 하나 고정하고 그 다음 부터 검색 돌기 위해서!
        if array[min_idx] > array[j]:
            min_idx = j

    #한 바퀴 검색했으면 가장 작은 것을 앞에다가 고정해주어여 하니깐!
    array[i], array[min_idx] = array[min_idx], array[i]

'''
for index in range(N):
    min_value = 2135467890
    found = 0
    for i in range(index, N):
        if min_value > nums[i]:
            min_value = nums[i]
            found = i
nums[index], nums[found] = nums[found], nums[index]

#2개는 같지만 스타일 차이! 

'''






print(array)



#셀렉션 알고리즘

def select(list, k):

    for i in range(0, k):
        min_idx = i
        #이건 고정이 아니라 탐색의 for라서 배열을 끝까지 봐야한다!
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
            list[i], list[min_idx] = list[min_idx], list[i]

        return list[k-1]





