'''


아니 이거 dfs 아냐?
'''



def f(n, k):  #순열의 크기 n , 결정할 위치 k
    if n == k:
        print(p)

    else:
        for i in range(n):
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                f(n, k+1)
                u[i] = 0

p = [0] * 3
arr = [1,2,3]
u = [0] * 3
# f(3,0)



# 숫자를 5개를 주는데 3개를 골라봐!


def f2(n,m,k):
    if n == k:
        print(p)

    else:
        for i in range(m): #주어진 숫자의 개수만큼
            if u[i] == 0:
                u[i] = 1
                p[k] = arr[i]
                f2(n, m, k+1)
                u[i] = 0

p = [0] * 3
arr = [1,2,3,4,5]
u = [0] * 5
f2(3,5,0)