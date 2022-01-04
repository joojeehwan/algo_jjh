



stack = []

def push(n):

    stack.append(n)

def pop():

    if len(stack) == 0:
        return print("empty")
    print(stack.pop())

def check_data():

    print(len(stack))



T = int(input())

N = int(input())

orders = [input() for _ in range(N)]


print(f"#{T}")

for order in orders:

    if order[0] == "i":
        push(int(order[2]))

    if order == "c":
        check_data()

    if order == "o":
        pop()








# T = int(input())
# for tc in range(T):
#     print("#{}".format(tc + 1))
#     N = int(input())
#     stack = []
#     for i in range(N):
#         order = input().rstrip()
#         if order[0] == "i":
#             b = int(order[2:])
#             stack.append(b)
#         elif order[0] == "o":
#             if len(stack) == 0:
#                 print("empty")
#             else :
#                 print(stack[-1])
#                 stack.pop()
#         else :
#             print(len(stack))