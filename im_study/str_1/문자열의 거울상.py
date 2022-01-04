

import sys
sys.stdin = open("문자열의 거울상_input.txt")

T = int(input())


for tc in range(1, T+1):

    sen = input().rstrip()

    res = ""

    for se in sen:

        if se == "b":
            res = "d" + res

        if se == "d":
            res = "b" + res

        if se == "p":
            res = "q" + res

        if se == "q":
            res = "p" + res

    print("#{} {}".format(tc, res))
