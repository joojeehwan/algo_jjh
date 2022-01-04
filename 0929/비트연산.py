'''


& 연산
- 0번 비트의 연산의 결과가 0이면 짝수 , 1이면 홀수 
- 특정 비트를 0으로 만드는 연산도 가능


| 연산
- 특정비트를 1로 만드는 연산


^ 연산
1) 비트 반전 => "0 또는 1이 채워진 1차원배열," 주어진 index에 대해 0 -> 1로 바꾸고 , 1을 0으로 바꾸는 그런 문제에서!

2) 비교 => 다르면 0이 아니고, 같으면 0




<< 연산
- 한칸 이동 -> 곱하기 2

>> 연산

- 한칸 디오 -> 나누기 2



1 << N

- 2^N 값을 갖는다.


사진 확인

'''



a = 2
b = 3
c = 3

#& 연산 => 홀짝 구분

if a & 0x01 : #0이 아니면
    print("홀수")
    
else:
    print("짝수")


#^ 연산 - 비교

if b^c  == 0:
    print("같음")



#^ 연산 - 비트반전

a = [1,0,0,1,1,0,0,0]
b = [0,1,2,7] #0, 1, 2, 7번 인덱스를 바꾸겟네!


for i in b:
    a[i] ^= 1

print(a)




for i in range(1 << 3): # 이것의 범위는 1000(2) - 1(2) 인것!
    if i & 1<<0: #i의 0번 비트의 값이 0이 아니면
        print(f"{i}의 0번 비트는 1")

    else:
        print(f"{i}의 0번 비트는 0")


for i in range(1 << 3): # 이것의 범위는 1000(2) - 1(2) 인것!
    print(f"{i}의 2번 비트는 {(i&(1<<2))>>2}")

    '''
    3210 비트
    
    0111
    0100
    ----
    0100
    
    '''
    
    
'''

16진수 한자리는 2진수 4자리로 표현이 

=> 16진수 2자리는 1바이트!  

16진수 :  0 ~ 9 A(10) ~ F(15)


'''


# def Bbit_print(i):
#     output = ""
#     for j in range(7, -1, -1):
#         output += "1" if i & (1 << j) else "0"
#     print(output, end = " ")
#
#
# a = 0x10
# x = 0x01020304
#
# print("%d = " %a, end = "")
# Bbit_print(a)
# print()
# print("")
# print("0%x = "%x, end = "")
# for i in range(0, 4):
#     Bbit_print((x >> i*8) & 0xff)
# #0xff = 11111111


#


def ce(n): # change endian

    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p



x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)


# 4 3 2 1
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))

p = ce(x)

#1 2 3 4
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))


#배열에 넣지 않고 바이트 단위로 뒤집는 것!

# 01 02 03 04 -> 04 03 02 01


def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)
