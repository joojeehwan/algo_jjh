'''

스택은 논리적인 것,,!

포함관계를 갖는 알고리즘 문제? 스택! EX) 괄호 문제


파이썬은 스택 만들 때! 굳이 TOP변수 설정해서 포인터질 안해도 되는구나!


파이썬에서는 isfull (푸시할떄) 굳이 안만들어도 된다!
그리고 심지어 안만들고 그냥 appned만 써도 상관 없다.

pop도 안만들고!
peek도 안만들고!


함수 밖에서 써도! 리스트는 글로벌이라 안써도 돼
그러나 일반변수는 사용해야해!



모든 언어에서 함수를 호출할때 스택을 사용한다!


디버그 옆에 프레임이 스택영역!

'''


#
#
# def push(item):
#     st.append(item)
#
#
# def pop():
#     if len(st) > 0:
#         return st.pop(-1)
#     return -1
#
# def peek():
#     return st[-1]
#
#
# st = []
#
# push(1)
# push(1)
#
from Tools.scripts.findlinksto import visit


def F_2():
    print("2-1")
    print("2-2")
    return 3
def F_1():
    print("1_1")
    value = F_2()
    print("1_2")
    return
print("m_1")
F_1()
print("m-2")
F_1()


#디버깅 꿀tip 사진확인 0719분 0818



#메모이 제이션

def fibo_m(n):
    # if n<2:
    #     memo[n] = n
    #     return memo[]
    #

    if n>=2 and memo[n] == 0:
        return fibo_m(n - 1) + fibo_m(n - 2)


    return memo[n]



n = 10
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1


#DFS => STACK BFS => 큐


#인접을 어떻게 표현하니??? 친구야???


#1. 인접행렬

adj = [[0,0,0,0,0,0,0],  #0
       [0,0,1,1,0,0,0],  #1
       [0,1,0,0,1,0,0],
       [0,1,0,0,1,0,0],
       [0,0,1,1,0,1,1]]  #5

#2. 딕셔너리로도 만듬


G = {0:[], 1:[2,3], 2:[4], 3:[4], 4:[2,3], 5:[4], 6:[4]}


#3 나동빈식도 보자!

graph = [[],
        [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
            ]


#v의 인접정접 중 방문하지 않은 w를 return
#없으면 -1 return




lst = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
visted = [False] * 8
st = []

def findW(v):
    for i in range(0, len(lst), 2):
        if lst[i] == v and visted[lst[i+1]]==False:
            return lst[i+1]

        if lst[i+1] == v and visted[lst[i]] == False:
            return lst[i]
    return -1

def findG(v):
    for c in G[v]:
        if visted[c]==False:
            return c

   return -1

def findG(v):
    for c in G[v]:
        if visted[c]==False:
            return c

   return -1





def dfs(v):
    visted[v] = True
    print(v, end = "")
    st.append(v)

    while st:
        w = findW(v)
        if w != -1 :
            st.appned(v)
            visted[w] = True
            print(w)
            v = w
        else:
            v = st.pop(-1)