'''

find : 조상 찾기! 
=> 내가 어떤 그룹인가?!

union : 2개를 같은 그룹으로 묶음(대표 원소끼리! )



1) 각각의 조상을 찾기
2) 한 쪽 조상을 다른 쪽 조상 밑으로 넣어준다.



그룹에 대한 정보?! => 조상에 다 몰아서!(사진 확인)


'''




'''

기본 유형

'''

def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px

parents = [i for i in range(7)] # make-set



'''

1. 유형 : root에 정보 몰아넣기!(그룹 정보 관리)

백준 친구비 문제


'''
#Q) 1번 을 포함하는 집합의 갯수는 ?!
#Q) 가중치들의 합? 계산
#실제 문제에서는 "유니온"을 커스텀하게 문제가,,! 

#그룹에 대한 정보!를 확인하는!
def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px

def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px


    #이 아래 부분이 추가 됨! 대표에 다가 모든 정보를!
    #그룹에 대한 정보?! => 조상에 다 몰아서!(사진 확인)
    if px == py:
        return
    cnt[px] = cnt[py]
    cnt[py] = 0


parents = [i for i in range(7)] # make-set
cnt =[i for i in range(7)]



'''

2. 유형 : 문제에서 요구하는 것을 역산으로 처리(난도가 높음)

백준 13306 트리

3. 유형 : 민 스패닝 트리, 사이클을 방지할 때 사용 

'''