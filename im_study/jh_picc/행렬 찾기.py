



'''

0. 기본 입력


아이디어 생각남!
오른쪽에다가 세로로 0배열을 만들어서 붙인다!

1. 이차원 배열 검색 하닥

2. 숫자가 나온다? 그 나온 순간을 기점으로 오른쪽 으로 이동,, 0만날때까지!

3.




어렵다,,,!!!!
생각을 배우자!!

스킬이랑!!


괜찮다아!! 긍정적인 생각을 가지자!
'''




#옆으로 어디까지 갈 수 있나 체크!

# 이렇게! 뭐랄까! 반복의 범위가 정확히 주어진게 아니라! 어떤 특정 조건을 만족하면 이루어지는 경우는 for 보다는 while이 낫다!
# 즉, 해당 목표를 이루기까지 정확한 반복의 횟수를 모른다면! while이 나은거야!! ,,, 오,,,


import sys
sys.stdin = open("행렬찾기_input.txt")

def width(i, j): #행렬의 시작점을 알아서 넣는다면,,,?! 그 생각에서 시작!

    count = 1 #일단 그 점에 들어가기만 해도 길이는 1이니깐! 길이라서,,!

    col = j
    while True : # while의 쓰임,,!

        col += 1 #오른쪽으로 이동하면서! 확인해보는 것! 브레이크 조건을 만족시키는,,!!

        if col >= N: #범위를 벗어나는 예외 조건 만나면 멈춰!
            break

        if MAP[i][col]: #0이 아닌 값이 있다면!
            count += 1

        else: # 0을 만나면 멈춰! => 원하는 구간의 길이가 아니니깐!
            break

    return count


#아래로 얼마나 갈 수 있난 길이 체크

def height(i, j):
    count = 1 #길이라서,,!

    row = i #할당

    while True : #와일 트루 => 브레이크 문 생각

        row += 1 #로우를 증가시키면서,,! 브레이크문!

        if row >= N : # 로우가 n보다 커지면 장외니깐 !
            break

        if MAP[row][j]:
            count += 1

        else: #로우에 값이 없어도 나가라!
            break
    return count



#이미 체크한 영역은 다시 검사하지 않기 위해 0으로 바꿈!

def change(row, col, row_h, col_w): # 벌어진 가로길이와 세로길이

    for i in range(row, row_h): #위의 함수를 보면 count = 1시작해서! 자연스럽게 길이라서 +1 을 해준다! 그래서 row_h + 1을 할 필요가 없다!
        for j in range(col, col_w):
            MAP[i][j] = 0
            #두 점의 범위를 아니깐!



T = int(input())

for tc in range(1, T+1):

    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for row in range(N):
        for col in range(N):
            # 값이 있다면!
            if MAP[row][col]: #가로축 검색 하면서! 값이 보이면! 그것이 시작점!!
                #가로 길이 받아오기!
                w = width(row, col)

                #세로 길이 받아오기
                h = height(row, col)

                #확인한 것은 0으로 바꾸기!
                change(row, col, row+h, col+w)
                #문제에서 원하는! 행렬 크기 넣어주고, 곱한 값 넣어주고
                ans.append([h, w, h*w])

    ans = sorted(ans, key = lambda x: (x[2], x[0])) #이렇게 하나 배워가네,, 2개의 기준으로 정렬하는 람다식! 정렬이 되는 대상을 리스트에 넣어두고!  x[2] 에다가 "-" 붙이면 내림차순

    print("#{} {}".format(tc, len(ans)), end = " ")
    #그리고 정답 배열에 있는 것 출력하기!
    for row, col, _ in ans:   # _ 이거 하는 이유는 안에 값이 3개가 있으니깐! 안쓰니깐 저렇게 둔것! 두개만 사용할려고!
        print("{} {}".format(row, col), end = " ")
    print()






