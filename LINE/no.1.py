def solution(table, languages, preference):
    total = [0]*len(table)
    table = [list(table[i].split()) for i in range(len(table))]
    for L in range(len(languages)):
        for i in range(len(table)):
            for j in range(1,6):
                if languages[L] == table[i][j]:
                    total[i]+=(6-j)*preference[L]
    maxT = max(total)
    if total.count(maxT) > 1:
        answer = []
        for t in range(len(total)):
            if maxT == total[t]:
                answer.append(table[t][0])
        answer.sort()
        ans = answer[0]
    else:
        ans = table[total.index(maxT)][0]

    return ans

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))