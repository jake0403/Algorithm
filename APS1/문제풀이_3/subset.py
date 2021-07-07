c = 3
a = [i for i in range(1,c+1)]   # a = [1,2,3]
subset = [[]]
for x in a:     #a의 원소를 한 개씩 꺼내
    size = len(subset)
    for y in range(size):       #subset의 각 원소에 더한 원소를 subset에 추가
        #subset.append([x for x in subset[y] + [x]])
        subset.append(subset[y] + [x])
print(subset)