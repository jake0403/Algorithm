from collections import defaultdict
import sys
input = lambda : sys.stdin.readline().strip()

def checker(word):
    n = len(word)
    if n == 1:
        return 1
    left = 0
    check = [word[left]]
    right = 1

    while right < n:
        if word[left] == word[right]:
            left+=1
            right+=1
        else:
            if word[right] in check:
                return 0
            check.append(word[right])
            right+=1
            left = right -1

    return 1


N = int(input())
ans = 0
for _ in range(N):
    words = input()
    ans+=checker(words)

print(ans)