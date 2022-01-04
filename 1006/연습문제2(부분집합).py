'''


연습문제 2
{1,2,3,4,5,6,7,8,9,10}의 부분집합 중에서 합이 10 부분집합을 모두 출력하시오


'''

# 부분집합 합 문제 구현하기(연습문제 3)
data = [1,2,3,4,5,6,7,9,10]
check = [0] * (len(data))
path = []
# index : data의 index, value : 해당 data를 골랐는가?

bit = 0
ans = 0
def dfs(now, sum = 0):
    global bit
    global ans
    if now >= len(data): # 조합을 1가지 만들었다.
        if sum == 10:#만들고 보니 그 합이 10이다.
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


'''

dfs  추가 되는 요소

1) check (중복 사용 금지)
2) path (어떤 방식으로 진행해 왔는지 확인)
3) snm, cnt (고른 원소들의 합, 몇 개의 원소를 골랐는가??)
4) 좌표, 계산, 좌표 유효성 검사(다음 좌표가 맵을 벗어나는가?)
5) 가지치키(특정 조건을 벗어나면 안되는 경우, 시간 효율을 업시킬 때)
6) DP, 메모이제이션(계산했던 값을 저장해놓고 똑같은 상황이 발생하면 전에 계산한 값을 갖다 사용, 시간 효율을 업 시킬 때)

'''


# 부분집합의 합이 10이되는 방법 찾기

def dfs(now = 0, sum = 0, path = []):
    if sum == 10:
        # 답을 1가지 찾았다!
        # 기록 <-
        ans_set.add(tuple(path))
        return
    if sum > 10:
        return # 가지치기
    if now == len(arr):
        return

    # 1. now를 사용한다.
    if sum + arr[now] <= 10 :
        dfs(now + 1, sum + arr[now], path + [arr[now]])
    # 2. now를 사용하지 않는다.
    dfs(now + 1, sum, path)


arr = [1,2,3,4,5,6,7,8,9,10]
ans_set = set()
dfs()
for ans in ans_set:
    print(ans)