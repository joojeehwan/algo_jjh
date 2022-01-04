'''


공유기 설치

파라메트릭 서치 유형


'''

import sys
input = sys.stdin.readline

#N : 전체 집의 개수, C : 공유기의 갯수
N, C = map(int, input().split())

#전체 집의 좌표 정보를 입력받기

lst = list(int(input()) for _ in range(N))


#이진 탐색을 위해서 정렬을 수행

lst.sort()

#집의 좌표중에서 gap이 가장 작은 값
start = 1

#집의 좌표들 중에서 gap이 가장 큰 값
end = lst[-1] - lst[0]

res = 0

if C == 2:
    print(lst[-1] - lst[0])

else:
    while (start <= end) :
        mid = (start + end ) // 2
        #맨 앞에서 부터 차례대로 설치를 하니깐 !
        value = lst[0]
        count = 1

        #현재의 mid(gap)값을 이용해소 공유기를 설치

        for i in range(1, len(lst)):
            #앞에서부터 차례대로 설치 함
            if lst[i] >= value + mid:
                value = lst[i]
                count += 1

        #C개 이상의 공유기를 설치할 수 있는 경우, gap의 시작의 좌표를 증가
        if count >= C:
            start = mid + 1
            res = mid

        #C개 이상의 공유기를 설치할 수 없는 경우, gap의 끝 좌표를 감소
        else:
            end = mid

print(res)



'''

import math,sys
input = sys.stdin.readline

n,c = map(int,input().split())
h = [int(input()) for i in range(n)]
h.sort()
start,end = 1, h[n-1] - h[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if c == 2:
    print(h[n-1] - h[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while(start < end):
        mid = (start + end)//2

        count = 1
        ts = h[0]
        # 마지막으로 설치된 공유기의 위치
        for i in range(n):
            if h[i] - ts >= mid:
                count+=1
                ts = h[i]
        if count >= c:
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
    print(result)

'''