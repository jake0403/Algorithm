def calc(a,b,c):
    if c =='/':
        return a/b

    elif c =='*':
        return a*b
    elif c == '+':
        return a+b
    else:
        return a-b

def inOrder(n):
    if n > 0:
        left = inOrder(ch1[n])
        right = inOrder(ch2[n])
        if graph[n].isdigit():
            return int(graph[n])
        else:
            return calc(left, right, graph[n])




for tc in range(1, 11):
    N = int(input())
    graph = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for i in range(1,N+1):
        arr = list(input().split())
        if arr[1].isdigit():
            graph[i] = arr[1]
        else:
            graph[i] = arr[1]
            ch1[i] = int(arr[2])
            ch2[i] = int(arr[3])
    ans = int(inOrder(1))
    print(graph)
    print(ch1, ch2)
    print(ans)