# 풀이 3가지 볼 수 있음,,! 오 좋구만,,!




#1 내풀이

#갈 수 없는 : 0 / 갈 수 있는 : 1
import sys

sys.stdin = open("where_word_input.txt")


T = int(input())

for tc in range(1, T+1):

    N, K  = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    total = 0

    #행우선
    for row in range(N):
        count = 0 # 행하나 고정하고, 거기서 아래의 반복문 끝나는 값들을 갱신해야 하니깐!
        for col in range(N):
            if matrix[row][col] == 0 : #검은색 부분 갈 수 없다.
                if count == K: #검은색인 부분까지 갔는데, k와 count가 같다면!
                    total += 1 #찾고자 하는 값을 하나 증가 시키고,
                count = 0 # 그게 아니라면 count 값을 초기화 시키고 다음 반복을 준비,,!

            else: # 흰 부분 이니깐 count 증가 시킨다.
                count += 1

        #밑에 경우는 검은거 안만나도, 그냥 처음부터 끝까지 갔기 때문에 보는 경우!
        if count == K:
            total += 1


    #열우선

    for row in range(N):
        count = 0
        for col in range(N):
            if matrix[col][row] == 0:
                if count == K:
                    total += 1
                count = 0

            else:
                count += 1

    print("#{} {}".format(tc, total))
                


    #열우선

#2 담당 교수님 풀이




T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    #가로

    for row in range(N):
        length = 0
        for col in range(N): #이거는 내 풀이와 반대로,,! 적을 수 있는 것 부터 생각!
            if MAP[row][col] == 1: #갈 수 있는 곳!
                length += 1
                if col + 1 == N or MAP[row][col +1] == 0: # 단어의 끝인가? / 뒤에가 벽인가?
                    if length == K:
                        ans += 1
            else:
                length = 0 #벽을 만났으면 길이를 다시 초기화 하고 다음 반복을 해야 하기 때문에!

        # 세로
    for col in range(N):
        length = 0
        for row in range(N):
            if MAP[row][col] == 1:
                length += 1
                if row + 1 == N or MAP[row + 1][col] == 0:
                    if length == K:
                        ans += 1
            else:
                length = 0
    print("#{} {}".format(tc + 1, ans))