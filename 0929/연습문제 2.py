'''


데이터 처리가 중요,,

'''

#000011111001011110100011 입력

# 연습문제 2
data = input().rstrip()
length = len(data) * 4  # 2진수로 나와야할 길이
data = int(data, 16)  # 10진수
print(data)
data = bin(data)[2:]  # 2진수 문자열
print(data)
# length - len(data) # 앞에 0이 붙어야하는 개수
data = "0" * (length - len(data)) + data

print(data)
for pos in range(0, len(data), 7):
    if pos + 7 > len(data):
        now = int(data[pos:], 2) # 뒤에 마지막 3개를 처리하는 방법!
    else:
        now = int(data[pos: pos + 7], 2)
    print(now)