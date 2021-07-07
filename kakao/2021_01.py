def solution(s):
    answer = 0
    num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',

    }
    num_change = ''
    str_num = ''
    for i in range(len(s)):
        if s[i].isdigit():
            num_change += s[i]
        else:
            str_num += s[i]
            if len(str_num) >= 3 and str_num in num_dict:
                num_change+=num_dict[str_num]
                str_num =''

    return num_change

s = "one4seveneight"
print(solution(s))