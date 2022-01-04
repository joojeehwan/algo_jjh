'''


익스클르시브 오어! 사용!


한자리를 토글?

그 한ㅈ자리만 1로 하고 옮겨가면서 익스클로시브 오어!



이진수 바꾸기

1. tmp = 0

tmp = tmp*2 + i

i
1 0 1 0


2. int("이진수" , 2) => 이 방법으로 풀어보자 나는!


3. enumerrate

0 1 0 1
2의 영승, 2의1승 , 2의 2승 ,2의 3승

tmp += i * (n진수 ** 승)


하나의 비트 빼고 더하기,,!

1 0 1 0 에서 오른쪽 1을 0으로 바꿀려하면!

10 - 2*1(지금의 값을 뺴고) + 2*0(바꾸려는 값을 더한다)


'''


T = int(input())

for tc in range(1, T+1):

    binarys = input()
    ternary = input()



    #2진수로 만들 수 있는 수
    sub_set = set()
    for idx, binary in enumerate(binarys):
        if idx == 0:
            continue
        else:
            if binary == '1':
                #그 앞까지의 인덱스를 가져와서 1이 아닌 0으로 바꾸기
                tmp = int(binarys[:idx] + '0' + binarys[idx + 1:], 2)
            else:
                # 그 앞까지의 인덱스를 가져와서 0이 아닌 1으로 바꾸기
                tmp = int(binarys[:idx] + '1' + binarys[idx + 1:], 2)
            sub_set.add(tmp)

    #3진수로 만들 수 있는 수
    for idx, tri in enumerate(ternary):
        if tri == '0':
            tmp1 = int(ternary[:idx] + '1' + ternary[idx + 1:], 3)
            tmp2 = int(ternary[:idx] + '2' + ternary[idx + 1:], 3)
        elif tri == '1':
            tmp1 = int(ternary[:idx] + '0' + ternary[idx + 1:], 3)
            tmp2 = int(ternary[:idx] + '2' + ternary[idx + 1:], 3)
        else:
            tmp1 = int(ternary[:idx] + '0' + ternary[idx + 1:], 3)
            tmp2 = int(ternary[:idx] + '1' + ternary[idx + 1:], 3)

        #2진수에 들어있는 값과 비교
        if tmp1 in sub_set:
            ans = tmp1
            break
        elif tmp2 in sub_set:
            ans = tmp2
            break


    print(f"#{tc} {ans}")




##############################


'''


마지막 부분!!
중복된 녀석을 잡아온다,,!! 약간 그런식의 풀이! 



'''








