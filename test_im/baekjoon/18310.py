'''


안테나



'''



n = int(input())

lst = list(map(int, input().split()))

lst.sort()

#중간값
print(lst[(n - 1) // 2])

