import sys
#sys.setrecursionlimit(10**7)
def solution(money, costs):
    def dfs(m,c):
        nonlocal min_c, visited
        if min_c < c:
            return
        if m == money:
            if min_c < c:
                min_c = c
            return
        for i in range(6):
            if not visited[i] and m+money_unit[5-i] <= money:
                visited[5-i] = 1
                m+=money_unit[5-i]
                c+=money_dict[money_unit[5-i]]
                dfs(m,c)
                visited[5-i] = 0
                m-=money_unit[5-i]
                c+=money_dict[money_unit[5-i]]
    # 최소 비용을 찾기 위한 min 초기 값
    min_c = sys.maxsize
    money_dict = {}
    money_unit = [1,5,10,50,100,500]
    for i in range(len(money_unit)):
        money_dict[money_unit[i]] = costs[i]
    print(money_dict)
    visited = [0]*6
    dfs(0,0)
    return min_c

print(solution(4578,[1, 4, 99, 35, 50, 1000]))