'''

1) 허락받고 하자

IF문을 통해서 공백의 유무를 확인하고 읽을 수 있으면 읽고 넘어가기!


2) 허락은 무슨 용서를 구하자!




'''



T = int(input())


for tc in range(1, T+1):

    word = [0] * 5 #일단 5개의 단어를 입력 받으니깐,,! 리스트 내포 방식으로 안할려고!


    max_len = 0

    for i in range(5):
        word[i] = list(input()) #2차원 배열 만들기!

        if len(word[i]) > max_len:
            max_len = len(word[i]) # 리스트 내포 방식을 사용하지 않았기 때문에!
                                    # 바로 들어오는 문자열에 최대길이를 구할 수 있음


    print("{}".format(tc), end = "")

    for i in range(max_len):
        for j in range(5):
            if len(word[j]) > i:
                print(word[j][i], end="")

    print(())
