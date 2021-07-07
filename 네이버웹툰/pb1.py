from collections import defaultdict
def solutions(lottery):
    jackpot = defaultdict(list)
    for l in lottery:
        jackpot[l[0]].append(l[1])
    answer = []

    for j in jackpot:
        for idx in range(len(jackpot[j])):
            if jackpot[j][idx] == 1:
                answer.append(idx+1)
                break
    if not answer:
        return 0
    ans = sum(answer) // len(answer)
    return ans


lt = [[1,0],[2,0],[3,0]]
print(solutions(lt))