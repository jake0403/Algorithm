import sys
input = sys.stdin.readline

N, M = map(int, input().split())
full_file = set(input() for _ in range(N))
# 확장자 list
extension = set(input() for _ in range(M))
full_file.sort()
for i in range(N-1):
    if full_file[i].split(".")[0] == full_file[i+1].split(".")[0]:
        if full_file[i].split(".")[1] not in extension and full_file[i+1].split(".")[1] in extension:
            full_file[i], full_file[i+1] = full_file[i+1], full_file[i]

for f in full_file:
    print(f.rstrip())