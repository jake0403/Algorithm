import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
maxN = arr[0]
minN = arr[0]

for i in range(1,n):
    maxN = [
        max(maxN[0], maxN[1]) + arr[i][0],
        max(maxN[0], maxN[1], maxN[2]) + arr[i][1],
        max(maxN[1], maxN[2]) + arr[i][2]
    ]
    minN = [min(minN[0], minN[1]) + arr[i][0],
            min(minN[0], minN[1], minN[2]) + arr[i][1],
            min(minN[1], minN[2]) + arr[i][2]
            ]
maxN = max(maxN)
minN = min(minN)
print(maxN, minN)