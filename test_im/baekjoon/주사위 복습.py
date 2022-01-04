# 주사위를 N번 던져서 나올 수 있는 눈의 조합
# 단, 같은 눈을 2번이상 뽑으면 안된다!
# 1 1 ???

'''

백트래킹! (기본은 dfs)
다 해보면 시간이 너무 오래걸려,,! 그래서 중간에 안해보는 경우를!

끝까지 다 만들고 판단 한느 것이 아니라, 중간에 확인을 해본다!

now와 now +1 의 관계

다음이 여러개면 그에 맞게 또 재귀,,!

백트래킹 스킬

"패스" : 내가 어떻게 왓는지 기록!

-1 : 모름, 0 : 사용안함 1 : 사용함


'''

N = 3
path = [-1] * N

DAT = [0] * 7
sum = 0
cnt = 0


def dfs(now):
    global sum
    global cnt
    if now >= N:
        #N개의 주사위를 전부 뽑았다.
        print(path, sum)
        return

    for i in range(1, 7):
        path[now] = i
        sum += i
        cnt += 1

        dfs(now+1)

        sum -= i
        cnt -= 1
        # path[now] = -i 내가 직접 손으로 그려보니 이건 없어도 된다!

dfs(0)
