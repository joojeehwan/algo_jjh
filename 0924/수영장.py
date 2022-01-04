'''


dp

dfs

tip)

1번 인덱스가 1월이게 하기 위해서!

month = [0] + list ~


'''



#dfs 풀이! dp 풀이는 손으로 다시 해보자! 유투브 강의 최고의 이득!




'''

1) 일단 각 달 별로 완전탐색하지 않고 정해줄 수 있는 부분이 있다! (일 이용권을 살 것인지, 달 이용권을 살 것인지!)

2) 그리고 각 달을 한달이용권으로 살 것인지, 세 달 이용권으로 살 것인지 에 따른 완전탐색을 진행해준다.

3) 초기 최소값을 1년 이용권 가격으로 설정하고 비교해준다면, 자연스럽게 1년 이용권에 대한 탐색이 완료된다. 
=> 마지막에 비교할 필요가 없어짐! 

4) 11월 12월 처리를 해줄 것!

'''

#수영장 DFS 풀이


# def dfs(cost, m):
#     global min_cost
#
#     if m > 12:
#         if min_cost > cost:
#             min_cost = cost
#         return
#
#
#     #이렇게 조건을 주면서! 확실히 재귀의 횟수가 준다!
#     #그냥 라이브 방송의 풀이보다
#
#     #한달 모두 일 이용권으로 구매하는게 한 달 이용권보다 쌀 때!
#     if month[m]*day < mon:
#         dfs(cost + day*month[m], m + 1)
#     #1달권
#     else:
#         dfs(cost + mon, m + 1)
#     #3달권
#     if month[m]:
#         dfs(cost + quarter, m + 3)
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#     day, mon, quarter, year = map(int, input().split())
#
#     month = [0] + list(map(int, input().split()))
#
#     min_cost = year
#
#
#     dfs(0, 1)
#     print("#{} {}".format(tc, min_cost))



#####


'''

DP풀이!


앞에서 부터 경우의 수를 계산 하는 것! 


손으로 적어보니 이게 더 쉬운거 같디고하고,, 재귀 너무 어렵다! 


이건 디피로 푸는게 더 쉽구만?! 

'''


T = int(input())


for tc in range(1, T+1):


    day, mon, qua, yea = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(mon, day*month[1])
    dp[2] = dp[1] + min(mon, day*month[2])


    for i in range(3, 13):
        dp[i] = min(dp[i-3] + qua, dp[i-1] + mon, dp[i-1] + month[i] * day)

    #point! 마지막에 1년치랑 비교 하는 것 잊지 않기!
    print("#{} {}".format(tc, min(dp[12], yea)))
















































