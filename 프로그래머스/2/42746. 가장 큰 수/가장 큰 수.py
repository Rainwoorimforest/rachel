from functools import cmp_to_key

def solution(numbers):
    tmp = list(map(str, numbers))
    
    def compare(a,b):
        if a + b > b + a:
            return -1 # 첫번째 인자 a가 먼저 나옵니다. ex) ab
        elif a + b < b + a:
            return 1 # 두번째 인자 b가 먼저 나옵니다. ex) ba
        else: 
            return 0 # 순서 상관없이
    
    tmp.sort(key=cmp_to_key(compare))    
    answer = ''.join(tmp)
    
    # 이 케이스를 생각했어야 했네 ah
    if tmp[0] == '0':
        answer = '0'
    
    return answer