def downgrade(limit, sub):
    global count, answer
    if len(sub) == limit:
        count+=1
        if count == n:
            answer = int(sub)
            print(answer)
            sys.exit()
        return
    else:
        if sub == '':
            for i in range(limit-1, 10):
                sub+= str(i)
                downgrade(limit, sub)
                sub = ''
        else:
            for i in range(int(sub[-1])):
                if limit - len(sub) -1 >i:
                    continue
                sub+= str(i)
                downgrade(limit, sub)
                sub = sub[:-1]

import sys
n = int(sys.stdin.readline())
count = answer = -1
for num in range(1,11):
    downgrade(num, '')
print(-1)