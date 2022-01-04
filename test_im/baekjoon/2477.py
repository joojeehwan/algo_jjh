'''



참외밭


동쪽 1

서쪽 2

남쪽 3

북쪽 4



방향이 1개씩 나오는거 2개 곱 - (방향이 2개씩 나온는 거 2개 곱 중간 2개) = 넓이

반 시계 방향으로 순서대로 주어진다! =>

데이터를 전처리 할까? 값이 하나 씩 나오는거 2개 앞으로 보내고, 2개씩 나오는거는 뒤에 2개씩


혹은

주어진 배열에서 가장 긴 가로변을 구할 수 있음. 그리고 이 양 옆에 있는 것 중에서

긴 것이


가장 긴 가로변 양옆에 붙어있는 변(세로변)들의 차이 : 작은 사각형의 세로 길이
가장 긴 세로변 양옆에 붙어있는 변(가로변)들의 차이 : 작은 사각형의 가로 길이


'''



melon = int(input())  #참외수

arr = [list(map(int, input().split())) for _ in range(6)]

max_width = 0
max_width_inex = 0
max_height = 0
max_height_index = 0

for i in range(6):

# 방향이 동서면 가로 => 1,2
# 이중에서 가장 긴 것 구하기,, 넓이
    if arr[i][0] == 1 or arr[i][0] == 2: #이거 2개중에 값이 하나씩 있으니깐!
        if max_width < arr[i][1]:
            max_width = arr[i][1]
            max_width_index = i


# 방향 남북이면 세로 => 3,4
# 이중에서 가장 긴 것 구하기,, 높이
    elif arr[i][0] == 3 or arr[i][0] == 4:

        if max_height < arr[i][1]:
            max_height = arr[i][1]
            max_height_index = i

'''
가장 긴 가로변 양옆에 붙어있는 변(세로변)들의 차이 : 작은 사각형의 세로 길이
가장 긴 세로변 양옆에 붙어있는 변(가로변)들의 차이 : 작은 사각형의 가로 길이
'''

#모둘려 연산을 통해서! 구현! 원형을 구현
mini_square_height = abs(arr[(max_width_index - 1) % 6][1] - arr[(max_width_index + 1) % 6][1])
mini_square_width = abs(arr[(max_height_index - 1) % 6][1] - arr[(max_height_index + 1) % 6][1])


print(((max_height * max_width) - (mini_square_height * mini_square_width))* melon)














