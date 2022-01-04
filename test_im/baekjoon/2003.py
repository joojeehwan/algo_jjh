'''


수들의 합2

투포인터




'''




N , M = map(int, input().split())

lst = list(map(int, input().split()))


count = 0

temp_sum = 0

end = 0

for start in range(N):

    #end를 가능한 만큼 이동 시키기
    while temp_sum < M and end < N: #합이 목표합보다 작고, end가 뒤로 갈곳이 있으면
        temp_sum += lst[end]
        end += 1

    if temp_sum == M:
        count += 1

    temp_sum -= lst[start]




print(count)

