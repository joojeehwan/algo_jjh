
'''

다음의 순서에 따라 각 위치에 차례대로 값을 넣는다.
1. 첫 번째 숫자인 1을 넣는 위치는 첫 번째 행 가운데이다.
2. 숫자가 N의 배수이면 바로 아래의 행으로 이동하여 다음의 수를 넣고
3. 그렇지 않으면 왼쪽 위로 이동하여 다음의 숫자를 넣는다.
   만약 행이 첫 번째를 벗어나면 마지막 행으로 이동하고,
   열이 첫 번째를 벗어나면 마지막 열로 이동한다.


범위에 row 1- col-1, 즉 '-1' 값을 주어서 2부터 범위 벗어
나는것을 구현할 수 있게 함


재귀방식

/* 채워야 할 위치(x, y)와 값(num)을 전달받아 */
/* 배열에서 해당 위치에 값을 넣고 다음의 위치와 값을 호출하는 재귀함수 */

void fill(int x, int y, int num)
{
    if(num > n * n) return; // 수가 범위를 벗어나면 종료
    if(x < 1) x = n; // x가 0이면 n으로
    if(y < 1) y = n; // y가 0이면 n으로
    arr[x][y] = num; // 배열 채우기

    if(num % n == 0) fill(x + 1, y, num + 1); // num이 n의 배수이면 바로 아래 호출
    else fill(x - 1, y - 1, num + 1); // 아니면 왼쪽 위 호출
}


'''

N = int(input())

MAP = [[0] * N for _ in range(N)]

value = 1
row, col = 0, N // 2
#일단 초기값 넣고 시작
MAP[row][col] = value



#NxN크기의 정사각형을 다 채우면 끝나는거
while value < N**2:
    if value % N == 0:
        #아래로 한칸만 내려가면 된다
        row += 1
        value += 1
        MAP[row][col] = value
        
    else:
        #값이 하나씪 증가하면서 MAP에 담겨야 하니깐
        #전체적으로 한번만 이렇게 증가 시킨 것
        value += 1
        #사각형 범위를 벗어나지 않는다면 왼쪽 대각선 위로
        if 0 <= row-1 < N and 0 <= col-1 < N:
            row -= 1
            col -= 1
            MAP[row][col] = value
        #row가 경계 값을 벗어나는 경우
        elif row-1 < 0 and 0 <= col-1 < N:
            row = N-1
            col -= 1
            MAP[row][col] = value

        elif 0<= row-1 < N and col-1 < 0:
            row -= 1
            col = N-1
            MAP[row][col] = value


for lst in MAP:
    print(*lst)