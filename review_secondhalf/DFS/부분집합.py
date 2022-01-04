


#단순 하게 모든 부분 집합 생성하는 방법


# bit = [0,0,0,0]
#
# for i1 in range(2):
#     bit[0] = i1
#
#     for i2 in range(2):
#         bit[1] = i2
#
#
#         for i3 in range(2):
#             bit[2] = i3
#
#             for i4 in range(2):
#                 bit[3] = i4
#                 print(bit)
#
#
#
#
#
# # 바이너리 카운팅을 통한 부분집합 생성, 비트 연산자로 부분집합 구하기
# #블로그 글 확인하기! 설명이 정말 잘되어있다!
#
#
#
# arr = [4,5,6]
#
# n = len(arr)
#
# for i in range(1 << n): #모든 부분 집합의 갯수들중에서!
#
#     for j in range(n): #arr안에 있는 인덱스 만큼
#
#         if i & (1<<j): #i에 대해서 (1<<j)로 검사 하는 것!
#
#             print(arr[j], end = " ")
#
#     print()


# 재귀로  부분집합 구하기
# 순열의 크기 N
# level, depth, 결정할 위치 k

def subset(n, k):
    if n==k: #순열의 크기 만큼 다 결정했다
        for i in range(n):
            if visited[i] == 1:  #방문했던 녀석들을
                print(arr[i], end=" ")
        print()
    else:
        visited[k] = 1 #방문 했다고 표시
        subset(n, k+1) #재귀속으로 고고!

        visited[k] = 0 #방문 표시 지우고
        subset(n, k+1) #그 다음 재귀하러!


arr = [1,2,3,4]
visited = [0] * len(arr)

subset(len(arr),0)




#교수님 추가 설명!

#부분 집합 합 문제 구현하기(연습문제 3) => 고를지 말지,,!!



#now : 이번에 고를지 말지 선택할 index => path를 사용하니깐 더 잘알 수 있다.

#check[now] = 1

#path를 사용해서!
def dfs(now, sum = 0):

    global ans

    if now >= len(data): #조합을 1가지 만들었다. 인덱스를 처음부터 끝까지 다 보았으니!

        if sum == 0: #만들고 보니 그 합이 내가 찾던 값이다. 합이 0이 되는 것을 찾고 있었네!
            print(path)
            ans += 1
        return

    check[now] = 1 #그냥 헷갈리니깐 이것도 그냥 넣자! 부분집합이나 부분집합 합 구할때! 그냥 넣어버리자!
    path.append(data[now]) #경로를 보기 위해서!
    dfs(now+1, sum + data[now]) #now를 고른 경우
    path.pop() #경로에서 다시 빼야지!

    check[now] = 0
    dfs(now+1, sum) #now를 고르지 않은 경우 path에 넣을것도 없으니 당연히 뭐 하는것도 없다!

data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
check = [0] * len(data)
path = []
ans = 0

dfs(0)

print(ans) #합이 10이 되는 부분집합의 갯수


'''

위에 같은 경우는 부분집합의 갯수를 제한하지 않았는데! 

이제는 제한을 해서 ,,! 그래서 data[now]를 추가할떄마다 부분집합의 원소를 사용하는 것이므로

cnt를 추가해서 답을 구한다!

'''

#4개를 골라서 0이 되는 것!

data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

check = [0] * (len(data))

path = []


ans = 0
cnt = 0


def dfs_subset(now, sum = 0):

    global cnt
    global ans

    if cnt == 4:
        if sum == 0:
            ans += 1
            print(path)
        return

    if now >= len(data):

        return

    cnt += 1 #횟수 증가했다! 값을 넣었으니깐!
    path.append(data[now])
    dfs_subset(now+1, sum + data[now])
    path.pop()
    cnt -= 1 #다시 돌아왔으니! 사용횟수는 줄었다

    dfs_subset(now + 1, sum)

dfs_subset(0)
print(ans)






