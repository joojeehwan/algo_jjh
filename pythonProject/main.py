
# 수업팁
# 문제 위주로! RUN할때 ... 으로 해야지 다른것도 실행이 된다.


# input은 한줄을 입력 받는다!
# str.split() : 띄어쓰기 단위로 쪼갬

# 인풋 : 한 줄 입력
# 인풋.스필릿 : 한 줄 입력받고 띄어쓰기 단위로 조개기
# map(int, input().split()) 쪼갠 데이터들을 int(정수)로 각각 변환
# list(map(int, input().split())) < 변환 data들을 list형태로 사용

#range(end_index) : 0 ~ end_index -1
#range(start_index, end_index) : start_index ~ end_index - 1


    
# 디버깅 모드 : 코드를 한줄한줄 실행키면서 어떻게 변화하는지 확인하는 작업
# 왓치스 : 원하는 값을 보고 싶은 경우 사용
# 브레이크 포인트 :  디버깅 모드로 실행시 멈출 부분


#디버깅 모드 : 코드를 한줄한줄 실행시키면서 어떻게 변화하는지 확인하는 작업
#Watches : 특정 값들을 확인하고 싶을 때 활용

#break point <- 디버깅 모드로 실행시 멈출 부분 (줄번호 옆 클릭)

# 코드 한줄씩 실행
# step over : F6
# step into : F7

# 커서까지만 실행
# run to cursur : alt + F9

# step out : shift + F8

de = 1 # dummy code : 프로그램이 돌아갈때 영향을 주지 않는 코드
# break point 찍기용


test_case = 1
ans = 5

print("#{} {}".format(test_case, ans))
