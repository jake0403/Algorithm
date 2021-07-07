N = int(input())
a = list(map(int,input().split()))
a.sort()
print(a)
mn = 0
answer = []
for i in a:
    mn+=i
    answer.append(mn)
print(sum(answer))