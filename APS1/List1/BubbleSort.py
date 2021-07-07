# 5
# 7 3 4 5 1

N = int(input())
A = list(map(int,input().split()))
print(A)

def bubbleSort(A):
    for i in range(len(A)-1,0,-1 ):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

print(bubbleSort(A))

