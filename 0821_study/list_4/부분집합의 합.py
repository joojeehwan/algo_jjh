





T = int(input())


for tc in range(T):

    N, K = map(int, input().split())

    ans_count = 0

    for bit in range(1 << 12):

        sum = 0
        cnt = 0

        for j in range(12):
            if bit & (1 << j) != 0 : #값이 있으면!
                # j번째 bit를 filtering한 결과가 1이 있으면
                # => 0이 아니라면 j번째 수를 사용하겠다는 의미
                sum += j + 1 #1번 부터 12번까지의 숫자를 사용해야 하므로,,!
                cnt += 1

        if sum == K and cnt == N:
            ans_count += 1

    print("#{} {}".format(tc + 1, ans_count))