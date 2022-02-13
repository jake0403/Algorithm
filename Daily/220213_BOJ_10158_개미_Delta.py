import sys
input = lambda : sys.stdin.readline().strip()

''' [시간초과 코드]
def move():
    d1 = d2 = 1
    for i in range(t):
        if ant[0] == 0 or ant[0] == w:
            d1 *= -1
        if ant[1] == 0 or ant[1] == h:
            d2 *= -1
        ant[0]+=d1
        ant[1]+=d2

w, h = map(int, input().split())
ant = list(map(int, input().split()))
t = int(input())
move()
print(*ant)
'''
w, h = map(int, input().split())
ax, ay = map(int, input().split())
t = int(input())
print(w - abs(w-(t+ax)%(2*w)), h-abs(h-(t+ay)%(2*h)))