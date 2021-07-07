v = int(input())
ind = [2,3,5,7,11]
answer = []
for i in ind:
    count = 0
    while v % i == 0:
        v/=i
        count+=1
    answer.append(count)

answer = [str(x) for x in answer]
answer = ' '.join(answer)
print(f'# {answer}')
