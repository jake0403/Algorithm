'''
1.  arr = [4,5,2,3,1] , k = 2,  result = 4
2.  arr = [5,4,3,2,1] , k = 4,  result = 2
3.  arr = [5,4,3,2,1] , k = 2,  result = 4
'''

arr = [4,5,2,3,1]
k = 2
result = 4
switch = []
for i in range(len(arr)):
    if arr[i] != i+1:
        switch.append([i, arr[i]])

print(switch)