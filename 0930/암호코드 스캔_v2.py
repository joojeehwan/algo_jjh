code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def check_code(data, size):
    # data : size * 56개짜리 bits
    # check_code : data가 코드로 변환이 가능한가?(검증 X)
    data = data[::size]  # 56개 bits로 이루어진 data(size만큼 확장되기 전의 코드)

    """
    data의 7개씩의 bits들이 code로 복구가 되는가?
    8개가 복구 잘 된다면 data는 코드로 변환이 가능한 부분

    - 같이하면 좋은 것
    8개로 복구한 수 <- 반환
    """


# T = int(input())
#
# for tc in range(T):
#     height, width = map(int, input().split())
#     lines = set()
#     for _ in range(height):
#         temp = input().rstrip('0')
#         if temp == "":
#             continue
#         lines.add(bin(int(temp, 16))[2:].rstrip('0'))
#         # 1. 16진수 상태로 뒤에 0을 제거
#         # 2. 16진수 -> 10진수
#         # 3. 10진수 -> 2진수
#         # 4. 2진수 상태로 뒤에 0을 제거
#         # 5. 중복 데이터 제거
#     codes = set()
#     for line in lines:
#         # line < - 7개가 1개의수, 14개가 1 개의 수, 21개가 1 개의 수
#         size = 1
#         while line:  # <--- True나중에 바꿔줘야함
#             last = len(line)
#             guess = line[last - size * 56:]
#             # size * 7이 1개의 수, 1개의 코드는 8개의 수, 총 size * 7 * 8bits가 1개의 코드
#             # code라고 가정할 bits
#
#             # guess가 1개의 코드가 되는가?
#             check_code(guess, size)  # 코드로 변환이 가능한지 판별
#             if 코드로 변환이 가능하면 < -
#             codes.add(guess)  # 다른줄의 같은 코드를 다시 계산하지 않도록 set에 등록
#             --- 같은줄의 다른 코드를 찾기 위해 - ---
#             line에서 guess만큼의 data를 삭제
#             삭제한 line에서 rstrip('0') 으로 오른쪽의 0들 삭제