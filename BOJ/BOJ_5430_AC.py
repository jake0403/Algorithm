import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    func = input()
    func = func.replace("RR",'')
    N = int(input())
    arr = input()
    arr = arr[1:-1].split(',')

    rv = front = back = 0

    for f in func:
        if f == "R":
            rv+=1
        else:
            if rv % 2 == 0:
                front+=1
            else:
                back+=1

    if front+back <= N:
        arr = arr[front: N-back]
        if rv % 2 != 0:
            print(f"[{','.join(arr[::-1])}]")
        else:
            print(f"[{','.join(arr)}]")
    else:
        print("error")