import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
lesson = list(map(int, input().split()))
if N == 1:
    print(lesson[0])
    sys.exit()
front = max(lesson)
end = sum(lesson)

def binarySearch(left, right):
    while left <= right:
        mid = (left + right) // 2
        cnt = blueRayCnt(mid)

        if cnt > M:
            left = mid + 1
        else:
            right = mid - 1
    return left

def blueRayCnt(mid):
    cnt = 0
    total = 0
    for i in range(N):
        if total + lesson[i] > mid:
            cnt += 1
            total = 0
        total += lesson[i]
    else:
        if total:
            cnt+=1
    return cnt

print(binarySearch(front, end))