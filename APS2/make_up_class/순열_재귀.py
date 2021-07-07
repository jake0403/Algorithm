def f2(i, n, k):
    if i == k:
        print(p)
    else:
        for j in range(n):
            if u[j] == 0:
                u[j] = 1
                p[i] = arr[j]
                f2(i+1, n, k)
                u[j] = 0

N = 5
K = 3
arr = [1,2,3,4,5]
u = [0] * N
p = [0] * K
f2(0, N, K)

def f(i, n, k):  # p[i]에 들어갈 숫자를 정하는 단계
    if i == k:  # 순열의 크기와 비교
        #print(p[:k])
        pass
    else:
        for j in range(i, n):  # p[i]를 p[j]와 교환해 p[i]를 결정
            print(i)
            p[i], p[j] = p[j], p[i]
            f(i+1, n, k)  # p[i+1]을 결정하러 이동
            p[i], p[j] = p[j], p[i]  # 원래위치로 되돌리고 다음 j와 교환 준비

N = 5
K = 3
p = [x for x in range(1,N+1)]
f(0, N, K)
