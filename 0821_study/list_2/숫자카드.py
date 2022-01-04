import sys

sys.stdin = open("number_card_input.txt")






T = int(input())


for tc in range(1, T +1):


    N = int(input())

    res = list(map(int, input()))

    max_number_count = [0] * 10 #소트 카운트에서 idea를 얻어서! 풀이!


    for i in range(len(res)):

        max_number_count[res[i]] += 1

    max_idx = 0  #카운트의 인덱스가 곧 숫자 이기때문에! 그래서 숫자를 구하기 위해서 idx를 구하는 것!
    max_number = max_number_count[0] #그 숫자의 값을 구하며 ㄴ그것이 바로 카드가 몇장인지 구하는 것!

    for i in range(len(max_number_count)): #여기서 "=" 요곳이 중요함!
        if max_number_count[i] >= max_number_count[max_idx]:
            max_idx = i #인덱스 최대값

        if max_number_count[i] > max_number:
            max_number = max_number_count[i]
            # 실제 값 최대값
    print(f"{tc} {max_idx} {max_number}")


    T = int(input())

    for tc in range(T):

        N = int(input())

        cards = int(input())
        card_li = [0] * 10

        max_value = -1
        max_index = -1

        for i in range(N):

            card = cards % 10 #1의 자리 숫자 추출
            cards //= 10 #1의 자리 숫자 삭제,, 즉 다음 1의 자리를 가보자아!
            card_li[card] += 1

            if card_li[card] > max_value:
                max_value = card_li[card]
                max_index = card
                
            if card_li[card] == max_value and max_index > card :
                max_index = card #개수가 같으면 더 큰 번호가 답

            print("#{} {} {}".format(tc + 1, max_index, max_value))


