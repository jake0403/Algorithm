r, c = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())
pillow = Rp*Cp
room = []
pc = 0
for i in range(r):
    t = list(input())
    pc += t.count('P')
    room.append(t)
if pillow == pc:
    print(0)
else:
    print(1)