name_list = ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]

def solution(name_list):
    answer = []
    N = len(name_list)
    idx = 0
    same = 65
    left = 0
    right = 1
    while right < N:
        if name_list[left] != name_list[right]:
            left+=1
            right+=1
            continue
        else:
            while name_list[left] != name_list[right]:
                right+=1
            for i in range(right-left+1):
                name_list[left+i]+=chr(same+i)
            left = right+1
            right = left+1
    return name_list

print(solution(name_list))