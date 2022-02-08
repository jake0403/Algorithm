import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
info = []
country = set()
for i in range(N):
    student = list(map(int, input().split()))
    info.append(student)
    country.add(student[0])
info.sort(key= lambda x: x[2], reverse=True)
check = [0]*len(country)
medal = 0
answer = []
for i in range(N):
    if len(answer) == 3:
        break
    if check[info[i][0]-1] == 2:
        continue
    else:
        check[info[i][0]-1]+=1
        answer.append([info[i][0], info[i][1]])
for a,b in answer:
    print(a,b)