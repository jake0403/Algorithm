import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().strip()

def lucky_word(pre_word, cnt):
    global answer
    if cnt == len(String):
        answer+=1
        return
    for s in s_dict.keys():
        if pre_word == s:
            continue
        if s_dict[s] == 0:
            continue
        s_dict[s]-=1
        lucky_word(s,cnt+1)
        s_dict[s]+=1


String = input()
s_dict = defaultdict(int)
for s in String:
    s_dict[s] += 1
answer = 0
lucky_word("",0)
print(answer)