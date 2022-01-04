# 주사위를 N번 던져서 나올 수 있는 눈의 조합
# 단, 같은 눈을 2번이상 뽑으면 안된다!
# 1 1 ???

N = 3
path = [-1] * N
DAT = [0] * 7
sum = 0
cnt = 0


def dfs(now):
    global sum
    global cnt
    if now >= N:
        # N개의 주사위를 전부 뽑았다.
        print(path, sum)
        return
    # DAT[index] -> index : 주사위눈, value : 해당 주사위 눈을 뽑은적이 있는가?

    # now : 몇 번째 주사위를 던질 것인가?
    # 1, 2, 3, 4, 5, 6
    for i in range(1, 7):
        # i라는 눈을 뽑았다.
        path[now] = i # now번째에 i라는 눈을 뽑았다 라고 기록
        sum += i
        cnt += 1
        # i라는 눈을 뽑았을 때, 다음 주사위 눈도 뽑으러 가라!
        dfs(now + 1)
        sum -= i
        cnt -= 1
        path[now] = -1 # i라는 눈을 뽑았을 때 방법들은 끝났으니 복구

dfs(0)