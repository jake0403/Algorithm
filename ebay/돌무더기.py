from copy import deepcopy
def solution(stones, k):
    def dfs(stone, move):
        global wins
        if sum(stone) < k:
            return
        elif sum(stone) == k:
            if stone.count(0) == k-1 and stone.count(k) == 1:
                wins.append(move)
        else:
            for r in rules:
                for i in range(k):
                    stone[i] += r[i]
                    if r[i] == 1:
                        move += str(i)
                dfs(stone, move)
        return
    answer = ''
    N = len(stones)
    game = [-1]*N
    rules = []
    wins = []
    for i in range(N):
        g = deepcopy(game)
        g[i] = 1
        rules.append(g)



    dfs(stones, "")
    return wins
stones = [1,3,2]
print(solution(stones, 3))