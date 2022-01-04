
import sys

sys.stdin = open("GNS_test_input.txt")


#카운트 배열을 만들어서!

T = int(input())

for tc in range(1, T+1):

    temp = input()

    lst = input().split()

    #counts배열을 만들기 위해서 순서에 맞게 만든것!
    nums =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    #이것의 인덱스가 곧 값을 의미,,!
    counts = [0] * 10

    #이중포문을 사용해서 카운츠 안에 입력받은 li와 i의 값을 비교!  => 값이 같다면  count의 값을 증가!
    for li in lst:
        for i in range(10):
            if nums[i] == li:
                counts[i] += 1

    print("#{}".format(tc))

    for i in range(10):  #i에 맞는 카운츠 배열의 값을 뽑아서 카운츠 배열안에 있는 숫자 만큼 반복을 돌린다!
        for j in range(counts[i]): #각 숫자가 몇번씩,,!
            print(nums[i], end=" ")

    print("")

