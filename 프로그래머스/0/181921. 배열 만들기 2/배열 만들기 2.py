# 연결 테스트 제발
def solution(l, r):
    answer = []

    for i in range(l, r + 1):
        if all(x in "05" for x in str(i)):
            answer.append(i)

    if not answer:
        return [-1]

    return answer