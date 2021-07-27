n = int(input())
result = 0
for i in range(1, n+1):
    if i < 100:
        result += 1
    else:
        splitNum = list(map(int, str(i)))
        if splitNum[1] - splitNum[0] == splitNum[2] - splitNum[1]:
            result+=1
print(result)
