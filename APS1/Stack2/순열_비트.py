arr = [1,2,3]

N = len(arr)

sel = [0] * N

# check 10진수 정수
def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        # check에 해당 값이 있으면 continue
        if check & (1 << j): continue

        sel[idx] = arr[j]
        perm(idx+1, check | (1<<j)) # 원상 복구가 필요없다.



perm(0,0)