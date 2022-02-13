from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
pop_list = list(map(int, input().split()))
dq = deque([x+1 for x in range(N)])
cnt = 0
for p in pop_list:
    while True:
        if dq[0] == p:
            dq.popleft()
            break
        else:
            if dq.index(p) < len(dq)/2:
                while dq[0] != p:
                    dq.append(dq.popleft())
                    cnt+=1
            else:
                while dq[0] != p:
                    dq.appendleft(dq.pop())
                    cnt+=1
print(cnt)