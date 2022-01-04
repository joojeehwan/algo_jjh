'''

데이터를 보면서 내가 잘 이해 했는지 확인!

내가 찾아야 하는건 집의 개수,,!
=>

0. 기본적인 입력을 받는다.

1. 기지국을 찾는다..

2. 찾은 기지국을 기준으로 델타배열을 사용하여서
 A,B,C에 맞게 검색을 한다. A는 1칸, B는 2칸, C는 3칸

3. 찾은 집을 CHEECK를 함..

4. MAP을 다시 보면서, 체크되지 않은 집의 갯수를 찾는다!

5. 예외체크,,! 이차원 배열에선 항상 예외를 생각해라! 지도 같은 문제! 델타 배열을 사용하게 되면 예외를 항상 생각!

그냥 아싸리 지워 버리는것도 좋은 방법이구만,,



'''



T  = int(input())


for tc in range(1, T+1):


    N = int(input())

    MAP = [list(input().rstrip()) for _ in range(N)]


    for row in range(len(MAP)):

        for col in range(len(MAP[row])):

            if MAP[row][col] == 'A':

                MAP[row + 1][col] = "x"
                MAP[row][col+ 1] = "x"
                MAP[row-1][col] = "x"
                MAP[row][col-1] = "x"

            if MAP[row][col] == 'B':
                MAP[row + 1][col] = "x"
                MAP[row][col + 1] = "x"
                MAP[row + 1][col] = "x"
                MAP[row][col + 1] = "x"
                MAP[row + 2][col] = "x"
                MAP[row][col + 2] = "x"
                MAP[row - 2][col] = "x"
                MAP[row][col - 2] = "x"

            if MAP[row][col] == 'C':

                MAP[row + 1][col] = "x"
                MAP[row][col + 1] = "x"
                MAP[row + 1][col] = "x"
                MAP[row][col + 1] = "x"
                MAP[row + 2][col] = "x"
                MAP[row][col + 2] = "x"
                MAP[row - 2][col] = "x"
                MAP[row][col - 2] = "x"
                MAP[row + 3][col] = "x"
                MAP[row][col + 3] = "x"
                MAP[row - 3][col] = "x"
                MAP[row][col - 3] = "x"

    cnt = 0
    for row in range(len(MAP)):

        #초기화 안쪽에서 할때는 행별로 카운트 할때! cnt = 0
        for col in range(len(MAP[row])):
            if MAP[row][col] == "H":
                cnt += 1

    print("#{} {}".format(tc, cnt))



