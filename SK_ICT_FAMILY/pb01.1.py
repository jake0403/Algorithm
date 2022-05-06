import sys
sys.setrecursionlimit(10**9)
money = 1999
costs =[2, 11, 20, 100, 200, 600]
min_c = sys.maxsize
money_dict = {}
money_unit = [1,5,10,50,100,500]
for i in range(len(money_unit)):
    money_dict[money_unit[i]] = costs[i]
answer=[]
def dfs(m,c):
    if m > money:
        return
    if m == money:
        answer.append(c)
    for mn in money_unit[::-1]:
        c.append(mn)
        dfs(m,c)
        c.pop()

dfs(0,[])
print(answer)
