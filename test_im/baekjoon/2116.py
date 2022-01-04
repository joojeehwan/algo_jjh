'''


주사위 쌓기



주사위를 수직으로 쌓을때 서로 맞닿은 부분의 눈이 같아야하고 전부다 쌓았을 때 양옆 주사위 눈의 합의 최대값을 구하는 문제이다.


주사위 눈은 1-6, 2-4, 3-5가 서로 위아래로 짝지어져있기 때문에 반대편은 자동적으로 따라온다.

나는 주사위 눈을 짝지어서 배열에 저장했다.

전체 주사위를 돌면서 저장한 주사위 눈의 짝에서 값을 찾고 반대쪽을 다음 대상으로 바꿔가면서 반복문을 진행했다.

#
#
# 양옆의 숫자중 최대값은 4,5,6중 하나이므로 6,5가 있는지 체크해서 최대값을 구해서 더해나갔다.
#
#
# '''
#
#
#
from sys import stdin
input = stdin.readline


n = int(input())


dices = [[] for _ in range(n)]
answer = 0

for idx in range(n):
    nums = list(map(int, input().split()))

    dices[idx].append((nums[0], nums[5]))
    dices[idx].append((nums[1], nums[3]))
    dices[idx].append((nums[2], nums[4]))

#[[(2, 4), (3, 6), (1, 5)],
# [(3, 5), (1, 4), (2, 6)],
# [(5, 2), (6, 1), (4, 3)],
# [(1, 5), (3, 2), (6, 4)],
# [(4, 3), (1, 5), (6, 2)]]






def solv():
    for dice in dices[0]:
        for target in dice:
            # print(target)
            select_num(target)
    print(answer)



def select_num(target):
    global answer
    total = 0

    for idx in range(n):
        for dice in dices[idx]:
            if target in dice:
                if 6 in dice:
                    if 5 in dice:
                        total += 4
                    else:
                        total += 5
                else:
                    total += 6
                if target == dice[0]:
                    target = dice[1] # 그 다음 번호 확인 하려는?!
                    break

                else:
                    target = dice[0] #타켓의 값을 다이스에 첫번째로,,
                    break
    answer = max(answer, total)

solv()
