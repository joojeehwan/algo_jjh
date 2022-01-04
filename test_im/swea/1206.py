'''



view


인덱스가 좌우 칸이라 생각하고, value값이 빌딩의 높이라 생각,,!

일차원 배열!


일차원 배열의 값들 중에서, 좌우로 2칸 보았을 때 내가 가장 큰것의 갯수를 찾는다!

5개씩 반복문을 돌리면서 양옆 체크 하면 될거 같은데?!

'''

T = 10

for tc in range(1, T+1):

    N = int(input())

    lst = list(map(int, input().split()))

    sum = 0

    for i in range(2, N-2): #검색할 빌딩 하나 고정,,!

        max_value = 0

        for j in range(-2, 3): #길이 5개씩

            if j != 0 and max_value < lst[i + j]: #j가 0인 부분은 검색안해도 된다!
            #4가지의 경우만 본다!

                max_value = lst[i + j]

        ret = lst[i] - max_value
        
        if ret < 0: #조망권이 없다
            ret = 0

        sum += ret


