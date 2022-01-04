#dp로 풀어보자!



'''

최세진 교수님 dp풀이 레츠고!

그전에 그냥 dfs + 가지치기 풀이!

조합의 방식으로 풀어버렷네?!
'''

def dfs(now, cnt = -1):

    global ans

    if cnt >= ans: #가지치기
        return

    if now >= n - 1:
        ans = min(ans, cnt)
        return

    #for문으로 next를 찾는 이유! 그 지점까지 딱 가는게 아니라 범위내에 있는 곳 어디든에서든 교환을 할 수 있으니깐!
    for next in range(now + 1, now+ charges[now] + 1):
        dfs(next, cnt + 1)



T = int(input())

for tc in range(1, T + 1):

    data = list(map(int, input().split()))

    n = data[0] #첫번째 데이터는 갯수!

    charges = data[1:] #1 이후의 모든 것들

    ans = 987654321

    dfs(0)

    print(f"#{tc} {ans}")



#dp 풀이! dp 배열을 이용한!

def dfs(now):
    
    # now 이후로 목적지까지 교환해야하는 최소 횟수

    if now >= n - 1:
        return 0
    #이미 dp에 저장이 되어있는 거면 그냥 가져와서 쓰자!
    if dp[now] != -1:
        return dp[now]

    ret = 987654321

    #여기서 ret값을 정해주네! now에서 그 다음으로 갈 수 있는 값중에서 가장 최소 값을!
    for next in range(now + 1, now + charges[now] + 1):
        ret = min(ret, dfs(next) + 1)
    #dp 배열에서 쓸 수 있게 ret값을 넣어주자!
    dp[now] = ret
    return ret


T = int(input())

for tc in range(1, T + 1):

    data = list(map(int, input().split()))

    n = data[0] #첫번째 데이터는 갯수!

    charges = data[1:] #1 이후의 모든 것들

    ans = 987654321

    dp = [-1] * n #now 이후로 목적지까지 교환해야하는 최소 횟수가 담기는 배열


    print(f"#{tc} {dfs(0) - 1}")



