def solution(program, flag_rules, commands):
    answer = []
    commands = [list(commands[i].split()) for i in range(len(commands))]
    flag_rules = [list(flag_rules[i].split()) for i in range(len(flag_rules))]
    flag = True
    # flag name 저장하는 리스트 생성(e.g. -s, -n, -e)
    flag_name = [x[0] for x in flag_rules]
    # flag 변수 타입 저정하는 리스트 생성(e.g NULL, NUMBER ....)
    flag_argument_type = [x[1] for x in flag_rules]

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
            for i in range(1, len(com)):
                if flag == False: break
                # flag_rules의 타입이 일치하는지 확인
                for fl in flag_rules:
                    # end 명령어 입력 시 뒤에 Null 값이 아니면
                    if fl[0] == "-e" and com[-1] != fl[0]:
                        # answer에 False 넣고 loop 탈출
                        flag = False
                        break

                    # flag 일 때
                    if fl[0] == com[i]:
                        # flag가 flag_argument_type(문자)과 일치하지 않는다면
                        if 'STR' in fl[1]:
                            # 복수일 때(STRINGS)
                            if fl[1][-1] == 'S':
                                n = 1
                                # 다음 flag가 나오기 전까지
                                # 올바른 flag_arguments인지 확인
                                while com[i + n] not in flag_name:
                                    if not com[i + n].isalpha():
                                        flag = False
                                        break
                                    n += 1
                            # 단수일 때(STRING)
                            else:
                                if not com[i + 1].isalpha():
                                    flag = False
                                    break
                                elif i+2 < len(com) and com[i+2] not in flag_name:
                                    flag = False
                                    break
                        # flag가 flag_argument_type(숫자)과 일치하지 않는다면
                        elif "NUM" in fl[1]:
                            # 복수일 때(NUMBERS)
                            if fl[1][-1] == 'S':
                                n = 1
                                # 다음 flag가 나오기 전까지
                                # 올바른 flag_arguments인지 확인
                                while com[i + n] not in flag_name:
                                    if not com[i + n].isdigit():
                                        flag = False
                                        break
                                    n += 1
                            # 단수일 때(STRING)
                            else:
                                if not com[i + 1].isalpha():
                                    flag = False
                                    break
                                elif i+2 < len(com) and com[i+2] not in flag_name:
                                    flag = False
                                    break
            answer.append(flag)
            flag = True
    return answer
program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]
print(solution(program,flag_rules,commands))