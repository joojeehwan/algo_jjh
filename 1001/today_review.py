



#반복을 이용한 선택정렬



def selectioSort(arr):

    n = len(arr)

    for i in range(0, n-1): # 맨 끝인 n-1 인덱스 까지 하는게 아니라 그 하나 앞까지 함! 이미 거기까지 하면 교환은 다 이루어 졌기 떄문에
        min_idx = i # 처음 인덱스가 가장 작다고 가정하고,

        for j in range(i+1, n): #기준 인덱스 다음 부터 값을 비교하면서 최소값을 찾는다
            if arr[j] < arr[min_idx]:
                min_idx = j

        #포문이 끝나서 기준 인덱스 이후에서 가장 작은 인덱스를 찾게 되면 그 최소값을 맨 앞으로  인덱스를 체인지

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


arr = [7,5,1,4,3,2,6]


selectioSort(arr)

print(arr)


# selectionsort를 재귀적 알고리즘으로 작성

def selecionsort(arr, k): #k는 index

    n = len(arr)

    if k == n-1: #근데 그 k값이 맨 마지막까지 가면 재귀를 종료,,
        return

    min_idx = k
    for i in range(k, n):
        if arr[min_idx] > arr[i]:
            min_idx = i

    arr[k], arr[min_idx] = arr[min_idx], arr[k]

    selecionsort(arr, k+1) #for문에서 k값이 앞으로 한칸씩 움직이는 재귀를 만들려고!


arr = [7,5,1,4,3,2,6]

selecionsort(arr, 0)

print(arr)







'''

재귀 함수의 구성,,

=> dfs(now) :

    if 종료조건:(베이스 케이스)
        return

    dfs(now + 1) (인덕티브 케이스)



보통 문제에 나오는 형태는,,!

def f(n, k) :

    if n == k:
        return


    f(n+1, k)
    
배열의 총개수 n , 배열의 K번째 인덱스

'''

#2제곱 연산 재귀와 반복으로 만들어보기



# def power_2 (k):
#
#     if k == 0:
#         return 1
#
#     else:
#         return 2 * power_2(k-1)
#
#
#
# def power_of_2(k):
#
#     #이건 와일문으로 구성하는게 좋구만,,!
#     #값이 어떤 목표를 향해 가고 있으니깐!
#     i = 0
#     power = 1 #곱 하는 값의 초기 값은 1로 한다!
#     while i < k:
#         power = power * 2
#         i += 1
#
#     return power
'''

베이비 진 문제

고지식한 방법(Bruete-force 탐색) 순차탐색


'''

# def squentialsearch(arr, k):
#
#     i = 0
#     while i < len(arr):
#         if arr[i] == k:
#             return arr[i]
#
#         i +=1
#
#     return -1
#
#
#
# lst = [4,5,6,7,8,9]
#
# a = squentialsearch(lst, 0)
# print(a)


'''

순열, 조합, 부분집합 => 완전 검색

'''


#순열 단순하게 for문을 사용해서 만들기 < - 이건 사전적 순서가 되는구나!
#그걸 다시 2차원 배열로 만들어서 이제 조작하겟지!

# lst = []
# for i in range(1,4):
#     for j in range(1,4):
#         if j != i:
#             for k in range(1, 4):
#                 if k != i and k != j:
#                     lst.append(i)
#                     lst.append(j)
#                     lst.append(k)
#
# arr = []
#
# for i in range(0, len(lst), 3):
#     temp = [] #잠깐 뜰이 되어주는?!
#     for j in range(i, i+3):
#         temp.append(lst[j])
#
#     arr.append(temp)
#
#
# print(lst)
# print(arr)

# 재귀 호출을 통한 순열 생성

def perm(n, k):
    if k == n:
        print(p)

        return

    else:

        for i in range(k, n): #K까지는 확정이니 그 다음부터 고른다!
            p[k], p[i] = p[i], p[k]
            perm(n, k+1) # 그 찾고자 하는 k자리 그 오른쪽 자리를 보아라!
            p[k], p[i] = p[i], p[k]



#교환을 해서 이게 사전적 순서대로 안되는 것!
p = [1,2,3]

perm(3,0)