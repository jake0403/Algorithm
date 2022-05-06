# 특정 조건 로그 수집
'''
t = 'team_name'
a = 'application_name'
e = 'error_level'
m = 'message'
'''
logs = ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]
# answer =3
#logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
# answer = 6
# cnt = 0
def solution(logs):
    cnt = 0
    t = 'team_name'
    a = 'application_name'
    e = 'error_level'
    m = 'message'
    for l in logs:
        if len(l) > 100:
            cnt += 1
            continue
        log = l.split(" ")
        if len(log) != 12:
            cnt += 1
            continue
        if t not in log or a not in log or e not in log or m not in log:
            cnt+=1
            continue
        for i in [2,5,8,11]:
            if not log[i].isalpha():
                cnt+=1
                break

    return cnt

print(solution(logs))