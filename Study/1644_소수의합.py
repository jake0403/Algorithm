N = int(input())

eratos = [1]*(N+1)
primeNum = []
eratos[0] = eratos[1] = 0

def findPrimeNum(eratos, primeNum):
    for i in range(2,N+1):
        if not eratos[i]:
            continue
        primeNum.append(i)
        for j in range(i**2, N+1, i):
            eratos[j] = 0

findPrimeNum(eratos, primeNum)

cnt = total = 0
if primeNum:
    total=primeNum[0]
    left = right = 0
    # 투포인터로 N 찾기
    while left <= right and right < len(primeNum):
        # 소수들의 합이 N보다 작거나 같을 때
        if total <= N:
            # 소수들의 합이 N이라면 개수+1
            if total == N:
                cnt+=1
            # N보다 작으면
            right += 1
            if right < len(primeNum):
                total += primeNum[right]
        else:
            total -= primeNum[left]
            left+=1
print(cnt)