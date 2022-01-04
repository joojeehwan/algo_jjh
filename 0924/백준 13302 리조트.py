'''

5일권을 쓰는게 좋은거 같은데,,?!





dfs 풀이!



'''

# 백준 13302 리조트 DFS DP 수정 완료본
import sys

#3. 값에대한 처리, 반환 받아서 사용
# 현재 상태에서 마지막까지 도달하는데 필요한 비용
def dfs(day, tic):
    #dfs(day, tic)
    # day,tic상태에서 n일까지 앞으로 최소한 얼마나 필요한가? 반환

    # 2. 기저 조건
    global n
    if day > n:
        return 0
    if DP[day][tic] != 21e8:
        # 첫 세팅값이 아니면 '계산한 적이 있다.'
        return DP[day][tic]
    cost = 21e8
    # 1. 기본 구조
    cost = min(cost, dfs(day + 1, tic) + 10000)
    # day+1,tic에서부터 n일이 될때까지의 최소 비용
    cost = min(cost, dfs(day + 3, tic + 1) + 25000)
    cost = min(cost, dfs(day + 5, tic + 2) + 37000)
    if tic >= 3:
        cost = min(cost, dfs(day + 1, tic - 3) + 0)
    if DAT[day] == 1:
        cost = min(cost, dfs(day + 1, tic) )
        # 이용하지 못하는날은 이용권을 사용하지 않고 그냥 날짜만 지나감
    DP[day][tic] = cost
    return cost

# dfs에서 시간 줄이는 방법 2가지
# 1. dp, memoization
# 2. 가지치기

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
DP = [ [21e8] * (n + 6) for _ in range(n + 6) ]
# DP[day][tic] : day, tic상태에서 n일까지 '최소 비용'

DAT = [0] * (n + 6) # DAT['날짜'], value - 1:이용 불가, - 0:이용 가능
for day in data:
    DAT[day] = 1

print(dfs(1, 0))






##################################################################




# 백준 13302 리조트 for문 DP 수정 완료본
import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
DP = [ [21e8] * (n + 6) for _ in range(n + 6) ]
# DP[day][tic] : day, tic상태에서 n일까지 '최소 비용'

DAT = [0] * (n + 6) # DAT['날짜'], value - 1:이용 불가, - 0:이용 가능
for day in data:
    DAT[day] = 1

DP[0][0] = 0

for day in range(1, n + 1):
    for tic in range(n + 1):
        # day까지 티켓이 tic개만큼 있을 때, 얼마나 비용이 들었는가?
        # day, tic상태
        #1일권
        cost = DP[day - 1][tic] + 10000
        #3일권
        if day >= 3 and tic >= 1:
            cost = min(cost, DP[day - 3][tic - 1] + 25000)
        #5일권
        if day >= 5 and tic >= 2:
            cost = min(cost, DP[day - 5][tic - 2] + 37000)
        #쿠폰
        if tic <= n - 3: # <----- 여기서 tic >= 3을 하면 안됐습니다... tic+3에 대한 처리만 해줘야 합니다.
            cost = min(cost, DP[day - 1][tic + 3])
        if DAT[day] == 1: # 리조트 이용 X
            cost = min(cost, DP[day - 1][tic])
        DP[day][tic] = cost

ans = 21e8
for tic in range(n + 1):
    ans = min(ans, DP[n][tic])

print(ans)



