






def binary_search(array, target, start, end):
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) / 2
        if array[mid] == target:
            return (mid, cnt)

        elif array[mid] > target:
            end = mid -1

        else:
            start = mid + 1


    return None
array = []
for i in range(1, 401):
    array.append(i)
print(array)