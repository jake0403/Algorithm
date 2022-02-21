from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = [list(x.split()) for x in report]
    # 신고한 리스트
    noo_list = defaultdict(set)
    # 신고 당한 횟수
    bu = defaultdict(int)
    bu_list = []
    for i in id_list:
        bu[i] = 0
    for r in report:
        noo_list[r[0]].add(r[1])

    for noo in noo_list.values():
        for n in noo:
            bu[n] += 1
    for b in bu:
        if bu[b] >= k:
            bu_list.append(b)
    if not bu_list:
        return answer

    for noo in noo_list:
        for b in bu_list:
            if b in noo_list[noo]:
                answer[id_list.index(noo)] += 1
    return answer