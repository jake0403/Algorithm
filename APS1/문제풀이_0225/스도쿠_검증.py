T = int(input())

def sudoku_check(sudoku):
    for i in sudoku:
        if sum(i) != 45:
            return 0
    tmp = 0
    for i in range(9):
        for j in range(9):
            tmp+=sudoku[j][i]
        if tmp != 45:
            return 0
        tmp = 0
    tmp = 0
    for i in range(0,9,3):
        for r in range(3):
            for c in range(3):
                tmp+=sudoku[i+r][i+c]
        if tmp != 45:
            return 0
        tmp = 0
    return 1

for tc in range(1, T+1):
    N = 9
    sudoku = [list(map(int, input().split())) for x in range(N)]
    print(f'#{tc} {sudoku_check(sudoku)}')

