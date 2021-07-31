
color = ["YW", "RY", "WG", "BW"]
prices = [7561, 8945]

def solution(color, prices):
    from collections import defaultdict
    result = 0
    color = [list(x) for x in color]
    top = defaultdict(int)
    bottom= defaultdict(int)
    # 상하의 분리해서 저장
    for c in color:
        top[c[0]]+=1
        bottom[c[1]]+=1
    # 상의 하의가 짝을 이룬다면 result에 합산
    for t in top:
        if top[t] > 0 and bottom[t] > 0:
            result+=prices[0]
            top[t]-=1
            bottom[t]-=1
    cnt = 0
    # 짝을 이루지 않는다면 세트로 살 때와 추가요금 내고 나눠서 살 때 비교
    for t in bottom:
        if top[t] or bottom[t]:
            if top[t]:
                cnt+=top[t]
            else:
                cnt+=bottom[t]
    # 세트로 구매하는 것이 더 저렴하다면
    if prices[0] < prices[1]-prices[0]:
        result+=(cnt*prices[0])
    # 추가요금 낼 때가 더 저렴하다면
    else:
        result+=(cnt//2*prices[1])

    return result

solution(color, prices)