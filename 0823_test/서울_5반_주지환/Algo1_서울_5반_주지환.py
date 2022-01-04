

T = int(input()) #테스트 케이스의 입력을 받는다.

for tc in range(1, T+1): #주어진 테스트 케이스의 수만큼 반복을 돌린다

    N, M = map(int, input().split()) #N, M을 입력받는다

    lst = list(map(int, input().split())) #주어진 배열을 입력 받는다

    print("#{}".format(tc), end=" ") #출력을 하기 위한 프린트 문을 작성한다.
    for i in range(N - M + 1): #M의 크기를 고려하여 시작 인덱스를 결정한다.

        max_ = 0 #초기 최대값을 설정
        min_ = 10001 #초기 최소값을 설정

        for j in range(3): #M의 길이 만큼 반복을 돌린다.
            if lst[i+j] > max_ : #최대값을 구한다
                max_ = lst[i+j]

            if lst[i+j] < min_ : #최소값을 구한다.
                min_ = lst[i+j]

            res = max_ - min_ #둘의 차이를 구한다.


        print("{}".format(res), end = " ") #출력에 맞게 프린트문을 작성

    print("") #출력에 맞게 프린트문을 작성

