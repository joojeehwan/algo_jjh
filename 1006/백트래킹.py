'''



부분집합 백트래킹으로 만든느거 이해가 안되네???

'''


'''


연습문제2


백트래킹 2가지 방법 : 
1) 지금까지 더한게 내가 찾는것보다 더 커? 그럼 가지치키

2) 지금까지 더한거랑 더한게 남은거랑 더해도 내가 찾고자 하는 것보다 작아? 그럼 가지치기! 

'''





'''

백트래킹 이용하여 순열 / 조합을 구하는 것은 많이 사용 됨! 

'''


#조합


def dfs(level, beginwith):

    if level == r: #r개를 뽑은 경우
        print(res)
        return

    for i in range(beginwith, len(n)):
        res[level] = n[i]
        dfs(level + 1, i + 1)



n = [i for i in range(10)]
r = 6
res = [0] * r
dfs(0,0)



#순열


def dfs(level):

    if level == r:
        print(res)
        return

    for i in range(len(n)):
        if checked[i] == True:
            continue
        res[level] = n[i]
        checked[i] = True
        dfs(level + 1)
        checked[i] = False



n = [i for i in range(3)]
r = 2
res = [0] * r
checked = [False] * len(n)
dfs(0,0)

