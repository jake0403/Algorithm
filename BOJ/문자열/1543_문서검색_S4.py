import sys
input = lambda : sys.stdin.readline().strip()


doc = input()
search = input()
ans = 0
N = len(doc)
n = len(search)

i = 0
while i <= N - n:
    if doc[i:i+n] == search:
        ans+=1
        i+=n
    else:
        i+=1

print(ans)