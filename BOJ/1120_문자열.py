import sys
a, b = input().split()
min_num = sys.maxsize
for i in range(len(b)-len(a)+1):
    num = 0
    for j in range(len(a)):
        if b[i+j] != a[j]:
            num+=1
    min_num = min(min_num, num)
print(min_num)