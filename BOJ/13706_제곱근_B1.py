n = int(input())

def binarySearch(front, end):
    mid = (front+end) //2
    while True:
        if mid ** 2 == n:
            print(mid)
            return
        elif mid **2 > n:
            end = mid
        elif mid**2 < n:
            front = mid
        mid = (front + end) // 2
binarySearch(1,n)
