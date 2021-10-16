room = [".$.$$.", "$....$", ".$..##", "$....#", "######"]

def solution(room):
    answer = 0
    room = [list(x) for x in room]
    N = len(room)
    M = len(room[0])

    for i in range(N-1):
        for j in range(M):
            if room[i][j] == '$':
                answer+=1
                for k in range(i, N-1):
                    if room[k+1][j] == '#':
                        room[k][j] ='$'
                        room[i][j] = '.'
                        break
    return answer

print(solution(room))
