# 단순 2진 암호코드

def find_end(): #거꾸로 도는 for문!
    for row in range(height - 1, -1, -1):
        for col in range(width - 1, -1, -1):
            if MAP[row][col] == "1":
                return row, col
    return -1, -1

def check(end_row, start_col):
    DAT = {13:0, 25:1, 19:2, 61:3, 35:4, 49:5, 47:6, 59:7, 55:8, 11:9}
    cnt = 1
    sum = 0
    ret = 0
    for col in range(start_col, start_col + 56, 7):
        #col 각 암호 숫자 코드의 시작점
        num = int(MAP[end_row][col : col + 7], 2) # 암호 숫자 코드의 10진수 값
        if not num in DAT:
            return 0
        else :
            num = DAT[num] # 암호 숫자 코드를 본래 수로 복구
        if cnt % 2 == 1: # 홀수 자리
            sum += num * 3
        else : # 짝수 자리
            sum += num
        ret += num
        cnt += 1
    if sum % 10 == 0: # 정상
        return ret
    else : # 오류
        return 0


t = int(input())
for tc in range(t):
    height, width = map(int, input().split())
    MAP = [ input().rstrip() for _ in range(height) ]
    end_row, end_col = find_end()
    start_col = end_col - 55
    print(f"#{tc + 1} {check(end_row, start_col)}")