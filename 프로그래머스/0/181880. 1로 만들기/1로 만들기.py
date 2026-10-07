def func(n): # 이거는 바텀업인데..
    if n < 0:
        return
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n ==2 or n==3:
        return 2
    
    if n > 2:
        return func(int(n/2)) + 1
    
    
def solution(num_list):
    answer = 0
    
    max_num = max(num_list)
    num_dp = [0] * (max_num+1)
    num_dp[2] = 1
    num_dp[3] = 1
    
    for n in range(4, max_num+1): # 4부터 카운트
        num_dp[n] = num_dp[int(n/2)] + 1
        
    count = 0
    for num in num_list:
        count += num_dp[num]
    
    
    return count