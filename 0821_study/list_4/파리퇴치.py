


#가장 다중 포문을 이해하기에 좋은...! 고정 돌리기,,! 그리고
# 그 큰 개념을 작은 개념으로 가져와,,! 약간 프렉탈같은 생각!



T = int(input())


for tc in range(1, T+1):


    N, M = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    maxi = 0
    for row in range(N-M+1): #row 세로로 움직임,,!
        for col in range(N-M+1): #col 가로로 움직임,,!
            current = 0
            for k in range(M): #여기 반복이 끝나면 작은 스퀘어 하나의 합이 나옴 그래서,, 커런트를 여기에!
                for l in range(M):
                    current += MAP[col+l][row+k]

            if current > maxi:
                maxi = current

    print('#{} {}'.format(tc, maxi))



