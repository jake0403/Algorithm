from typing import List
def generateParenthesis(n: int) -> List[str]:
    result = []

    def backtrace(result, s, start, end, m):
        if start == m and end == m:
            result.append(s)
            return
        if start < m:  # open parenthesis num is less than max
            backtrace(result, s + "(", start + 1, end, m)
        if end < start:  # close parenthesis num is less than open num
            backtrace(result, s + ")", start, end + 1, m)

    backtrace(result, "", 0, 0, n)
    return result

generateParenthesis(3)