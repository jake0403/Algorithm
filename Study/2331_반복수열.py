import sys
input = sys.stdin.readline

A, P = map(int, input().split())

# 최대 값 = (9^5)*4
D = [0]*246196
# 반복수열 개수
routineNum = 1
# 숫자 쪼개기
def splited(A,P):
    sub = 0
    for a in str(A):
        sub+=(int(a)**P)
    return sub

def findRoutine(A,P,D,rn):
    if D[A]:
        return D[A]-1
    D[A] = rn
    rn+=1
    splitNum = splited(A,P)
    return findRoutine(splitNum,P,D,rn)

print(findRoutine(A,P,D,routineNum))
