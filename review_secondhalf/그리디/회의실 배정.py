'''

그리디는 이걸로 마무리


활동선택 문제

1. 종료 시간이 빠른 순서로 활동들을 정렬한다.
2. 첫번쨰 활동(a1)을 선택한다
3. 선택한 활동(a1)의 종료시간 보다 빠른 시작 시간을 가지는 활동을 모두 제거
4. 남은 활동들에 대해 앞의 과정을 반복

'''


N = int(input())

times = []

for _ in range(N):

    start_time, end_time = map(int, input().split())
    times.append((start_time, end_time))

#종료 시간 기준으로 정렬을 해야 함 => 종료 시간이 빠른 순으로 정렬! 그리고는 시작시간이 가장 빠른 순으로,,!

times.sort(key = lambda x:(x[1], x[0]))


'''

람다식 생각 나지 않으면! sort를 사용하기 위해서!
  for i in range(n):
        time_stamp[i][0], time_stamp[i][1] = time_stamp[i][1], time_stamp[i][0]
    time_stamp.sort()
'''

cnt = 1
end_time = times[0][1] #가장 빠른 종료시간

for k in range(1, N):
    if times[k][0] >= end_time : #가장 빠른 종료시간 보다 그 이후에 있는 가장 빠른 시작시간(이미 정렬이 되어있기 떄문에 순차적으로) for문을 돌아도 가능 한것! 
        cnt += 1 # 정답의 갯수 증가
        end_time = times[k][1] # 그 다음 반복을 위해서 end_time을 갱신

print(cnt)