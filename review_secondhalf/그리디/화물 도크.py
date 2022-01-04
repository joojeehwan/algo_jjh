#그리디 알고리즘의 문제는 정렬을 진짜 많이한다..


T = int(input())




for tc in range(1, T+1):
    N = int(input())

    time = [list(map(int, input().split())) for _ in range(N)]
    time.sort(key = lambda x:(x[1], x[0])) #람다로 정렬한느 방법 알아두면 편한다!
    #종료시간을 첫번 째, 시작 시간을 두번 째 기준으로 오름차순 진행

    # start_time = 5423575
    # for i in range(len(time)):
    #
    #     if time[i][0] < start_time:
    #         start_idx = i
    #         start_time = time[i][0]

    #정렬을 하게 되면 위와 같은 최소값을 굳이 안찾아도 맨 앞에 있는것을 선택하면 되자나!

    ans = 1
    end = time[0][1]
    for i in range(1, N):
        if time[i][0] >= end:
            end = time[i][1]
            ans += 1

    print(f"#{tc} {ans}")


#교수님 풀이

# 화물 도크 (정렬 -> for - if 문)
t = int(input())

for tc in range(t):
    n = int(input())

    #람다를 사용하지 않고! 이차원 배열에서 1번 인덱스 기준으로 정렬! => 바꿔서!
    time_stamp = [list(map(int, input().split())) for _ in range(n)]

    # 앞의 것 우선 SORT가 앞에것 기준으로 정렬하니간!
    for i in range(n):
        time_stamp[i][0], time_stamp[i][1] = time_stamp[i][1], time_stamp[i][0]
    time_stamp.sort()

    now = 0  # now : 지금 화물이 끝나는 시간
    ans = 0 #가짓수!
    for i in range(n):
        if now <= time_stamp[i][1]:
            # now시간 이후에 시작하는 도크
            now = time_stamp[i][0] #나우 갱신
            ans += 1 #가지수더하기!
    print(f"#{tc + 1} {ans}")