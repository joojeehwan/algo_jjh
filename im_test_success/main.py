'''


시작점 기준으로 해서 오른쪽에 사각형이 만들어져야 한다.

시작점이 되는 값의 col을 보다 큰 것들의 사격형의 넓이를 구해야함!


1.함수 만들기

2. 함수를 이용해서 전체 행렬에 적용

(1)같은 숫자를 발견하면 그 기준으로 사격형이 들어간 갯수를 구하고, temp에 저장하고
끝까지 돌면서 또 같은 숫자가 나오면, temp에 저정한 값하고 값을 비교한다.
그래서 최대 사각형의 넓이를 구한다.

최대값을 return 하는 함수를 만들면 된다.

(2) 이걸 이차원 배열에 하나씩 다 해본다. why?! 시작점이 다 다르니깐!  그 최대값을 정답 배열에 넣자.

그 정답 배열에서 최대값의 갯수만 구하면 된다.


(3) 한 점에서 최대 크기의 사각형이 2개 생기는건 어떻게 ?!

=> 함수를 구할 때 조작을 해야 될거 같아! 생기는 값마다 다 res에 넣어버리고


'''

# ans = [1,3,4,5]
# 이런식으로 정답의 갯수를 구하자!
# res = max(ans)
#
# print(ans.count(res))



T = int(input())


for tc in range(1, T+1):

    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]

    #이 함수 잘 돌아감.
    def find_max(row, col):

        res = []
        for i in range(row, N):
            for j in range(col, N): #시작점 기준으로 배열을 돌아야 하니깐!
                if j >= col: #col이 나보다 크거나 같아야 해
                    if lst[i][j] == lst[row][col]:
                        max_temp = (j - col + 1) * (i - row + 1)
                        res.append(max_temp)
        return res

    ans = []

    for row in range(N):
        for col in range(N):
            ans.extend(find_max(row, col))

    max_width = max(ans)

    result = ans.count(max_width)

    print(f"#{tc} {result}")




