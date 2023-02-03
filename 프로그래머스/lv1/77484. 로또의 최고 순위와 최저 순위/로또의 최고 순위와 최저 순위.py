def solution(lottos, win_nums):
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
        elif lotto == 0:
            zero_cnt += 1
            
    answer = [rank[zero_cnt + cnt], rank[cnt]]
    return answer