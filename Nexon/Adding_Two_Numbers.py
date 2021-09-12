import math
def addNumbers(a,b):
    ans = int(a+b)
    ans2 = math.floor(a+b)
    return [ans, ans2]


a = 2.34
b = 5.7898989
print(addNumbers(a,b))