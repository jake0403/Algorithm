prices = [1,2,3,2,3]
def solution(prices):
    answer = []
    for i in range(len(prices)):
        stock = 0
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                stock+=1
                break
            else:
                stock+=1
        answer.append(stock)
    return answer
print(solution(prices))