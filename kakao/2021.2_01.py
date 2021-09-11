from collections import defaultdict
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
def solution(id_list, report, k):
    answer = [0]*(len(id_list))
    report = [list(r.split()) for r in report]
    re_dict = defaultdict(set)
    for r in report:
        re_dict[r[0]].add(r[1])
    print(re_dict)
    points = defaultdict(int)
    for rd in re_dict:
        for d in re_dict[rd]:
            points[d]+=1
    print(points)
    for rd in re_dict:
        for r in re_dict[rd]:
            if points[r] >= k:
                answer[id_list.index(rd)]+=1
    # for idx, rd in enumerate(re_dict):
    #     for i in re_dict[rd]:
    #         if points[i] >= k:
    #             answer[idx]+=1
    return answer

print(solution(id_list, report,2))