## 백준 1254 팰린드롬 만들기 문제랑 같음
plain = "abcde"

def solution(plain):
    n = len(plain)
    for i in range(n):
        if plain[i:] == plain[i:][::-1]:
            answer = n+i
            return answer

print(solution(plain))