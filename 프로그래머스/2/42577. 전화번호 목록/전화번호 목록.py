def solution(phone_book):
    # 1. 모든 전화번호를 해시 맵에 담기
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    
    # 2. 각 번호의 접두어가 해시 맵에 있는지 확인
    for number in phone_book:
        temp = ""
        # 자기 자신을 제외한 접두어 조각들을 검사
        for digit in number[:-1]: 
            temp += digit
            if temp in hash_map:
                return False
                
    return True
#    answer = True
# 시간 초과, 입력값이 10^5이하여야.. 지금은 10^6이라서, 최악의 경우엔 시간 복잡도 = 10^6 * 10^6 = 1조임.   
#     for idx_pre in range(len(phone_book)):
#         pre = phone_book[idx_pre]
#         for idx_side in range(len(phone_book)):
        
#             if (idx_pre == idx_side) or (len(pre) > len(phone_book[idx_side])):
#                 continue
            
#             side_temp = phone_book[idx_side]
#             side = side_temp[:len(pre)]
            
#             if pre == side:
#                 return False
            
#   return answer