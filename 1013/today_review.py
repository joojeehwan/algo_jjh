


# 2. 맨 꼭대기 층의 인테리어와 같은 인테러이 패턴이 몇개 있는지 확인하는 함수.


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


# x층! 이 함수 밖에서 for문으로 한 층씩 접근 할 것임!
def is_same(x):

    for i in range(5):
        if MAP[x][i] != pattern[i]:
            return False

    return True


pattern = []
#패턴은 첫번째 리스트니깐!
for i in range(5):
    pattern.append(MAP[0][i])

cnt = 0

for i in range(8):
    ret = is_same(i)
    if ret == True:
        cnt += 1

print(cnt)



#3. 맵에 패턴이 몇개 존재 하는지 출력!

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
    
    이렇게 4개에 대해서 비교를 하는 것,,! 
    
'''


#4중 포문을 함수를 사용해서 뺀 것!

# 4중 포문 사용하는 문제?! => 파리퇴치 문제!

def is_pattern(row, col): # rol, col 부터 4칸 검사하기

    if row + 1>= 4 or col + 1 >= 6 :
        return False # 범위 체크 범위를 벗어남!

    for dr in range(2):
        for dc in range(2):

            if MAP[row+dr][col+dc] != pattern[dr][dc]:
                return False



cnt2 = 0
for row in range(4):

    for col in range(6):

        ret = is_pattern(row, col)
        if ret == True:
            cnt2 += 1


print(cnt2)





