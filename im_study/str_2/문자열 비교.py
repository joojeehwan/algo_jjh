



T = int(input())


for tc in range(1, T+1):

    patt = input()
    text = input()

    flag = 0

    for i in range(len(text) - len(patt) + 1):

        cnt = 0
        for j in range(len(patt)):
            if text[i+j] == patt[j]:
                cnt += 1

        if cnt == len(patt):
            flag = 1 #찾았다!

    print("#{} {}".format(tc, flag))



