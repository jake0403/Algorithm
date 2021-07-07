def solution(n, k, command):
    answer = ''
    table = [1] * (n+1)
    remember_c = []
    for cmd in command:
        # 내려가고 올라가는 명령어
        if cmd[0] == 'D' or cmd[0] == 'U':
            num = ''
            # X를 확인
            for i in range(2, len(cmd)):
                num += cmd[i]
            num = int(num)
            # 아래로 내려갈 때
            if cmd[0] == 'D':
                if table[k+num] == 0:
                    while table[k+num] == 0:
                        num+=1
                if k + num < n:
                    z_cnt = table[k:k+num+1].count(0)
                else:
                    z_cnt = table[k:].count(0)
                k += (num + z_cnt)
            # 위로 올라갈 때
            else:
                # 이전 값의 k를 확인 => 삭제된 값은 건너 뛰어야함
                if table[k] == 0:
                    while table[k] == 0:
                        k+=1
                if table[k-num] == 0:
                    while table[k-num] == 0:
                        num+=1
                if k - num >0:
                    z_cnt = table[k-num:k].count(0)
                else:
                    z_cnt = table[1:k].count(0)
                k -= (num + z_cnt)
        elif cmd[0] == 'C':
            table[k] = 0
            remember_c.append(k)
            # 마지막 행일 때는 윗 행 선택
            if k == n:
                k -= 1
                if table[k] == 0:
                    while table[k] == 0 and k > 1:
                        k-=1
            else:
                k += 1
                if table[k] == 0:
                    while table[k] == 0 and k < n:
                        k+=1

        elif cmd[0] == 'Z':
            table[remember_c.pop()] = 1
        print(cmd, k)
        print(table)

    for t in table:
        if not t:
            answer+='X'
        else:
            answer+='O'
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))