'''


① Brute Force 기법 - 반복 / 조건문을 활용해 모두 테스트하는 방법
② 순열(Permutation) - n개의 원소 중 r개의 원소를 중복 허용 없이 나열하는 방법
③ 재귀 호출
④ 비트마스크 - 2진수 표현 기법을 활용하는 방법
⑤ BFS, DFS를 활용하는 방법

'''



#순차 탐색 구현


def squential_search(arr, k):
  i = 0

  while i < len(arr):
    if arr[i] == k:
        return arr[i]

    i += 1

    return -1



lst = [4,5,6,7,8,9]

a = squential_search(lst, 0)
print(a)
