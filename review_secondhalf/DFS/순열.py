


#단순하게 순열을 생성하는 방법

#회장 1명, 부회장 1명을 뽑는 경우를 순열, 대표 2명을 뽑는 경우를 조합

# 뽑았을 때 순서가 정해져 있는 경우 순열, 뽑았을 떄 순서가 안정해져 있으면 조합

#순열 단순하게 for문을 사용해서 만들기 < - 이건 사전적 순서가 되는구나!
#그걸 다시 2차원 배열로 만들어서 이제 조작하겟지!

lst = []
for i in range(1,4):
    for j in range(1,4):
        if j != i:
            for k in range(1, 4):
                if k != i and k != j:
                    lst.append(i)
                    lst.append(j)
                    lst.append(k)
arr = []

for i in range(0, len(lst), 3):
    temp = [] #잠깐 뜰이 되어주는?!
    for j in range(i, i+3):
        temp.append(lst[j])

    arr.append(temp)


print(lst)
print(arr)


#재귀 호출을 통한 순열 생성(최소한의 변경을 통해서)


#n : 몇개의 수로 순열을 만들지,,!
#k : level => 몇개의 수를 확정 지었는지!
def perm(n, k):


    if k == n:
        print(arr)

        return

    else:
        #k 까지는 확정이니 그 다음부터 고른다.
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n,k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [1,2,3]


perm(3,0)


#visited 배열을 사용한 순열

#n 순열의 크기, k : 결정할 위치
def perm_2(n, k):

    if n == k:
        print(arr)

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1

                perm_lst[k] = arr[i]
                perm_2(n, k+1)

                visited[i] = 0 #다시 돌아와서! 그 값을 사용해야 하니깐! #순열의 경우 순서가 있으니깐! 다른 것들을 또 써여해!

perm_lst = [0] * 3 #3개의 숫자로 순열을 만들어봐

arr = [1,2,3] #숫자 3개를 줄건데

visited = [0] * 3


# 숫자 5개를 주는데 3개를 골라봐

def perm_3(n,m,k):
    if n == k:
        print(perm_lst_2)

    else:
        for i in range(m): #주어진 숫자의 개수만큼
            if visited_2[i] == 0:
                visited_2[i] = 1

                visited_2[k] = arr[i] #값 기록하기!
                perm_3(n, m, k+1)

                visited_2[i] = 0

perm_lst_2 = [0] * 3
arr_2 = [1,2,3,4,5]
visited_2 = [0] * 5
perm_3(3,5,0)

