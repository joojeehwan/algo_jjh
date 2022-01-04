'''


창고 다각형


가장 큰 높이를 기준으로 왼쪽과 오른쪽을 나누어서 생각하자!




'''


#
# for i in range(4, -1, -1):
#     print(i)

import sys

input = sys.stdin.readline

max_high = 1
max_loc = 0

n = int(input())

#기둥들의 위치와 높이를 입력받을 리스트
pillar = []

#가장 높은 위치의 인덱스와 높이를 입력받으면서 같이 구하기!
for i in range(n):
    loc, high = map(int, input().strip().split())
    pillar.append([loc, high])

    #기둥이 어디까지 있는지,,!
    if max_loc < loc:
        max_loc = loc
    #가장 큰 높이의 기둥을 구하는!
    if max_high < high:
        max_high = high
        max_index = loc

#입력받은 값들을 이용해 다시 창고의 다각형 모양을 만듬.
pillar_list = [0] * (max_loc + 1)
for loc, high in pillar:
    pillar_list[loc] = high

total = 0

temp = 0
#처음부터 가장높은 위치까지=> if 절안 : temp보다 값이 크면 그 값을 total 더해
# if 절 밖 : temp가 더 크기 때문에 그냥 temp값을 더한다..
# 즉 큰 값을 만날때만 temp값을 바꾸면서 더한다!
for i in range(max_index + 1):
    if pillar_list[i] > temp:
        temp = pillar_list[i]

    total += temp

#오른쪽 끝에서 부터 가장 높은 위치 보다 한 칸 앞에 있는 곳 까지 =>
# max_loc ~ max_index + 1 범위를 탐색

temp = 0 #temp를 초기화해서! 다음 계산을 준비
for i in range(max_loc, max_index, -1):
    if pillar_list[i] > temp:
        temp = pillar_list[i]
    total += temp

print(total)