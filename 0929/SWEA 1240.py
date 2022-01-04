'''



뒤에서 가다가 1 만나면 그떄부터!!


연습문제 3을 이차원으로 확장했다고 생각,,,



이차원 배열을 뒤 부터 검사하면서 1이 오면 멈추자! 그곳 부터 56개 앞으로가 하나의 암호코드!

이 암호코드를 다시 7개씩 8개로 나누어서! 패턴하고 비교하면 된다!


근데 굳이 앞으로 갈 필요가 있나?! 앞에서 부터 가서 암호 코드 하나씩 가져오면 되자나?!


어차피 한줄만 알면 나머지는 다 같으니깐,,! 굳이 뒤에서 부터 올필요가 없어 보인다.


아아 앞에서 하면! 안되는구나,,!! 저게 길이를,,!! 없는 패턴을 넣을 수가 있다!

괜히 그냥 뒤에서 부터 하라는 것이 아니것음! 일단 1을 만나면
'''


import sys
sys.stdin = open("swea1240.txt")



def change(number):
    DAT = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }
    return DAT[number]



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input())) for _ in range(N)]



    start_idx = 0
    start_line = 0

    #다중 포문 탈출하기


    #바보 같았다. 저거 계속 포문 돌리고 있으면,, 계속 갱신하면서 도니깐! 마지막으로 간 것!
    #지금까지 중복된 값 없이 하나의 값만 찾아서 익숙하지 않았다. 이렇게 안게 다행!
    #flag를 활용한 이중포문 탈출하기 좋았다?!
    # flag = True
    # for i in range(N):
    #      for j in range(M):
    #          if MAP[i][j] == 1:
    #             start_line = i
    #             start_idx = j-1 #0까지 포함 시켜야 하니깐!
    #             flag = False
    #             break
    #      if flag == False:
    #          break

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                start_line = i
                start_idx = j  # 0까지 포함 시켜야 하니깐!

    password = MAP[start_line][start_idx - 55  : start_idx + 1]


    #이제 password를 7개씩 나누자! 이거는 str part에서 많이 했던 것!

    res = ""
    for i in range(0, len(password), 7):
        temp = ""
        for j in range(i, i+7):
            temp += str(password[j])
        res += change(temp)

    # print(res)

    #이제 주어진 조건에 맞게 수식 처리!

    even_sum = 0
    odd_sum = 0

    for i in range(7):
        if i % 2 == 0:
            even_sum += int(res[i])

        else:
            odd_sum += int(res[i])

    total = (even_sum * 3) + odd_sum + int(res[7])

    if total % 10 == 0:
        print(f"#{tc} {even_sum + odd_sum + int(res[7])}")
    else:
        print(f"#{tc} 0")



