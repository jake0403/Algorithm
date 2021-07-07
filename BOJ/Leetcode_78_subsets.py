
num = [1,2,3]
result = []

def dfs(i, visited):
    result.append(visited)

    for i in range(i, len(num)):
        dfs(i+1, visited + [num[i]])

dfs(0,[])
print(result)
