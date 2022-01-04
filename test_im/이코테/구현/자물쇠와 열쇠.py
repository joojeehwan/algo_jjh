
'''

2020 카카오 신입공채




'''


# MAP = [[1,2,3],[4,5,6],[7,8,9]]
# n = len(MAP)
# m = len(MAP[0])
# res = [[0] * n for _ in range(m)]
# for i in range(len(MAP)):
#     for j in range(len(MAP[i])):
#         #print(MAP[3-j-1][i], end = "")
#         res[3-j-1][i] = MAP[i][j]
#     print()
#
# for row in range(n):
#     for col in range(m):
#         print(res[row][col], end= " ")
#     print()
'''
4중 포문 부분을 이해하는게 중요! 
다시 이해해보자
'''

# 2차원 리스트 90도 회전 하게 하는 함수
def rotate_matrix_90_degree(MAP):
    # 행 길이 계산(세로)
    n = len(MAP)
    # 열 길이 계산(가로)
    m = len(MAP[0])
    result = [[0] * n for _ in range(m)]  # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = MAP[i][j]

    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    # 가운데 그 부분까지만 보면 되니깐 이렇게 for문의 범위를 설정하는 것
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 전환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠에 기존의 자물쇠 넣기
    # 여기 인덱스 그대로 둔것은 기존의 배열에서도 인덱스를 조정하니깐 !

    for i in range(n):
        for j in range(n):
            # 중간에 넣어야 하니! 각각의 인덱스에 n을 더해서 중앙으로 들어간것
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인

    for rotation in range(4):
        # 열쇠 회전
        key = rotate_matrix_90_degree(key)
        # 자물쇠 좌표를 하나씩,,!
        #자물쇠 좌표도 움직여야 하고, 열쇠랑 자물쇠 하나하나 매칭해야 하니깐!
        #열쇠의 좌표도 움직여야 하니깐! 4중 포문이 돌아아걍 한다!
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True

                # 자물쇠에서 열쇠를 다시 뺴기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False
