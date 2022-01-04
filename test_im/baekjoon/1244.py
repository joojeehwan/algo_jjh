'''



스위치 켜고 끄기




남학생(1) : 받은 수의 배수, 스위치 상태 변경

여학생(2) : 받은 수의 좌우로 대칭상태를 파악 -> 대칭 상태인 부분에 대해서 스위치 상태 변경

만약에 대칭이지 않으면 내가 받은 번호만 스위치 상태를 변경



'''


light_num = int(input())

#1부터 사용하는 문제의 조건을 맞추기 위해서
lst = [-1] + list(map(int, input().split()))

student_num = int(input())

student = [list(map(int, input().split())) for _ in range(student_num)]


for stu_info in student:

    if stu_info[0] == 1: #남학생이라면
        #자기가 받은 수  부터 전구의 갯수 맘큼,, 배수만큼 증가하면서! 전구ㅡㄹ 킨다.
        for i in range(stu_info[1], light_num+1, stu_info[1]):

            if lst[i] == 0:
                lst[i] = 1

            else:
                lst[i] = 0

    else:
        #여학생이라면 
        # #여기서 인덱스 에러가 나나보다,,
        # if lst[stu_info[1]-1] != lst[stu_info[1]+1]:

        if lst[stu_info[1]] == 1: # 여학생이 일단 선택되면 일단 자기 자신은 바꾸니깐

            lst[stu_info[1]] = 0

        else:
            lst[stu_info[1]] = 1

        for k in range(light_num // 2):
            #탐색의 범위 설정,,!
            #중간 값부터 인덱스의 값을 증가 시키면서(for문을 통해 증가 시킴)
            
            #범위 넘어서는 것 제외
            if stu_info[1] + k > light_num or stu_info[1] - k < 1:
                break
            #
            if lst[stu_info[1] + k] == lst[stu_info[1] - k]:

                if lst[stu_info[1] + k] == 1:

                    lst[stu_info[1] + k] = 0

                else:
                    lst[stu_info[1] + k] = 1

                if lst[stu_info[1] - k] == 1:
                    lst[stu_info[1] - k] = 0

                else:
                    lst[stu_info[1] - k] = 1
            else:
                break #초장 부터 다른 경우도 그냥 탐색 돌면 안돼! 첫 비교부터 다르다?! nreak


for i in range(1, light_num+1):
    print(lst[i], end = " ")
    if i % 20 == 0 :
        print()






