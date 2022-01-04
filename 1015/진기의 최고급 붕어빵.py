'''

다시 해도 못풀겟구만,, 뭐징,,





'''

# 손님이 도착했을 떄의 시간에 붕어빵이 몇 개 존재 하는지 파악,,!
# 0개 이하로 있다면 팔 수가 없어,,!



'''
def solution(N, M, K, peoples):
    peoples.sort()
    for i in range(N):
        total_bread = (peoples[i] // M) * K
        if total_bread < i + 1:
            return improssible
    return possible

'''


T = int(input())

for tc in range(1, T+1):

        N, M, K = map(int, input().split())

        arrival_time = list(map(int, input().split()))

        sorted_arrival_time = sorted(arrival_time)

        cnt =  0 #누적된 사람 수
        flag = 1 #참으로 고정

        for time in sorted_arrival_time:
                fish_bread = (time // M) * K

                #진기가 붕어빵을 못판다. 그 당시에 누적된 사람수보다 붕어빵의 갯수가 작아
                if fish_bread <= cnt:
                        flag = 0
                        break
                else:
                        cnt += 1

        if flag == 1:
                print(f"#{tc} Possible")

        else:
                print(f"#{tc} Impossible")





