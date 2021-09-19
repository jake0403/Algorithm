import sys
input = lambda : sys.stdin.readline().strip()

S = input()

def makePalindrome(S):
    answer = 0
    n = len(S)
    for i in range(n):
        if S[i:] == S[i:][::-1]:
            answer = n+i
            return answer
    return answer
print(makePalindrome(S))