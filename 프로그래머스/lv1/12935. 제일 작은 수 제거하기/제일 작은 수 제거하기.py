def solution(arr):
    answer = []
    n = len(arr)
    if n == 1:
        return [-1]
    else:
        minIdx = 0
        for i in range(n):
            if arr[minIdx] > arr[i]:
                minIdx = i
        
        # print(minIdx)
    
        arr.pop(minIdx)
        answer = arr
    return answer