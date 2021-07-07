numbers = input()

result = 0


def solution(numbers):
    # 특수문자 체크
    for num in numbers:
        if not (num.isdigit() or num.isalpha()):
            break
    else:
        return 'INVALID'

    # 연속된 숫자,문자 체크
    for idx in range(0, len(numbers) - 2):
        if numbers[idx] == numbers[idx + 1] == numbers[idx + 2]:
            return 'INVALID'

    result = 0

    # 룬 알고리즘 체크
    for idx in range(len(numbers)):
        # 해당 자리가 숫자인 경우
        if numbers[idx].isdigit():
            # 자릿수가 홀수인 경우
            if (idx + 1) % 2:
                result += int(numbers[idx])

            # 자릿수가 짝수인 경우
            else:
                temp = int(numbers[idx]) * 2
                while temp > 0:
                    result += temp % 10
                    temp //= 10
        # 해당 자리가 문자인 경우
        elif numbers[idx].isalpha():
            temp = ord(numbers[idx])
            # 자릿수가 홀수인 경우
            if (idx + 1) % 2:
                while temp > 0:
                    result += temp % 10
                    temp //= 10
            # 자릿수가 짝수인 경우
            else:
                temp *= 2
                while temp > 0:
                    result += temp % 10
                    temp //= 10
    print(result)
    # 유효셩 검사
    if result % 10 == 0:
        return 'VALID'
    else:
        return 'INVALID'


result = solution(numbers)
print(result)
