data = input()

count0 = 0

count1 = 0


if data[0] == "1":
    #처음의 숫자 확인
    count0 += 1

else:
    count1 += 1


for i in range(len(data) - 1):
    #여기에 i + 1 이 있으니깐 위에서 인덱스 하나 뺴준 것!
    if data[i] != data[i + 1]:

        if data[i + 1] == "1":
            count0 += 1

        else:
            count1 += 1

print(min(count0, count1))
