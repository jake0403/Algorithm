textLength = 10
starting = [3, 1, 2, 8, 8]
ending = [5, 3, 7, 10, 10]

def paperCuttings(textLength, starting, ending):
    words = list(set(zip(starting,ending)))
    print(words)
    ans = 0
    def collague(i):
        nonlocal used
        s, e = words[i]
        for k in range(s,e+1):
            if used[k]: return 0
        return 1


    for i in range(len(words)-1):
        used = [0]*(textLength+1)
        idx = i+1
        for j in range(words[i][0], words[i][1]+1):
            used[j] = 1
        while idx < len(words):
            ans += collague(idx)
            idx+=1

    return ans


print(paperCuttings(textLength,starting,ending))