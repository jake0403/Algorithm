textLength = 10
starting = [3, 1, 2, 8, 8]
ending = [5, 3, 7, 10, 10]

def paperCuttings(textLength, starting, ending):
    words = list(set(zip(starting,ending)))
    words.sort()
    ans = 0
    for i in range(len(words)-1):
        idx = i+1
        while idx < len(words):
            if words[i][1] >= words[idx][0]:
                idx+=1
                continue
            else:
                ans+=1
                idx+=1
    return ans


print(paperCuttings(textLength,starting,ending))