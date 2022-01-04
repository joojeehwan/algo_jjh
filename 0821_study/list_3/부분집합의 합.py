


T = 10


#이건 암기하자..!
for tc in range(1, T+1):

    N = int(input())
    nums = list(map(int, input().split()))


    ans = 0 #

    for bit in range(1 << N):
        #부분 집합에 사영할 원소들 고르는 작업

        sum = 0
        for index in range(N):
            #비교"할" 녀석들을 뽑는!

            if 1 << index & bit != 0:
                #index의 위치에 값이 있으면 if절안으로 들어온다!
                sum += nums[index]

        if sum == 0:
            ans += 1

    print("#{} {}".format(tc, ans))





