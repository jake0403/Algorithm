from collections import Counter

def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    groups = [x for x in range(n+1)]
    ans = 0
    def find_set(x):
        while groups[x] != x:
            x = groups[x]
        return x
    for i in range(len(students1)):
        if queryType[i] != 'Total':
            groups[find_set(students2[i])] = find_set(students1[i])
        else:
            break
    group_cnt = Counter(groups[1:])
    print(group_cnt)
    for g in group_cnt:
        print(group_cnt[g])
        ans += group_cnt[g]
    return ans
queryType = ['Friend', 'Total']
n = 3
students1 = [1,2]
students2 = [2,3]

getTheGroups(n, queryType,students1,students2)