inputValue = input()
x = int(inputValue.split(' ')[0]) #공백을 기준으로 나누어서 앞에숫자는 x
y = int(inputValue.split(' ')[1]) #공백을 기준으로 나누어서 뒤에숫자는 y

for idx in range(abs(x - y)+1):
    if x-y > 0: idx = idx * -1 # 이 조건을 활용해서! 구구단의 오름차순 내림차순을 결정!
    for num in range(1, 10):
        print(f"{x + idx} * {num} = {str((x + idx) * num).rjust(2)}   ", end="")
        if num % 3 == 0:
            print("", end="\n")  #3단씩 끊어서 출력이므로!
    print("")