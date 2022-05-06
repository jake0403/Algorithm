sentence1 = ["line in line", "LINE", "in lion"]
n1 = 5
# result = 20  (12,8,7)
sentence2 = ["ABcD", "bdbc", "a", "Line neWs"]
n2 = 7
# result = 12 (7,4,1,11)
board = [0]*len(sentence2)
total_key = []
for i in range(len(sentence2)):
    print(set(sentence2[i].replace(" ","")))
    key = list(set(sentence2[i].replace(" ", "").lower()))
    total_key.append(key)
    cnt = 0
    for s in sentence2[i]:
        if s.isupper():
            cnt += 1
            if 'shift' not in key:
                key.append('shift')
    print(key)
    if len(key) <= n2:
        board[i] = len(sentence2[i]) + cnt
    print(board)
max_score = 0
for total in total_key:
    score = 0
    for t in total[:-1]:
        if t not in total:
            pass





def solution(sentences, n):
    answer = -1
    return answer