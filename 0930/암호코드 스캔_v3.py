# 암호코드 스캔
code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def check_code(data, size):
    # data : size * 56개짜리 bits
    # check_code : data가 코드로 변환이 가능한가?(검증 X)
    data = data[::size]  # 56개 bits로 이루어진 data(size만큼 확장되기 전의 코드)
    ret = []  # 복구해준 수들을 저장
    for pos in range(0, len(data), 7):
        # pos : data에서 1개의 수가 시작할 수 있는 위치
        temp = data[pos: pos + 7]  # 7개 bit추출
        if temp not in code:
            return 0  # code로 복구가 안된다.
        else:  # code로 복구가 가능한 상황
            ret.append(code[temp])
    return tuple(ret)  # 8개짜리 정상적으로 복구된 하나의 code를 반환

    """
    data의 7개씩의 bits들이 code로 복구가 되는가?
    8개가 복구 잘 된다면 data는 코드로 변환이 가능한 부분

    - 같이하면 좋은 것
    8개로 복구한 수 <- 반환
    """


T = int(input())

for tc in range(T):
    height, width = map(int, input().split())
    lines = set()


    for _ in range(height):
        temp = input().rstrip('0')
        if temp == "":
            continue
        lines.add(bin(int(temp, 16))[2:].rstrip('0'))
        # 1. 16진수 상태로 뒤에 0을 제거
        # 2. 16진수 -> 10진수
        # 3. 10진수 -> 2진수
        # 4. 2진수 상태로 뒤에 0을 제거
        # 5. 중복 데이터 제거
    codes = set()
    for line in lines:
        # line <- 7개가 1개의 수, 14개가 1개의 수, 21개가 1개의 수
        size = 1
        while line:  # line에 모든 bit들이 지워질때까지 진행(모든 code를 찾을 때까지)
            line = line.zfill(size * 56)  # 왼쪽의 0을 복구
            last = len(line)
            guess = line[last -size * 56:]
            # size * 7이 1개의 수, 1개의 코드는 8개의 수, 총 size * 7 * 8bits가 1개의 코드
            # code라고 가정할 bits

            # guess가 1개의 코드가 되는가?
            num_set = check_code(guess, size)  # 코드로 변환이 가능한지 판별하여 그 결과를 받아옴

            if num_set == 0:  # 정상적으로 복구가 안된
                size += 1  # size를 늘려서 다시 복구해보도록 진행
            else:  # 정상적으로 복구
                codes.add(num_set)  # 복구된 code를 기록
                line = line[:-size * 56].rstrip('0')
                size = 1
                # 복구한 code부분 삭제
                # 다음 코드 위치 찾기(오른쪽의 0들을 전부 삭제)
            """
            if 코드로 변환이 가능하면 <-
                codes.add(guess) # 다른줄의 같은 코드를 다시 계산하지 않도록 set에 등록

                --- 같은줄의 다른 코드를 찾기 위해 ----
                line에서 guess만큼의 data를 삭제
                삭제한 line에서 rstrip('0')으로 오른쪽의 0들 삭제
            """
    answer = 0
    for code in codes:
        result = 0
        temp_ans = 0
        for i in range(len(code)):
            if i % 2 == 0:
                result += int(code[i]) * 3
            else:
                result += int(code[i])
            temp_ans += int(code[i])
        if result % 10 == 0:
            answer += temp_ans
    print("#{} {}".format(tc, answer))