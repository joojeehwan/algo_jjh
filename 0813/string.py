# s1 = "a b c"
#
# s2 = s1.replace("a", "d")
#
# s3 = s1.split()
#
# s4, s5, s6 = s1.split() # 오 이렇게도 쓸 수 있다
# print(s3)
# print(s4, s5, s6)
# print(s1.replace("a", "d"))
# print(s1) # s1이 바꾸는 것이 아님!! 이거 주의!!
#
#
#
# s1 = "ab A"
#
# s1 = s1.replace("a", "b") #""안을 수정하는게 아니라 새로운 "" 객체를 가리키는 것!
#
#
# a = list(input())
# n = len(a) #글자수
# for i in range(n//2):
#     a[i], a[n-1-i] = a[n-1-i], a[i]# s[i] <-> s[n-1-i]
#
# cnt = [0] * 26 #카운츠,,,!
#
# s="aba"
# for x in s:
#     cnt[ord(x)-ord("a")] += 1
#
# print(cnt)

'''

== , is의 차이

is는 객체와 관련된 것!




'''