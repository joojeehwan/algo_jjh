


def perm(n, k):
    if k == n:
        print(p)

        return

    else:

        for i in range(k, n): #K까지는 확정이니 그 다음부터 고른다!
            p[k], p[i] = p[i], p[k]
            perm(n, k+1) # 그 찾고자 하는 k자리 그 오른쪽 자리를 보아라!
            p[k], p[i] = p[i], p[k]



#교환을 해서 이게 사전적 순서대로 안되는 것!
p = [1,2,3]

perm(3,0)