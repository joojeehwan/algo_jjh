'''

2019 카카오 신입 공채

프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/42891
에 가서 풀어야 정확히 풀림

힙큐 사용해서 시간이 가장 적게 걸리는 음식을 뽑아버리네,,!
'''

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간 보다 k가 크거나 같다면 -1

    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 음식 시간
    previous = 0

    length = len(food_times)  # 남은 음식의 개수

    # sum_value + (현재의 음식시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    # while문을 통해서 지금 찾고 있는거다! 조건이 아래에서 변하자나!
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length # 가장 시간이 적게 걸리는 녀석부터 다 먹었다! 그 시간!
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    #람다 정도 알고 가자
    res = sorted(q, key=lambda x: x[1])  # 음식 번호를 기준으로 정렬
    #여기도 알자! %로 다시 처음으로 오는,,!
    return res[(k - sum_value) % length][1]