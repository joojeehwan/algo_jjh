'''


작사각형

두개의 직사각형이 겹치는 부분이

1. 직사각형

2. 선분

3. 점

혹은 아예 안 겹치거나,,!


'''



'''

1. 두 직사각형의 왼변중 x 좌표가 큰 변, 오른변중 x 좌표가 작은 변, 윗변중 y 좌표가 작은 변, 아랫변중 y 좌표가 큰 변을 고른다.

 

2. 위에서 구한 값 중 x 축에 평행한 변의 좌표끼리, y 축에 평행한 변의 좌표끼리 서로 빼준다.(각각 xdiff, ydiff)

 

3. xdiff 나 ydiff 둘다 0이상이면 a 

    둘중 하나라도 0 이하면 d

    둘다 0이면 c

    나머지는 b

 

4. 위 과정을 4번 반복한다.



'''
for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    xl = max(x1, x2)
    xr = min(p1, p2)
    yb = max(y1, y2)
    yt = min(q1, q2)

    xdiff = xr - xl
    ydiff = yt - yb
    if xdiff > 0 and ydiff > 0:
        print('a')
    elif xdiff < 0 or ydiff < 0:
        print('d')
    elif xdiff == 0 and ydiff == 0:
        print('c')
    else: print('b')





for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    result = "a"

    if q1 < y2 or q2 < y1 or x1 > p2 or p1 < x2:
        result = "d"

    if p1 == x2:
        result = "c" if (q1 == y2 or y1 == q2) else "b"

    if x1 == p2:
        result = "c" if (y1 == q2 or q1 == y2) else "b"

    if q1 == y2:
        result = "b"


    if q2 == y1:
        result = "b"
        continue

    print(result)

    # if q1 < y2 or q2 < y1 or x1 > p2 or p1 < x2:
    #     result = "d"
    #
    # #오른쪽에서 점 선
    # if p1 == x2:
    #     if q1 == y2 or y1 == q2:
    #         result = "c"
    #     else:
    #         result = "b"
    #
    # #왼쪽에서
    # if x1 == p2:
    #     if y1 == q2 or q1 == y2:
    #         result = "c"
    #
    #     else:
    #         result = "b"
    #
    # #위에서
    # if q1 == y2:
    #     if p1 == x2 or p2 == x1:
    #         result = "c"
    #
    #     else:
    #         result = "b"
    #
    # #아래에서
    # if y1 == q2:
    #     if p1 == x2 or p2 == x1:
    #         result = "c"
    #
    #     else:
    #         result = "b"
    #
    # print(result)


import sys
input = sys.stdin.readline

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1==y2 or q2==y1:
            print('b')
            continue
    else:
        print('a')
        continue
