''''

수열 2559



온도의 합을 구하는 문제,, 이거 im 스럽다!


'''

#완탐 -> 시간 초과
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
#
# Temperature = list(map(int, sys.stdin.readline().split()))
#
# max_temperature = 0
# for i in range(N - K + 1):
#
#     temp_Temperature = 0
#     for j in range(i, i + K):
#         temp_Temperature += Temperature[j]
#
#     max_temperature = max(max_temperature, temp_Temperature)
#
# print(max_temperature)




# 슬라이딩 윈도우 보다 더 쉬운 방법

import sys

N, K = map(int, sys.stdin.readline().split())

Temperature = list(map(int, sys.stdin.readline().split()))


temp = sum(Temperature[:K])
result = temp #처음 값이 일단 최대라 생각하고 넣어두기! 처음 값이 최대일 수도 있으니깐
for i in range(K,N):
    temp += Temperature[i] - Temperature[i-K] #연속된 k일에서 k+1번째 되는 날의 온도를 더하고 첫번쨰 날을 뺸다.
    result = max(result, temp) # 최대 값을 구해라!


print(result)





#슬라이딩 윈도우


