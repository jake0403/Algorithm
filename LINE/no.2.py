from collections import Counter
def solution(inp_str):
    answer = []
    # 1번 조건
    def num_1(inp_str):
        if len(inp_str) < 8 or len(inp_str) > 15:
            answer.append(1)
            return
    # 2번 조건
    def num_2(inp_str):
        spe = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
        for inp in inp_str:
            if inp.isalnum():
                continue
            elif inp in spe:
                continue
            else:
                answer.append(2)
                return
    # 3번 조건
    def num_3(inp_str):
        chk = [0]*4
        spe = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
        for inp in inp_str:
            if inp.isalpha():
                if inp.isupper():
                    chk[0]=1
                elif inp.islower():
                    chk[1]=1
            elif inp.isdigit():
                chk[2]=1
            elif inp in spe:
                chk[3]=1
        if sum(chk) < 3:
            answer.append(3)
            return

    def num_4(inp_str):
        for i in range(len(inp_str)- 3):
            chk = inp_str[i:i+4]
            if chk.count(chk[0]) ==4:
                answer.append(4)
                return

    def num_5(inp_str):
        cnt = Counter(inp_str)
        for c in cnt:
            if cnt[c] >=5:
                answer.append(5)
                return
    num_1(inp_str)
    num_2(inp_str)
    num_3(inp_str)
    num_4(inp_str)
    num_5(inp_str)
    if not answer:
        answer = [0]
    return answer
# inp = "aaaaZZZZ)"
# print(solution(inp))