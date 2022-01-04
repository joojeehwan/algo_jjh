'''

10/ 01 숙제

야 이걸 어떻게 dfs로 푼거지?!

완전탐색이면 dfs, bfs가 생각나야지 포문으로 다 돌리는것만 생각나면 안돼!

dfs로 가지치기를 한다면 충분히 시간 단축이 가능하다.


'''

def dfs(runs = 0):

    global result

    #종료조건과 재귀를 이어나갈 식이 필요

    if runs == swaps:
        result = max(result, int("".join(numbers)))
        return #종료,,
    for i in range(digits):
        for j in range(i + 1, digits):
            numbers[i],numbers[j] = numbers[j], numbers[i]

            checker = "".join(numbers)
            if (checker, runs) not in visited:
                visited.add((checker, runs))
                dfs(runs + 1) # dfs

            numbers[i],numbers[j] = numbers[j], numbers[i]

T = int(input())


for tc in range(1, T+1):

    numbers, swaps = input().split()

    numbers = list(numbers)

    swaps = int(swaps)

    digits = len(numbers)

    result = 0

    visited = set()

    dfs()

    print(f"#{tc} {result}")





''''

K가 전체길이 이상인것,,을 확인하는 ,,! 그게 바로 추가됨! 


'''


#시간 효울을 업 시키는 방법

# 1. 가지치기 => 지금에서는 중복된 수가 또 만들어지는 것을 방지!