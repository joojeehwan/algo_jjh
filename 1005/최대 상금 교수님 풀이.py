# 시간 효율 업
# memoization, dp
# 가지치기 backtracking

def dfs(now, cnt = 0):
    # now번까지오는데, cnt번 교환을 했다.
    global ans

    if (k - cnt) % 2 == 0:
        # 짝수번 남아서 현재 모양을 확정 가능
        num = int("".join(map(str, num_list)))
        ans = max(ans, num)

    if cnt == k:
        # 정확히 K번 사용이 끝!(한가지 방법을 완벽하게 만들었다!)
        num = int("".join(map(str, num_list))) # 정수 리스트 -> 문자 리스트 -> 하나의 문자열 -> 하나의 정수
        ans = max(ans, num)
        return

    if now >= len(num_list):
        return
    # 1. now번째 교환 X
    dfs(now + 1, cnt)

    # 2. now번째 교환 O
    for i in range(now + 1, len(num_list)):
        # i : now번째랑 교환해줄 위치0
        num_list[now], num_list[i] = num_list[i], num_list[now]
        num = int("".join(map(str, num_list)))
        if not num in num_set[cnt + 1] :
             # 이미 cnt + 1번 교환으로 num을 만든 적이 있다.
            num_set[cnt + 1].add(num) # cnt + 1번 교환으로 지금 모양을 만들었다라고 추가
            dfs(now + 1, cnt + 1)
        #복구
        num_list[now], num_list[i] = num_list[i], num_list[now]


t = int(input())
for tc in range(t):
    num, k = input().split()
    k = int(k)
    num_list = list(map(int, str(num)))
    #"123" -> [1, 2, 3]
    num_set = [set() for _ in range(k + 1) ]
    # num_set[] - index : 교환 횟수, value : index횟수를 소모하여 만든 모양
    ans = -1
    dfs(0)
    print(f"#{tc + 1} {ans}")


