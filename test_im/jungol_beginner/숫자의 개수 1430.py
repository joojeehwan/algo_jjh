'''

이건 그 카운팅 배열을 사용하면 좋을 것 같다.


'''




n = int(input())
m = int(input())
k = int(input())

num = n * m * k

counting = [0] * 10

for i in str(num):

    counting[int(i)] += 1

# print(counting)

for i in range(len(counting)):
    print(counting[i])