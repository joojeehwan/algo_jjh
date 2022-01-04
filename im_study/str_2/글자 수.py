


T = int(input())



for tc in range(1, T+1):

    str1 = input()

    str2 = input()

    counts = [0] * 256 #인덱스에 의미를 부여,,! 그 인덱스 번호가 그 문자! 2이면 그 문자가 2개 있는 것!

    for ch in str2:
        counts[ord(ch)] += 1 #ord가 문자를 숫자로,,!


    max_count = -1

    for ch in str1:
        if max_count < counts[ord(ch)]:
            max_count = counts[counts[ord(ch)]]


    print("#{} {}".format((tc, max_count)))

