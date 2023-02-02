def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        res = 1
        for j in range(1, i//2 + 1):
            if i % j == 0:                
                res += 1
                
        if res % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer