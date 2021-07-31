road ="111011110011111011111100011111"
max_length = 0
cnt = 0
n = 3
for i in range(len(road)):
    while cnt < n :
        for j in range(i, len(road)):
            if road[j] == 0:
                cnt+=1
# 투포인터로 접근