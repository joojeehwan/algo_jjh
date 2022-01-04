



sentence = "4100112380990844"


T = 10

for tc in range(1, T+1):
    N, sentence = input().split()
    stack = []

    for i in range(len(sentence)):

        if stack and stack[-1] == sentence[i]:
            stack.pop()

        else:
            stack.append(sentence[i])

    print(f"#{tc} {''.join(stack)}")