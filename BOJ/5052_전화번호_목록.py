import sys

T = int(sys.stdin.readline())
for tc in range(T):
    num_list = []
    answer = 0
    n = int(sys.stdin.readline())
    for i in range(n):
        num_list.append(sys.stdin.readline().strip())
    num_list.sort()

    for i in range(n - 1):
        if num_list[i + 1].startswith(num_list[i]):
            print('NO')
            answer = 1
            break
    if answer == 0:
        print('YES')