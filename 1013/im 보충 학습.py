'''


<함수>

코드 반복

여러번 이용


단순화



'''




#1 두 배열이 같은지 아닌지 알려주는 함수 만들어 보자 is_same()함수 동일 / 안동일 한지 True, false로 해보자!

def is_same(arr1, arr2):

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True


lst1 = [3,2,1,7,5]
lst2 = [3,2,1,7,5]

print(is_same(lst1, lst2))





#2 맨 꼭대기 층의 인테리어와 같은 인테리어 패턴이 몇개 있는지 확인하는 함수!

MAP = [[3,2,1,7,9], [3,3,3,1,2], [3,2,1,7,9], [3,2,1,7,9], [1,2,3,4,5], [1,1,1,1,1], [3,2,1,8,9], [3,2,1,7,9], [3,3,1,7,9]]



def func2(MAP):

    temp = MAP[0]
    cnt = 0
    for i in range(1, len(MAP)):
        if temp == MAP[i]: #이렇게 해도 되는구나!
            cnt +=1

    return cnt


print(func2(MAP))




MAP = [
    [3,2,1,7,9],
    [3,3,3,1,2],
    [3,2,1,7,9],
    [1,2,3,4,5],
    [1,1,1,1,1],
    [3,2,1,8,9],
    [3,2,1,7,9],
    [3,3,1,7,9],
]

def is_same(y) :
    #MAP[y] [i]
    for i in range(5) :
        if MAP[y][i] != pattern[i] :
            return False
    return True

pattern = []
for i in range(5):
    pattern.append(MAP[0][i])
de = - 1
cnt = 0
for y in range(8):
    ret = is_same(y) # y 층과 vs pattern
    if ret == True :
        cnt += 1

print(cnt)


#3 맵에 패턴이 몇개 존재 하는지 출력!


'''

EX) 

<MAP>
A B G K A B
T T A B C P
A B C D C R
C D A B C D 

<pattern>

A B
C D


위와 같은 예시에서는 2개가 정답! 


1. 방법 2가지 아예 for문의 범위를 줄일지

2. 범위는 그대로 두고 예외처리를 할지! 
'''

MAP = [
    ["A", "B", "G", "K", "A", "B"],
    ["T", "T", "A", "B", "C", "P"],
    ["A", "B", "C", "D", "C", "R"],
    ["C", "D", "A", "B", "C", "D"]
]

pattern = [
    ["A", "B"],
    ["C", "D"]
]


# def is_parrten(MAP, pattern):
#
#
#
#     for i in range(len(MAP)):
#         for j in range()





MAP = [
    "ABGKAB",
    "TTABCC",
    "ABCDQR",
    "CDABCD"
]

pattern = [
    "AB",
    "CD"
]
'''
    [r+0][c+0] vs [0][0]
    [r+0][c+1] vs [0][1]
    [r+1][c+0] vs [1][0]
    [r+1][c+1] vs [1][1]
'''
def is_pattern(r,c): # r,c 부터 4칸 검사하기
    if r + 1 >= 4 or c + 1 >= 6 : return False # 범위 체크
    for dr in range(2) :
        for dc in range(2) :
            # MAP[r+dr][c+dc] vs pattern[dr][dc]
            if MAP[r+dr][c+dc] != pattern[dr][dc] : return False # 패턴 x

    return True


cnt = 0
for r in range(4) :
    for c in range(6) :
        ret = is_pattern(r,c)
        if ret == True:
            cnt += 1

print(cnt)