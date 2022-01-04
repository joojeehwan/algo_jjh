





# 나 보다 높이가 큰것이 양옆으로 2칸 이상 거리가 뛰어 있어야대,,,! 
'''

왼쪽 오른쪽으로 나보다 높이가 큰 값이 있는게 2칸 이상 뛰고,,, 존재 해야대

=> 1) 양옆으로 2개씩 나보다 작은 것들이 있고
   2) 갯수를 구할때는 가장 큰것에서 두번째 작은것 뺴기

'''


import sys
sys.stdin = open("view_input")



TC = 10

for tc in range(1, TC+1):

    N = int(input())
    height = list(map(int, input().split()))


    #case1 가장 높은 높이에서 두번째 높은 높이를 뺀 세대수


    # max_height = height[0]
    #
    # second_max_height = height[1]
    #
    # for hei in height:
    #     if max_height < hei:
    #         max_height = hei
    # for hei in height:
    #     if second_max_height < hei and max_height > hei:
    #             second_max_height = hei
    #
    # case1 = max_height - second_max_height



    #case2 그 외에 세대간의 차이가 2만큼 떨어져 있는 것들의 갯수


    #아 이중포문의 개념을 몰랏다... 기준을 돌리면서 그 기준에 맞는거 경우의 수 따라라락! 그 느낌!
    # 방 마다 열고 들어가서 여기 있어 없어?! 그리고 다음방 가서 있어 없어? 이느낌 !
    # 반복 하나 후 들어가서 확인 반복 따따따따ㄸ라라 그 디음 반복 들어가서 반복후 따따따따따ㅏ라


    sum = 0
    for i in range(2, N-2):
        max_value = 0
        for j in range(-2, 3):
            if j != 0 and (max_value < height[i + j]):
                max_value = height[i + j]
        ret = height[i] - max_value
        if ret < 0:
            ret = 0

        sum += ret