'''

와 이거 어려운데,,!


어떻게 출력해야 삼각형을 만들지?!


와 그러네,, 공백이라고 생각하는구나,,!

'''

# n = int(input())
#
# char = ord("A")
#
# for i in range(1, n+1):
#
#     # 공백을 출력하기 위한 for문
#     for k in range(n- i + 1):
#         print(" ", end = " ")
#
#     # 문자를 출력하기 위한 for문
#     for _ in range(0, i):
#         print(chr(char), end=" ")
#         char += 1
#
#     print()

# n = int(input())
#
# MAP = [[0] * n for _ in range(n)]
#
# char = ord("A")
#
# for i in range(1, n+1):
#
#     for j in range(i, n+1):
#
#         n -= 1
#         MAP[j][n] = chr(char)
#         char += 1
#
#         if char >= ord("Z") + 1:
#             char = ord("A")
#

n = int(input())

char = ord("A")
arr = [[" "] * n for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        arr[j][n-1-j+i] = chr(char)
        char += 1

        if char >= ord("Z") + 1:
            char = ord("A")

for row in range(n):
    for col in range(n):
        print(arr[row][col],  end= " ")
    print()
