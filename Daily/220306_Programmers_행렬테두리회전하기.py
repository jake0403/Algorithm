def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            arr[i - 1][j - 1] = (i - 1) * columns + j

    for t, l, b, r in queries:
        top, left, bottom, right = t - 1, l - 1, b - 1, r - 1
        tmp = arr[top][left]
        min_num = tmp
        for d in range(top, bottom):
            check = arr[d+1][left]
            arr[d][left] = check
            min_num = min(min_num, check)
        for d in range(left, right):
            check = arr[bottom][d+1]
            arr[bottom][d] = check
            min_num = min(min_num, check)
        for d in range(bottom, top, -1):
            check = arr[d-1][right]
            arr[d][right] = check
            min_num = min(min_num, check)
        for d in range(right, left, -1):
            check = arr[top][d-1]
            arr[top][d] = check
            min_num = min(min_num, check)
        arr[top][left + 1] = tmp
        answer.append(min_num)

    return answer

rows = 3
columns = 5
queries = [[1, 1, 2, 2], [2, 3, 3, 4], [1, 2, 3, 4], [1, 1, 3, 4], [2, 2, 3, 5]]
print(solution(rows, columns, queries))