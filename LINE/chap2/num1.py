def solution(program, flag_rules, commands):
    answer = []
    commands = [list(commands[i].split()) for i in range(len(commands))]
    flag_rules = [list(flag_rules[i].split()) for i in range(len(flag_rules))]
    flag = True
    # Command 개수 만큼 반복
    for com in commands:
        # program 명이 일치하지 않으면 break
        if com[0] != program:
            flag = False
            answer.append(flag)
            continue
        # program 명이 일치한다면
        else:
            # 명령어 프로그램 명 제외 후 loop
            for i in range(1,len(com)):
                # flag_rules의 타입이 일치하는지 확인
                for fl in flag_rules:
                    # end 명령어 입력 시 뒤에 Null 값이 아니면
                    if fl[0] == "-e" and com[-1] != fl[0]:
                        # answer에 False 넣고 loop 탈출
                        flag = False
                        break
                    # 명령어 일 때
                    if fl[0] == com[i]:
                        if fl[1] == 'STRING':
                            if not com[i+1].isalpha():
                                flag = False
                                break
                        elif fl[1] == "NUMBER":
                            if not com[i+1].isdigit():
                                flag = False
                                break
            answer.append(flag)
    return answer

commands = ["line -s 123 -n HI", "line fun"]
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
program = "line"
print(solution(program, flag_rules, commands))