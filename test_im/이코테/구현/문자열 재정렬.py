'''

알파벳 대문자와 숫자 (0 ~ 9)로만 구성된 문자열이 입력으로 주어짐
이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

'''



datas = input()
res = []
val = 0
#아 이스 알파가 있지,,!! 이 바보!



for data in datas:

    if data.isalpha():
        res.append(data)

    else:
        val += int(data)

res.sort()

if val != 0:
    res.append(str(val))

print("".join(res))

