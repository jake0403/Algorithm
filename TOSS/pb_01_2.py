from collections import defaultdict
name_list = ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]

def solution(name_list):
    N = len(name_list)
    compare = defaultdict(int)
    for name in name_list:
        compare[name]+=1
    same = 65
    for i in range(N-1,-1,-1):
        if compare[name_list[i]] > 0:
            compare[name_list[i]]-=1
            name_list[i]+=chr(same+compare[name_list[i]])
    return name_list


print(solution(name_list))