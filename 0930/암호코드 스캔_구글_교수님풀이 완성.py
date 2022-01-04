# decode = {'112':0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}
# hex_to_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
#
#
# def examine(arr):
#     if ((arr[7]+arr[5]+arr[3]+arr[1])*3 + arr[0]+arr[2]+arr[4]+arr[6]) % 10:
#         return False
#     return True
#
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     big_code = [input()[:M] for _ in range(N)]
#     visited = []
#     ans = 0
#     for n in range(N):
#         binarified = ''
#         for char in big_code[n]:
#             binarified += hex_to_bin[char]
#         big_code[n] = binarified
#     res = []
#     for n in range(N):
#         f1 = f2 = f3 = 0
#         if '1' not in big_code[n]:
#             continue
#         for m in range(M*4-1,-1,-1):
#             if f2 == 0 and f3 == 0 and big_code[n][m] =='1':
#                 f1 += 1
#             elif f1 and f3 == 0 and big_code[n][m] == '0':
#                 f2 += 1
#             elif f1 and f2 and big_code[n][m] == '1':
#                 f3 += 1
#             elif f3 and big_code[n][m] == '0':
#                 mul = min(f1, f2, f3)
#                 res.append(decode[str(f1//mul)+str(f2//mul)+str(f3//mul)])
#                 f1 = f2 = f3 = 0
#                 if len(res) == 8:
#                     if res not in visited:
#                         if examine(res):
#                             ans += sum(res)
#                         visited.append(res)
#                     res = []
#     print('#{} {}'.format(test_case, ans))


# 암호코드 스캔

import sys

sys.stdin = open("swea_1242.txt")

code_nums = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def check_code(data, size):

    data = data[::size]
    ret = []
    for pos in range(0, len(data), 7):
        temp = data[pos: pos + 7]
        if temp not in code_nums:
            return 0
        else:
            ret.append(int(code_nums[temp]))
    return tuple(ret)


T = int(input())

for tc in range(T):
    height, width = map(int, input().split())
    lines = set()


    for _ in range(height):
        temp = input().rstrip('0')
        if temp == "":
            continue
        lines.add(bin(int(temp, 16))[2:].rstrip('0'))

    codes = set()
    for line in lines:
        size = 1
        while line:
            line = line.zfill(size * 56)  # 왼쪽의 0을 복구
            last = len(line)
            guess = line[last - size * 56:]
            num_set = check_code(guess, size)  # 코드로 변환이 가능한지 판별하여 그 결과를 받아옴
            if num_set == 0:
                size += 1
            else:
                codes.add(num_set)  # 복구된 code를 기록
                line = line[:-size * 56].rstrip('0')
                size = 1
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
    print("#{} {}".format(tc+1, answer))
