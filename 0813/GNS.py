T = int(input())
for tc in range(T):
    temp = input()
    data = input().split()
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0] * 10

    for now in data:
        for i in range(10):
            if nums[i] == now:
                counts[i] += 1
    # data의 수가 몇 개씩 있는지 counting
    print("#{}".format(tc + 1))
    for i in range(10):
        for j in range(counts[i]): # 각 숫자가 몇번 나왔는지
            print(nums[i], end = " ") # 그 숫자에 맞는 문자를 출력
    print("")