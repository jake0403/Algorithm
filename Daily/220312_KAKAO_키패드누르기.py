from collections import deque
def solution(numbers, hand):
    answer = ''
    hand_locate = {
        'L': '*',
        'R': '#'
    }
    dial_dict = {}
    dial = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    for i in range(4):
        for j in range(3):
            dial_dict[dial[i][j]] = [i, j]

    def bfs(delta, d):
        r, c = delta
        q = deque([])
        q.append([r, c])
        cnt = 0
        visited = [dial[r][c]]
        flag = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 4 and 0 <= nc < 3:
                        if dial[nr][nc] not in visited:
                            if dial[nr][nc] == d:
                                flag = 1
                            else:
                                q.append([nr, nc])
                                visited.append(dial[nr][nc])
            cnt+=1
            if flag:
                return cnt

    L = [1, 4, 7]
    R = [3, 6, 9]
    for n in numbers:
        if n in L:
            hand_locate['L'] = str(n)
            answer += 'L'
        elif n in R:
            hand_locate['R'] = str(n)
            answer += 'R'
        else:
            left = bfs(dial_dict[hand_locate['L']], str(n))
            right = bfs(dial_dict[hand_locate['R']], str(n))
            direction = 'R'
            # 두 손 거리가 동일할 때
            if left == right:
                # 왼손잡이
                if hand == 'left':
                    direction = 'L'
            # 오른쪽 거리가 더 멀다면
            elif left < right:
                direction = 'L'

            hand_locate[direction] = str(n)
            answer += direction

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers,hand))