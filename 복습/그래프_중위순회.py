'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''

def inOrder(idx):
    global word
    if idx > N:
        return
    inOrder(2*idx)
    word+=arr[idx]
    inOrder(2*idx+1)


T = 10
for tc in range(T):
    N = int(input())
    word = ''
    arr = [0]*(N+1)
    for i in range(N):
        info = list(input().split())
        arr[int(info[0])] = info[1]
    inOrder(1)
    print(word)