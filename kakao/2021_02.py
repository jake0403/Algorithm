def solution(places):
    answer = []
    # places들 안에 있는 대기실을 리스트로 변환
    for place in places:
        place = [list(x) for x in place]
        n = 5
        def delta(r, c):
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0<=nr<n and 0<=nc<n:
                    if place[nr][nc] == 'P':
                        return 0
                    elif place[nr][nc] == 'O':
                        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            if nr + dx == r and nc + dy == c:
                                continue
                            nx, ny = nr + dx, nc + dy
                            if 0<=nx<n and 0<=ny<n and place[nx][ny] == 'P':
                                return 0
            return 1
        def check(arr):
            ans = 1
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if arr[i][j] == 'P':
                        if not delta(i,j):
                            ans = 0
                            return ans
            return ans
        answer.append(check(place))
    return answer



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))