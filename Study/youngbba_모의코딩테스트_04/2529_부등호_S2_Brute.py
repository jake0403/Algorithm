import sys
input = lambda : sys.stdin.readline().strip()

def dfs(idx, s):
    global visited, max_num, min_num
    if idx == N+1:
        if not len(min_num):
            min_num = s
        else:
            max_num = s
        return
    for i in range(10):
        if not visited[i]:
            if idx == 0 or check(s[-1], str(i), arr[idx-1]):
                visited[i] = 1
                dfs(idx+1, s+str(i))
                visited[i] = 0


def check(i,j,c):
    if c == '>':
        return i > j
    else:
        return i < j



N = int(input())
min_num = ""
max_num = ""
arr = input().split()
visited = [0]*10
dfs(0,"")
print(max_num)
print(min_num)