def solution(grid):
    N, M = len(grid), len(grid[0])

    for i in range(1, N):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, M):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, N):
        for j in range(1, M):
            select = min(grid[i - 1][j], grid[i][j - 1])
            grid[i][j] += select

    result = grid[N - 1][M - 1]

    return result

grid = [ [1, 8, 3, 2], [7, 4, 6, 5] ]
print(solution(grid))