


'''

아직도 어려운 dfs


N과M을 다시 풀어봐야한다,,!

얼른,,!

직원수 : 레벨,,!

순열 문제

1 -> 2 -> 3 이랑
1 -> 3 -> 2 는 다름!

'''

def dfs(result, person):
    global max_result

    if result <= max_result:
        return

    if person == N: #모든 직원이각 자 일을 맡아 다 할떄, 최종결과랑 비교
        if max_result <= result :
            max_result = result
        return 
    
    #재귀

    for i in range(N):
        if visited[i] == 0 : # 방문을 하지 않는 곳만 간다.
            visited[i] = 1
            dfs(result * lst[person][i]*0.01, person + 1)
            visited[i] = 0 #다시 나왔을떄 풀어줘야 다음 반복문에서의 방문떄 이곳을 또 울 수 있음!



T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N

    max_result = 0 #비교할 최대 확률(0%가 가장 낮으므로)

    dfs(1, 0)

    #이런 문법이 있구먼,,!
    ans = format(max_result*100, ".6f")

    print(f"#{tc} {ans}")





