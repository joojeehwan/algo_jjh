'''


<분할 정복의 활용>
병합정렬

퀵정렬,,

=> 파티셔닝? 피봇의 위치를 결정0


호모 파티션 : 와일문이 2개 i j가 양뱡향으로 이동 (대표)


루모토 파티션 : for문이 하나네?! (이것도 알면!) 단방향!

이해는 되었다! 실력이 늘었네,, 나도,,




진짜 프로구램들은ㅇ 병합과 퀵이 최악의 경우 n제곱 시간이 걸리 수잇으니
합쳐서 사용한다!ex) 파이썬의 경우 tim sort


------------------------------------------------------------


백 트래킹(dfs + 가지치기)

아 오늘 다시 앤 퀸 꼭 풀어야지! 


'''

# test case 생성
import sys


# 랜덤
for test in range(10):

    sys.stdout = open(str(test) + ".txt", "w")

    H, W = 50, 50
    print(H,W)
    MAP = [[0] * (W) for _ in range(H)]

    for i in range(W):
        for j in range(H):
            MAP[i][j] = (i + j + 3 + test) % 10
            if MAP[i][j] == 0:
                MAP[i][j] = 'H'
            else:
                MAP[i][j] = str(MAP[i][j])

    for i in range(H):
        print("".join(MAP[i]))