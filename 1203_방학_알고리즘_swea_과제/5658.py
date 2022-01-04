


T = int(input())

for tc in range(1, T+ 1):

    N,  K = map(int, input().split())
    #문자로 하나씩 리스트에 담는,,!
    #['1', 'B', '3', ,,] 이런식으로 담는다.
    lst = list(input())

    words = []
    word_len = N // 4

    #리스트 회전,,!
    # 이중 포문을 통해서 모든 4개씩 다 보는 것!
    for _ in range(N):
        #안에서의 for문으로 
        for j in range(0, N, word_len):
            #글자 3개씩 확인 by using 슬라이싱
            word = "".join(lst[j:j+word_len])
            word_to_num = int(word, 16)

            #중복으로 세지 않기 위해서!
            if word_to_num not in words:
                words.append(word_to_num)

        #뒤에것 옮겨서 앞으로! 이동 시키는 부분
        temp = lst.pop()
        lst.insert(0, temp)
        #lst = lst[lst[-1]] + lst[:-1]
        #pop -> insert를 위에 처럼도 가능
    #아 이렇게 출력하는 것도 익숙해져야 한다,,! 오케이?!
    #sorted의 대상 자체가 배열이라 인덱싱이 가능한 것
    print(f"{tc} {sorted(words, reverse=True)[K-1]}")





