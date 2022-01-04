

'''

0과 1로 이루어진 1차 배열에서 7개 비트를 묶어서 10진수로 출력하기


'''

# 입력



#연습문제3
DAT = {int("001101",2) : "0",
       int("010011", 2) : "1",
       int("111011", 2) : "2",
       int("110001", 2) : "3",
       int("100011", 2) : "4"
       }

data = int(input().rstrip(), 16)
# print(data)
data = bin(data)[2:]
print(data)
end_pos = len(data) - 1 # 1이 위치한 맨 뒷 위치
print(f"ENDPOS : {end_pos}")
while end_pos >= 0 and data[end_pos] != "1": # 1을 찾는 알고리즘
    end_pos -= 1

while True:
    if end_pos - 5 >= 0:
        now = int( data[end_pos - 5 : end_pos + 1], 2)
        print(now)
    else :
        now = int(data[: end_pos + 1], 2)
        print(now)
        #now = "0"*(6 - (end_pos + 1)) + data[: end_pos + 1]
    if now in DAT: #dat안에 now가 있는지 확인 하는 in!
        print(DAT[now])
    else:
        break
    end_pos -= 6 #다음 앤드 포스로 가야지! 뒤에서 앞으로 다른 패턴 확인하러!