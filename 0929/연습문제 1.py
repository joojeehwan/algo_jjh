#연습문제1

# 0000000111100000011000000111100110000110000111100111100111111001100111



data = input().rstrip()

print(data)

#pos는 왼쪽부터 7개씩 묶어을때의 시작 비트
for pos in range(0, len(data), 7):



    # now = int(data[pos: pos + 7 ], 2)
    #
    #
    #
    # print(now)

    now = int(data[pos: pos + 7])
    print(data[pos: pos + 7], end = " : ")
    temp = 0 # 2진수로 만든 수
    for i in range(7):
        temp += (now % 10) * (1 << i) # 이진수의 값을 10진수로 바꿔서 더하는데! 자릿수 값을 곱해야 하니깐!
        now //= 10
        #print("temp : ", bin(temp))
        #print("now : ", bin(now))
    print(temp)




# K = 548
# N = 10
#
# for _ in range(3):
#     print(K % N)
#     K = K // N
#
# print(K)


'''

진수 <-
어떤 정수 k에서 n진수씩 각 자리의 수들을 뽑아오고 싶은 경우
k % n <- 1의 자리 1개 추출
k // n <- 1의 자리 삭제
10진수 10
1010 % 2 <- 0
1010 // 2 <-
101 % 2 <- 1
101 // 2
10


100111100 <- 10진수


'''