'''


연속인 숫자가 3개 이상? run

같은 숫자가 3개 이상? triple

1. 입력 -> p1, p2로 나누기 입력 받은 것

2. 함수로 트리플 런 체크

'''


def check(cnt_li): #player 마다 확인해야 하기떄문에 함수로 만들어서 하는 것이 좋음
    i = 0
    while i < 10:
        if cnt_li[i] >= 3:  #트리플 확인
            return 1

        #run확인!
        if i < 8 and cnt_li[i] >= 1 and cnt_li[i+1] >= 1 and cnt_li[i + 2] >= 1:
            return 1

        i += 1

    return 0


T = int(input())


for tc in range(1, T+1):

    lst = list(map(int, input().split()))
    p1 = []
    p2 = []

    count1 = [0] * 10
    count2 = [0] * 10
    # 입력
    for i in range(len(lst)):

        if i % 2 == 0 :
            p1.append(lst[i])
        else:
            p2.append(lst[i])

    # 카운트 배열 만들기! => run 과 트리플릿을 결정지을!
    for i in range(6):
        count1[p1[i]] += 1
        count2[p2[i]] += 1

        if i > 2 and check(count1): #적어도 2장은 넣고 3번째 넣었을 때 승패가 결정되니깐!
            print(f"#{tc} 1")
            break

        elif i > 2 and check(count2):
            print(f"#{tc} 2")
            break

    else: #for - else 구문 break없이 빠져 나오는 것들에 대한 처리 => 비김 처리!
        print(f"#{tc} 0")







