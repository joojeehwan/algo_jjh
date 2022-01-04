'''


그리디 알고리즘으로 풀어보자




'''

import sys
"""
Baby_Gin: Baby Gin
"""

import sys
sys.stdin = open('Baby_Gin_input.txt')




T = int(input())

for tc in range(1, T + 1):

    cards = int(input())


    # 번호가 인덱스가되어서
    counts = [0] * 10


 #카드 번호의 끝자지를 하나씩 확인 하는 로직
    for _ in range(6):
        counts[cards % 10] += 1
        cards //= 10 #계산햇으니 다음 자리 보자


    i = 0
    tri = run = 0

    while i < 8: #밑에서 인덱스가 i+2 까지 가니깐! 인덱스 i를 7까지 못하게 한것,,!(0~9숫자이지만)
        if counts[i] >= 3: # 트리플을 만족하는 아이들
           counts[i] -= 3 #트리플을 만족햇으니, 카운츠 배열에서 내려온다
           tri += 1
           continue #이것을 적음으로써 run과 트리플이 동시에 있을 경우를 확인! 밑에 있는 i를 증가 시키지 않으면서! 

        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1 :
            counts[i] -= 1 #값을 하나씩 빼면서 다음 "런"을 위해서 준비!
            counts[i+1] -= 1
            counts[i+2] -= 1
            run += 1
            continue

        i += 1

    if run + tri == 2:
           print("#{} Baby Gin".format(tc))
    else:
           print("#{} Lose".format(tc))

