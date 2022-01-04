# 단순하게 부분집합 생성



#단순하게 부분집합 생성,,!
bit = [0,0,0,0]
for i1 in range(2):
    bit[0] = i1
    for i2 in range(2):
        bit[1] = i2
        for i3 in range(2):
            bit[2] = i3
            for i4 in range(2):
                bit[3] = i4
                print(bit)



arr = [1,2,3]
n = len(arr)

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j): #i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=' ')
    print()