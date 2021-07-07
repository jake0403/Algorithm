from itertools import combinations, permutations, product

# def solution(numbers: str) -> int:
#     numbers = [int(x) for x in numbers]
#     print(numbers)
#     # c = combinations()
#     p = list(permutations(numbers))
#     print(p)

from math import sqrt

numbers = input()
ans = []
for r in range(1, len(numbers)+1):
    perlist = list(map(''.join, permutations(list(numbers), r)))
    perlist = set([int(x) for x in perlist])
    for i in list(perlist):
        if i >= 2:
            m = int(sqrt(i)+1)
            for j in range(2,m+1):
                if i % j == 0:
                    break
            else:
                ans.append(i)
print(len(list(set(ans))))
# solution(numbers)