'''
문제 설명
모든 알파벳을 다 썼는지 안 썼는지 확인 후
안 썼으면 안 쓴 알파벳 모두 출력
다 썼으면 'perfect' 출력
'''
sentence = "His comments came after Pyongyang announced it had a plan to fire four missiles near the US territory of Guam."

def solution(sentence):
    answer = ""
    sentence = sentence.lower()
    sentence = list(set(''.join(filter(str.isalpha, sentence))))
    check = [0]*26
    for i in range(len(sentence)):
        check[ord(sentence[i]) - 97] = 1

    for i in range(26):
        if not check[i]:
            answer+=chr(i+97)
    if not answer:
        answer = 'perfect'
    return answer

print(solution(sentence))