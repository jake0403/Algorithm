from math import ceil
def solution(n, clockwise):
    answer = [[]]
    arr = [[0]*n for _ in range(n)]
    ctr = [0,1,0,-1]
    ctc = [1,0,-1,0]

    cfr = [1,0,-1,0]
    cfc = [0,1,0,-1]
    finish = ceil(n**2//2)

    start = [[0,0],[0,n-1],[n-1,0],[n-1,n-1]]

    def screw(r,c):
        k = 1
        for i in range(n-k):
            pass

    return answer

n = 9
k = 1
while k<n:
    for i in range(n-k):
        print(i)
    k+=1
n =5
clockwise=True
result =[[1,2,3,4,1],[4,5,6,5,2],[3,6,7,6,3],[2,5,6,5,4],[1,4,3,2,1]]
#6	False	[[1,5,4,3,2,1],[2,6,8,7,6,5],[3,7,9,9,8,4],[4,8,9,9,7,3],[5,6,7,8,6,2],[1,2,3,4,5,1]]
#9	False	[[1,8,7,6,5,4,3,2,1],[2,9,14,13,12,11,10,9,8],[3,10,15,18,17,16,15,14,7],[4,11,16,19,20,19,18,13,6],[5,12,17,20,21,20,17,12,5],[6,13,18,19,20,19,16,11,4],[7,14,15,16,17,18,15,10,3],[8,9,10,11,12,13,14,9,2],[1,2,3,4,5,6,7,8,1]]