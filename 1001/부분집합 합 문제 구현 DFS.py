'''


현재 인덱스에서 다음 인덱스를 고를지 안 고를지 선택하는 과정의 연속,,!  => DFS

'''


'''
DFS 디버깅 방법


1) 체크 사용

2) PATH를 사용


'''


# 부분집합 합 문제 구현하기(연습문제 3)
data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
check = [0] * (len(data))
path = []
# index : data의 index, value : 해당 data를 골랐는가?

bit = 0
ans = 0
def dfs(now, sum = 0):
    global bit
    global ans
    if now >= len(data): # 조합을 1가지 만들었다.
        if sum == 0:#만들고 보니 그 합이 0이다.
            """
            for i in range(len(data)):
                if check[i] == 1:
                    print(data[i], end = " ")
            print("")
            """
            print(path)
            ans += 1
        #print(bin(bit)[2:].zfill(len(data)))
        return

    # now : 이번에 고를지 말지 선택할 index
    #check[now] = 1
    # bit = bit | (1 << now) # now번째 bit에 1이라고 기록
    path.append(data[now])
    dfs(now + 1, sum + data[now]) # now를 고른 경우
    path.pop()

    # bit = bit & (bit ^ (1 << now)) # now번째 bit를 지워줌
    #check[now] = 0
    dfs(now + 1, sum) # now를 고르지 않은 경우

dfs(0)
print(ans)



#4개 골라서 0이 되는 것!


data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
check = [0] * (len(data))
path = []
# index : data의 index, value : 해당 data를 골랐는가?

ans = 0
cnt = 0

def dfs_2(now, sum = 0):
    global cnt
    global ans

    if cnt == 4:
        if sum == 0:
            ans += 1
            print(path)
        return

    if now >= len(data):
        return

    cnt += 1
    path.append(data[now])
    dfs_2(now+1, sum + data[now])
    path.pop()
    cnt -= 1

    dfs_2(now + 1, sum)


dfs_2(0)
