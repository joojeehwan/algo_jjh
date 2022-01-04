

#그리디 알고리즘,,! 나올만 해!
from copy import _copy_immutable

import sys
sys.stdin = open('쉬운 거스름돈_input.txt')

T = int(input())



for tc in range(1, T+1):

    N = int(input())

    count = 0
    coin_types = [50000, 10000, 5000, 1000, 500, 100, 50 ,10] #일부러 큰 값부터 정렬!
    #무슨 종류의 코인이 있는지 정렬하고,,!
    res = []
    #정답이 들어갈 곳
    for coin in coin_types : #코인을 값을 큰것부터 차례대로 가져오면서!
        res.append(N // coin) #만약에 coin이 더 크게 되면 값이 0이 들어가게 된다!
                                # 문제가 원하는 바!
        if N >= coin:
            N %= coin #coin을 보기 위한 그 다음 자리 수의 N을 보기 위해서!

    print("#{}".format(tc))
    print(*res)


