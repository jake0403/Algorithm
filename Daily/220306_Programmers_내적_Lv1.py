a = [1,2,3,4]
b = [-3,-1,0,2]
def solution(a, b):
    answer = 0
    for sa, sb in zip(a,b):
        answer+= sa*sb
    return answer
