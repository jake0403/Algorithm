arr = [x+1 for x in range(10)]

N = len(arr)

sel = [0]*N # 결과들이 저장될 리스트

def perm(idx, check):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1<<j): continue
