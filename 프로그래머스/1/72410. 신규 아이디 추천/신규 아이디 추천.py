# 입력값을 받고 규칙에 맞으면 그대로 출력
# 규칙에 맞지않으면 7단계 진행 -> 그냥 일괄 7단계 진행하고 규칙 적용되면 Pass 하는 형태로 작성한다.
import string

def solution(new_id):
    new_input = new_id
    possible_st = ['-','_','.']
    

    # 1
    new_input = new_input.lower() # 원본이 바뀌도록 다시 주입
    
    # 2 허용되는 문자만 새 문자열에 넣는 방식을 이용한다.
    process_input = ""
    for s in new_input:
      if s.isdigit() or s.islower() or (s in possible_st):
        process_input += s
      
    
    # 3 연속으로 나올떄를 어떻게 처리할까?
    while '..' in process_input:
      process_input = process_input.replace("..", ".")
            
    # 4
    if process_input.startswith("."):
        process_input = process_input[1:]
    
    if process_input.endswith("."):
        process_input = process_input[:-1]
        
    # 5
    if process_input=="": # 공백 문자인지 빈 문자인지 구분행한다. 공백 " ", 빈문자열 ""
        process_input += 'a'
        
    # 6
    process_input = process_input[:15]
    if process_input.endswith("."):
        process_input = process_input[:-1]
        
    # 7
    while len(process_input) <= 2:
        process_input += process_input[-1]
            
            
    return process_input


